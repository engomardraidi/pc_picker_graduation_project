import os
import pandas as pd
import numpy as np
from fuzzywuzzy import process
from jinja2 import Template

def get_None_or_JSON(instance):
    return None if instance == None else instance.to_json()

def get_total_price(motherboard, cpu, ram, gpu):
    motherboard_price = 0 if motherboard == None else motherboard.price
    cpu_price = 0 if cpu == None else cpu.cpu.price
    ram_price = 0 if ram == None else ram.ram.price
    gpu_price = 0 if gpu == None else gpu.gpu.price

    return motherboard_price + cpu_price + ram_price + gpu_price

def write_fun():
    
    script_dir = os.path.dirname(__file__)
    template_path = os.path.join(script_dir, 'jinja2_templates', 'rule_template.j2')

    with open(template_path, 'r') as file:
        rule_template_content = file.read()
    
    rule_template = Template(rule_template_content)

    fields = [] # models_dashboard.Field.get_objects()

    for field in fields:
        rendered_rule_template = rule_template.render(field=field)

        expert_system_file_path = os.path.join(script_dir, 'expert_system.py')

        with open(expert_system_file_path, 'r') as file:
            content = file.read()

        if rendered_rule_template not in content:
            with open(expert_system_file_path, 'a') as file:
                file.write('\n')
                file.write(rendered_rule_template)
                file.flush()

def find_closest_match(name, size, choices):
    filtered_choices = choices[choices['size'] == size]
    result = process.extractOne(name, filtered_choices['name'])
    if result == None:
        return name
    else:
        match, score, index = result
        matched_row = filtered_choices[filtered_choices['name'] == match].iloc[0]
        return matched_row['price'] if score >= 85 else None

def process_names():
    rams = pd.read_csv('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/rams.csv')
    rams_copy = pd.read_csv('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/rams_1-cleaned_copy.csv')
    result = find_closest_match('G.Skill Trident Z5 RGB 32 GB', 32, rams)

    rams_copy['new_price'] = rams_copy['new_price'].replace('', np.nan)
    rams_copy['new_price'] = rams_copy['new_price'].fillna(rams_copy['new_price'].mean())
    

    new_names = []
    new_prices = []
    count = 0

    for index, row in rams_copy.iterrows():
        result = find_closest_match(row['name'], int(str(row['size']).replace('GB', '').strip()), rams)
        if result == None:
            # new_names.append(None)
            new_prices.append(None)
        else:
            # new_names.append(match)
            new_prices.append(result)
        count += 1
        print(count)

    rams_copy['new_price'] = new_prices

    rams_copy.to_csv('/Users/eng.omar/Desktop/python_backend/pc_picker_graduation_project/datasets/rams_1-cleaned_copy.csv', index=False)