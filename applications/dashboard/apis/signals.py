from django.db.models.signals import post_save
from django.dispatch import receiver
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from django.conf import settings
from csv import writer
from .decorators import disable_for_loaddata
from .. import models
from . import serializers
import pandas as pd
import os
# from jinja2 import Template

# @receiver(post_save, sender=models.CaseStyle)
# def create_case_style_function_in_knowledge_engine(sender, instance, created, **kwargs):
#     if created:
#         script_dir = os.path.dirname(__file__)
#         template_path = os.path.join(script_dir, 'jinja2_templates', 'case_style_template.j2')

#         with open(template_path, 'r') as file:
#             rule_template_content = file.read()

#         rule_template = Template(rule_template_content)

#         rendered_rule_template = rule_template.render(style=instance)
#         expert_system_file_path = os.path.join('applications/pc_picker/apis/expert_system/pc_parts/cases_knowledge.py')

#         with open(expert_system_file_path, 'r') as file:
#             content = file.read()

#         if rendered_rule_template not in content:
#             with open(expert_system_file_path, 'a') as file:
#                 file.write('\n')
#                 file.write(rendered_rule_template)
#                 file.flush()
    

@receiver(post_save, sender=models.CPU)
@disable_for_loaddata
def classification_cpu(sender, instance, created, **kwargs):
    if created:
        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets')
        df_file = pd.read_csv(f'{BASE_DIR}/cpus_1-cleaned.csv')

        df = df_file.drop(columns=['integrated graphics', 'image_url', 'socket', 'producer', 'tdp'])

        X = df[['price', 'base_clock', 'turbo_clock', 'cores', 'threads']]

        y = df[['gaming', 'graphic design', 'programming', 'office']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the Random Forest classifier
        classifier = MultiOutputClassifier(RandomForestClassifier(random_state=42))

        # Train the model on the training data
        classifier.fit(X_train, y_train)

        # Make predictions on the test set
        predictions = classifier.predict(X_test)

        # Evaluate the accuracy for each label
        # for i, label in enumerate(y.columns):
        #     accuracy = accuracy_score(y_test[label], predictions[:, i])
        #     print(f'Accuracy for {label}: {accuracy}')

        # Display overall classification report
        # print('\nOverall Classification Report:\n', classification_report(y_test, predictions))


        new_data = pd.DataFrame({
            'price': [instance.price],
            'base_clock': [instance.base_clock],
            'turbo_clock': [instance.turbo_clock],
            'cores': [instance.cores],
            'threads': [instance.threads],
        })

        # Make predictions for the new data
        new_predictions = classifier.predict(new_data)

        list_data = []

        if new_predictions[0, 0]:
            # gaming
            list_data.append({'cpu': instance.id, 'field': 3})
        if new_predictions[0, 1]:
            # graphic design
            list_data.append({'cpu': instance.id, 'field': 2})
        if new_predictions[0, 2]:
            # programming
            list_data.append({'cpu': instance.id, 'field': 1})
        if new_predictions[0, 3]:
            # office
            list_data.append({'cpu': instance.id, 'field': 4})

        serializer = serializers.CPUFieldSerializer(data=list_data, many=True)
        if serializer.is_valid():
            serializer.save()

        new_row = [
            instance.id,
            instance.name,
            instance.socket.socket,
            instance.price,
            instance.producer.name,
            instance.base_clock,
            instance.turbo_clock,
            instance.cores,
            instance.threads,
            instance.tdp,
            instance.integrated_graphics,
            instance.external_image if instance.external_image is not None else instance.image,
            new_predictions[0, 0],
            new_predictions[0, 1],
            new_predictions[0, 2],
            new_predictions[0, 3]
        ]

        with open(f'{BASE_DIR}/cpus_1-cleaned.csv', 'a') as file:
            writer_object = writer(file)
            writer_object.writerow(new_row)
            file.close()

        # Display the predictions
        # print('Predicted classification for the new data:')
        # print('Gaming:', new_predictions[0, 0])
        # print('Graphic Design:', new_predictions[0, 1])
        # print('Programming:', new_predictions[0, 2])
        # print('Office:', new_predictions[0, 3])

@receiver(post_save, sender=models.RAM)
@disable_for_loaddata
def classification_ram(sender, instance, created, **kwargs):
    if created:
        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets')
        df_file = pd.read_csv(f'{BASE_DIR}/rams_1-cleaned.csv')

        df = df_file.drop(columns=['timings', 'sticks', 'image_url', 'producer'])

        X = df[['size', 'clock', 'memory_type', 'price']]
        X['memory_type'] = X['memory_type'].str.replace('DDR', '')

        y = df[['gaming', 'graphic design', 'programming', 'office']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the Random Forest classifier
        classifier = MultiOutputClassifier(RandomForestClassifier(random_state=42))

        # Train the model on the training data
        classifier.fit(X_train, y_train)

        # Make predictions on the test set
        predictions = classifier.predict(X_test)

        # # Evaluate the accuracy for each label
        # for i, label in enumerate(y.columns):
        #     accuracy = accuracy_score(y_test[label], predictions[:, i])
        #     print(f'Accuracy for {label}: {accuracy}')

        # # Display overall classification report
        # print('\nOverall Classification Report:\n', classification_report(y_test, predictions))

        new_data = pd.DataFrame({
            'size': [instance.size],
            'clock': [instance.clock],
            'memory_type': [instance.type.type.replace('DDR', '')],
            'price': [instance.price]
        })

        # Make predictions for the new data
        new_predictions = classifier.predict(new_data)

        list_data = []

        if new_predictions[0, 0]:
            # gaming
            list_data.append({'ram': instance.id, 'field': 3})
        if new_predictions[0, 1]:
            # graphic design
            list_data.append({'ram': instance.id, 'field': 2})
        if new_predictions[0, 2]:
            # programming
            list_data.append({'ram': instance.id, 'field': 1})
        if new_predictions[0, 3]:
            # office
            list_data.append({'ram': instance.id, 'field': 4})

        serializer = serializers.RAMFieldSerializer(data=list_data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        new_row = [
            instance.id,
            instance.name,
            instance.size,
            instance.type.type,
            instance.price,
            instance.producer.name,
            instance.clock,
            instance.timings,
            instance.sticks,
            instance.external_image if instance.external_image is not None else instance.image,
            new_predictions[0, 0],
            new_predictions[0, 1],
            new_predictions[0, 2],
            new_predictions[0, 3]
        ]

        with open(f'{BASE_DIR}/rams_1-cleaned.csv', 'a') as file:
            writer_object = writer(file)
            writer_object.writerow(new_row)
            file.close()

        # Display the predictions
        # print('Predicted classification for the new data:')
        # print('Gaming:', new_predictions[0, 0])
        # print('Graphic Design:', new_predictions[0, 1])
        # print('Programming:', new_predictions[0, 2])
        # print('Office:', new_predictions[0, 3])

@receiver(post_save, sender=models.GPU)
@disable_for_loaddata
def classification_gpu(sender, instance, created, **kwargs):
    if created:
        BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets')
        df_file = pd.read_csv(f'{BASE_DIR}/gpus_1-cleaned.csv')

        df = df_file.drop(columns=['pci-e', 'length', 'slots', '8-pin connectors', '6-pin connectors', 'hdmi', 'display port', 'dvi', 'vga', 'sync', 'tdp', 'image_url', 'producer'])

        X = df[['vram', 'cores', 'memory_clock', 'boost_clock', 'price']]

        y = df[['gaming', 'graphic design', 'programming', 'office']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the Random Forest classifier
        classifier = MultiOutputClassifier(RandomForestClassifier(random_state=42))

        # Train the model on the training data
        classifier.fit(X_train, y_train)

        # Make predictions on the test set
        predictions = classifier.predict(X_test)

        # Evaluate the accuracy for each label
        # for i, label in enumerate(y.columns):
        #     accuracy = accuracy_score(y_test[label], predictions[:, i])
        #     print(f'Accuracy for {label}: {accuracy}')

        # # Display overall classification report
        # print('\nOverall Classification Report:\n', classification_report(y_test, predictions))


        new_data = pd.DataFrame({
            'vram': [instance.vram],
            'cores': [instance.cores],
            'memory_clock': [instance.memory_clock],
            'boost_clock': [instance.boost_clock],
            'price': [instance.price]
        })

        # Make predictions for the new data
        new_predictions = classifier.predict(new_data)

        list_data = []

        if new_predictions[0, 0]:
            # gaming
            list_data.append({'gpu': instance.id, 'field': 3})
        if new_predictions[0, 1]:
            # graphic design
            list_data.append({'gpu': instance.id, 'field': 2})
        if new_predictions[0, 2]:
            # programming
            list_data.append({'gpu': instance.id, 'field': 1})
        if new_predictions[0, 3]:
            # office
            list_data.append({'gpu': instance.id, 'field': 4})

        serializer = serializers.GPUFieldSerializer(data=list_data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        new_row = [
            instance.id,
            instance.name,
            instance.pci_e,
            instance.series.series,
            instance.vram,
            instance.cores,
            instance.memory_clock,
            instance.boost_clock,
            instance.price,
            instance.producer.name,
            instance.length,
            instance.slots,
            instance.connectors_8pin,
            instance.connectors_6pin,
            instance.dvi,
            instance.vga,
            instance.sync.sync,
            instance.tdp,
            instance.external_image if instance.external_image is not None else instance.image,
            new_predictions[0, 0],
            new_predictions[0, 1],
            new_predictions[0, 2],
            new_predictions[0, 3]
        ]

        with open(f'{BASE_DIR}/gpus_1-cleaned.csv', 'a') as file:
            writer_object = writer(file)
            writer_object.writerow(new_row)
            file.close()

        # Display the predictions
        # print('Predicted classification for the new data:')
        # print('Gaming:', new_predictions[0, 0])
        # print('Graphic Design:', new_predictions[0, 1])
        # print('Programming:', new_predictions[0, 2])
        # print('Office:', new_predictions[0, 3])

@receiver(post_save, sender=models.Laptop)
@disable_for_loaddata
def classification_laptop(sender, instance, created, **kwargs):
    # Load the laptop dataset
    BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets')
    df_file = pd.read_csv(f'{BASE_DIR}/laptops-readiest.csv')
    df = df_file

    df['Number_of_Cores'] = df['Number_of_Cores'].str.split('-', n=1).str[0]

    X = df[['VRAM', 'GPU_Speed', 'GPU_Cores', 'CPU_Speed', 'Number_of_Cores', 'Memory']]

    # Target variable (y)
    y = df[['Gaming', 'Workstation', 'Home']]

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the RandomForestClassifier
    classifier = RandomForestClassifier(random_state=42)

    # Train the model on the training data
    classifier.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = classifier.predict(X_test)

    # Evaluate the model
    # accuracy = accuracy_score(y_test, predictions)
    # print(f'Accuracy: {accuracy}')

    # # Display classification report
    # print(classification_report(y_test, predictions))

    # Example input data for testing
    new_data = pd.DataFrame({
        'VRAM': [instance.vram],
        'GPU_Speed': [instance.gpu_speed],
        'GPU_Cores': [instance.gpu_cores],
        'CPU_Speed': [instance.cpu_speed],
        'Number_of_Cores': [int(instance.number_of_cores.split('-')[0])],
        'Memory': [instance.memory],
    })

    # Make predictions for the example input
    new_predictions = classifier.predict(new_data)

    list_data = []

    if new_predictions[0][0] == True:
        # gaming
        list_data.append({'laptop': instance.id, 'use': 3})
    if new_predictions[0][1] == True:
        # workstation
        list_data.append({'laptop': instance.id, 'use': 2})
    if new_predictions[0][2] == True:
        # home
        list_data.append({'laptop': instance.id, 'use': 1})

    serializer = serializers.LaptopUseSerializer(data=list_data, many=True)
    if serializer.is_valid():
        serializer.save()

    new_row = [
        instance.external_image if instance.external_image is not None else instance.image,
        instance.name,
        instance.screen_size,
        instance.cpu_type,
        instance.memory,
        instance.storage,
        instance.gpu,
        instance.vram,
        instance.gpu_speed,
        instance.gpu_cores,
        instance.resolution,
        instance.weight,
        instance.backlit_keyboard,
        instance.touchscreen,
        instance.cpu_speed,
        instance.number_of_cores,
        instance.display_type,
        instance.graphic_type,
        instance.operating_system,
        instance.webcam,
        instance.price,
        new_predictions[0, 0],
        new_predictions[0, 1],
        new_predictions[0, 2],
    ]

    with open(f'{BASE_DIR}/laptops-readiest.csv', 'a') as file:
        writer_object = writer(file)
        writer_object.writerow(new_row)
        file.close()

    # Display the predicted use
    # print('Predicted Use for the Example Input:', new_predictions)

@receiver(post_save, sender=models.Mobile)
@disable_for_loaddata
def classification_mobile(sender, instance, created, **kwargs):
    BASE_DIR = os.path.join(settings.BASE_DIR, 'datasets')
    df_file = pd.read_csv(f'{BASE_DIR}/mobiles.csv')
    df = df_file

    X = df[['Price', 'Core_count', 'CPU_speed', 'Ram', 'Battery', 'Main_camera', 'Cameras_num']]

    # Target variables (y)
    y = df[['Performance_class', 'Camera_class', 'Battery_class', 'Browsing_class']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the RandomForestClassifier
    classifier = MultiOutputClassifier(RandomForestClassifier(random_state=42))

    # Train the model on the training data
    classifier.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = classifier.predict(X_test)

    # Evaluate the model

    # accuracy = accuracy_score(y_test, predictions)
    # print(f'Overall Accuracy: {accuracy}')

    # # Display classification report for each target variable
    # for i, target_variable in enumerate(target_variables):
    #     print(f'\nClassification Report for {target_variable}:')
    #     print(classification_report(y_test[target_variable], predictions[:, i]))


    # Example input data for testing
    new_data = pd.DataFrame({
        'Price': [instance.price],
        'Core_count': [instance.core_count],
        'CPU_speed': [instance.cpu_speed],
        'Ram': [instance.ram],
        'Battery': [instance.battery],
        'Main_camera': [instance.main_camera],
        'Cameras_num': [instance.cameras_num]
    })

    # Make predictions for the example input
    new_predictions = classifier.predict(new_data)

    list_data = []

    if new_predictions[0][0] == True:
        # performance
        list_data.append({'mobile': instance.id, 'use': 1})
    if new_predictions[0][1] == True:
        # camera
        list_data.append({'mobile': instance.id, 'use': 2})
    if new_predictions[0][2] == True:
        # bettery
        list_data.append({'mobile': instance.id, 'use': 3})
    if new_predictions[0][2] == True:
        # browsing
        list_data.append({'mobile': instance.id, 'use': 4})

    serializer = serializers.MobileUseSerializer(data=list_data, many=True)
    if serializer.is_valid():
        serializer.save()

    new_row = [
        instance.name,
        instance.external_image if instance.external_image is not None else instance.image,
        instance.price,
        instance.cameras,
        instance.cpu,
        instance.core_count,
        instance.cpu_speed,
        instance.storage,
        instance.ram,
        instance.screen_size,
        instance.refresh_rate,
        instance.battery,
        instance.fast_charging,
        instance.main_camera,
        instance.front_camera,
        instance.cameras_num,
        new_predictions[0, 0],
        new_predictions[0, 1],
        new_predictions[0, 2],
        new_predictions[0, 3],
    ]

    with open(f'{BASE_DIR}/mobiles.csv', 'a') as file:
        writer_object = writer(file)
        writer_object.writerow(new_row)
        file.close()

    # Display the predicted values for each target variable
    # for i, target_variable in enumerate(target_variables):
    #     print(f'Predicted {target_variable} for the Example Input:', new_predictions[0, i])