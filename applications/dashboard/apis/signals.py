from django.db.models.signals import post_save
from django.dispatch import receiver
from .. import models
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from jinja2 import Template
import pandas as pd
from . import serializers
import os

@receiver(post_save, sender=models.CaseStyle)
def create_case_style_function_in_knowledge_engine(sender, instance, created, **kwargs):
    if created:
        script_dir = os.path.dirname(__file__)
        template_path = os.path.join(script_dir, 'jinja2_templates', 'case_style_template.j2')

        with open(template_path, 'r') as file:
            rule_template_content = file.read()

        rule_template = Template(rule_template_content)

        rendered_rule_template = rule_template.render(style=instance)
        expert_system_file_path = os.path.join('applications/pc_picker/apis/expert_system_folder/pc_parts/cases_knowledge.py')

        with open(expert_system_file_path, 'r') as file:
            content = file.read()

        if rendered_rule_template not in content:
            with open(expert_system_file_path, 'a') as file:
                file.write('\n')
                file.write(rendered_rule_template)
                file.flush()
    

@receiver(post_save, sender=models.CPU)
def classification_cpu(sender, instance, created, **kwargs):
    if created:
        df = pd.read_csv("./././datasets/cpu_fields_class.csv")

        df = df.drop(columns=['integrated_graphics', 'url', 'image_url', 'created_at', 'updated_at', 'status', 'socket', 'producer'])

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
        for i, label in enumerate(y.columns):
            accuracy = accuracy_score(y_test[label], predictions[:, i])
            print(f'Accuracy for {label}: {accuracy}')

        # Display overall classification report
        print('\nOverall Classification Report:\n', classification_report(y_test, predictions))


        new_data = pd.DataFrame({
            'price': [instance.price],
            'base_clock': [instance.base_clock],
            'turbo_clock': [instance.turbo_clock],
            'cores': [instance.cores],
            'threads': [instance.threads]
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

        # Display the predictions
        print('Predicted classification for the new data:')
        print('Gaming:', new_predictions[0, 0])
        print('Graphic Design:', new_predictions[0, 1])
        print('Programming:', new_predictions[0, 2])
        print('Office:', new_predictions[0, 3])

@receiver(post_save, sender=models.RAM)
def classification_ram(sender, instance, created, **kwargs):
    if created:
        df = pd.read_csv("./././datasets/ram_fields_class.csv")

        df = df.drop(columns=['timings', 'sticks', 'url', 'image_url', 'created_at', 'updated_at', 'status', 'producer'])

        X = df[['size', 'clock', 'type', 'price']]

        y = df[['gaming', 'graphic design', 'programming', 'office']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize the Random Forest classifier
        classifier = MultiOutputClassifier(RandomForestClassifier(random_state=42))

        # Train the model on the training data
        classifier.fit(X_train, y_train)

        # Make predictions on the test set
        predictions = classifier.predict(X_test)

        # Evaluate the accuracy for each label
        for i, label in enumerate(y.columns):
            accuracy = accuracy_score(y_test[label], predictions[:, i])
            print(f'Accuracy for {label}: {accuracy}')

        # Display overall classification report
        print('\nOverall Classification Report:\n', classification_report(y_test, predictions))

        print(instance.type.id)

        new_data = pd.DataFrame({
            'size': [instance.size],
            'clock': [instance.clock],
            'type': [instance.type.id],
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

        # Display the predictions
        print('Predicted classification for the new data:')
        print('Gaming:', new_predictions[0, 0])
        print('Graphic Design:', new_predictions[0, 1])
        print('Programming:', new_predictions[0, 2])
        print('Office:', new_predictions[0, 3])

@receiver(post_save, sender=models.GPU)
def classification_gpu(sender, instance, created, **kwargs):
    if created:
        df = pd.read_csv("./././datasets/gpu_fields_class.csv")

        df = df.drop(columns=['pci_e', 'length', 'slots', 'connectors_8pin', 'connectors_6pin', 'hdmi', 'display_port', 'dvi', 'vga', 'sync', 'tdp', 'image_url', 'created_at', 'updated_at', 'status', 'producer'])

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
        for i, label in enumerate(y.columns):
            accuracy = accuracy_score(y_test[label], predictions[:, i])
            print(f'Accuracy for {label}: {accuracy}')

        # Display overall classification report
        print('\nOverall Classification Report:\n', classification_report(y_test, predictions))


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

        # Display the predictions
        print('Predicted classification for the new data:')
        print('Gaming:', new_predictions[0, 0])
        print('Graphic Design:', new_predictions[0, 1])
        print('Programming:', new_predictions[0, 2])
        print('Office:', new_predictions[0, 3])