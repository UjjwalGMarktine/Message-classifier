from django.test import TestCase

# Create your tests here.
import fasttext

# Test load
test_model_path = ("../app/models/abuse_classifier.bin")
model = fasttext.load_model(test_model_path)
labels, probs = model.predict("i love you so much", k=1)
print("labels:", labels)
print("probs:", probs)
print("confidence:", float(probs[0]))