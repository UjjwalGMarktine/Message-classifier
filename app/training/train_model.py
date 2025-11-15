import fasttext
import os
from django.conf import settings



def train_model(TEMP_TRAIN_FILE):
    model = fasttext.train_supervised(
            input=TEMP_TRAIN_FILE,
            epoch=25,
            lr=1.0,
            wordNgrams=2,
            verbose=2,
            minCount=1,
            loss="softmax"
        )

    model.save_model(settings.MODEL_PATH)
    print("Model trained and saved at:", settings.MODEL_PATH)
    return


def train_model_view(file_bytes=None):
    TEMP_TRAIN_FILE = os.path.join(settings.BASE_DIR, "training_data.txt")
    print("Training started")
    try:
        text = file_bytes.decode("utf-8")
    except Exception as e:
        print("Error decoding file:", str(e))
        return False

    try:
        with open(TEMP_TRAIN_FILE, "w", encoding="utf-8") as f:
            f.write(text)
        print("training_data.txt saved")
    except Exception as e:
        print("Failed to write training file:", str(e))
        return False

    try:
        train_model(TEMP_TRAIN_FILE)
        # model = fasttext.train_supervised(
        #     input=TEMP_TRAIN_FILE,
        #     epoch=25,
        #     lr=1.0,
        #     wordNgrams=2,
        #     verbose=2,
        #     minCount=1,
        #     loss="softmax"
        # )

        # model.save_model(settings.MODEL_PATH)
        # print("Model trained and saved at:", settings.MODEL_PATH)

        if os.path.exists(TEMP_TRAIN_FILE):
            os.remove(TEMP_TRAIN_FILE)
            print("Temporary file deleted successfully:", TEMP_TRAIN_FILE)

        return True

    except Exception as e:
        print("Training failed:", str(e))
        return False
