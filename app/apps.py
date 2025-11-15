from django.apps import AppConfig
import threading, sys
from django.conf import settings

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


    print("Inside app2 AppConfig app() outer")

    def ready(self):
        print("Inside app2 AppConfig ready()")

        if "runserver" in sys.argv:
            print("Starting training thread...")
            threading.Thread(
                target=self.run_training,
                daemon=True
            ).start()

    def run_training(self):
        print("Training started from AppConfig...")
        from app.training.train_model import train_model
        path = "/home/marktine/practice/Comment_classifier/comment_classification_project/dummy_training_data.txt"
        train_model(settings.DATA_SET)
