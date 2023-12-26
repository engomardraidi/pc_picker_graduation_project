from django.db.models.signals import post_save
from django.dispatch import receiver
from .. import models
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from . import serializers
    

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
        print(instance.id)
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