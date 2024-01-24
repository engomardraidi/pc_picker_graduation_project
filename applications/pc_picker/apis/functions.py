import os
import decimal
import pandas as pd
import numpy as np
from fuzzywuzzy import process
from jinja2 import Template
from rest_framework.response import Response
from numbers import Number
from ...core.functions import get_detail_response
from ...core.constants import Constants
from ...dashboard.models import MobileField

__NUM_OF_BEST = 3

def get_laptop_as_json(device, budget):
    return {
        'perc': (device.price / budget) * 100,
        'price': device.price,
        'device': device.to_json()
    }

def get_mobile_as_json(mobile, budget):
    return {
        'perc': (mobile.price / budget) * 100,
        'price': mobile.price,
        'mobile': mobile.to_json()
    }

def get_best_devices(devices):
    full_perc = decimal.Decimal(100)
    diff = 0
    best_devices = []

    if len(devices) > __NUM_OF_BEST:
        while len(best_devices) < __NUM_OF_BEST:
            diff += 2
            for device in devices:
                if len(best_devices) == __NUM_OF_BEST:
                    break
                check = device.get('check', False)
                if abs(device['perc'] - full_perc) <= diff and not check:
                    best_devices.append(device)
                    device['check'] = True
    else:
        best_devices = devices

    return best_devices

def validate_field_budget(field_model, field_id, budget):
    if field_id == None or budget == None:
        return Response(get_detail_response(Constants.REQUEIRED_FIELDS), status=400)
    elif (not isinstance(field_id,int) or not isinstance(budget,Number)) and field_model is not MobileField:
        return Response(get_detail_response(Constants.NOT_A_NUMBER), status=400)
    elif field_model is MobileField and (not isinstance(field_id,list) or not all(isinstance(i,int) for i in field_id)):
        return Response(get_detail_response(Constants.FIELD_NOT_A_LIST), status=400)
    elif field_model is MobileField and not isinstance(budget,Number):
        return Response(get_detail_response(Constants.BUDGET_NOT_A_NUMBER), status=400)

    if field_model is not MobileField and field_model.get_object(field_id) == None:
        return Response(get_detail_response(Constants.FIELD_NOT_EXIST), status=404)

    return None

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