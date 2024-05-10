import cv2
import numpy as np
import tensorflow as tf


def image_clasiifier(image_path,labels,loaded_model):
    print("Model Prediction Allowed")
    if loaded_model==None:
        model=tf.keras.models.load_model("engine/image_classification_Inceptionmodel.keras")
    else:
        model=loaded_model
    # Load and preprocess the image you want to predict
    

    # Open an image

    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(299, 299))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # Make a prediction
    predictions = model.predict(img_array)



    # Calculate the confidence scores as percentages
    confidence_scores = predictions * 100

    # Find the class label with the highest confidence
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = labels[predicted_class_index]

    # Display the predicted class label and confidence scores
    # print("Predicted Class Label:", predicted_class_label)
    # print("Confidence Scores:")
    a=[]
    for class_index, confidence in enumerate(confidence_scores[0]):
        
        class_label = labels[class_index]
        a.append({str(class_label):confidence})

    sorted_data = sorted(a, key=lambda x: list(x.values())[0], reverse=True)
    for item in sorted_data:
        for key, value in item.items():
            item[key] = str(value)
    return {'data':sorted_data}


    