import tensorflow as tf

class ImageClassifier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def classify_image(self, image_path):
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        image_array = tf.expand_dims(image_array, 0)  # Create a batch

        predictions = self.model.predict(image_array)
        predicted_class = tf.keras.applications.imagenet_utils.decode_predictions(predictions, top=1)[0][0]

        return predicted_class

    def close(self):
        tf.keras.backend.clear_session()

# Example usage:
if __name__ == "__main__":
    classifier = ImageClassifier("path/to/your/model.h5")
    result = classifier.classify_image("path/to/your/image.jpg")
    print("Prediction:", result)
    classifier.close()