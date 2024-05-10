import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

# Load the pre-trained ResNet50 model for initial classification
inception_model = keras.models.load_model('image_classification_Inceptionmodel.keras')
print("Plant Image CLassifier model Loaded","image_classification_Inceptionmodel.keras")
resnet_model = ResNet50()
resnet_model.load_weights('resnet50_weights_tf_dim_ordering_tf_kernels.h5')
print("Object Detect model Loaded","resnet50_weights_tf_dim_ordering_tf_kernels.h5")

# Load the pre-trained Inception V3 model for live processing
  # Replace with the path to your Inception V3 model file

# Define the labels for your classes
class_labels = ['Aloevera', 'Curry Leaves', 'Mint', 'Neem', 'Papaya', 'Pattharchatta', 'Tulsi']  # Replace with your class labels

# Function to classify an image
def classify_image(image_path,model):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict the class probabilities
    predictions = model.predict(img_array)
    
    # Decode and print the top-3 predicted classes
    decoded_predictions = decode_predictions(predictions, top=5)[0]
    new_prediction_labels=[]
    for i in decoded_predictions:
        if is_plant(i[1])==True:
            new_value = 'Plant'
            i=i+ (new_value,)
        if is_plant(i[1])==False:
            new_value = 'Not-Plant'
            i=i+ (new_value,)
        new_prediction_labels.append(i)
    print(new_prediction_labels)
    count_of_plant = sum(1 for (_, _, _, label) in new_prediction_labels if label == 'Plant')
    if count_of_plant>0:
        return {"status":"success","message":"Send to Inception V3"}
    else:
        return {"status":"error","message":"Invalid Image. Please Upload Plant Image"}
    

    
def is_plant(image_net_class):
    # List of ImageNet classes related to plants
    plant_classes = ['zucchini', 'cucumber', 'pot','vase','birdhouse', 'picket_fence', 'tench', 'goldfish', 'great_white_shark', 'tiger_shark', 'hammerhead', 'electric_ray', 'stingray', 'cock', 'hen', 'ostrich', 'brambling', 'goldfinch', 'house_finch', 'junco', 'indigo_bunting', 'robin', 'bulbul', 'jay', 'magpie', 'chickadee', 'water_ouzel', 'kite', 'bald_eagle', 'vulture', 'great_grey_owl', 'European_fire_salamander', 'common_newt', 'eft', 'spotted_salamander', 'axolotl', 'bullfrog', 'tree_frog', 'tailed_frog', 'loggerhead', 'leatherback_turtle', 'mud_turtle', 'terrapin', 'box_turtle', 'banded_gecko', 'common_iguana', 'American_chameleon', 'whiptail', 'agama', 'frilled_lizard', 'alligator_lizard', 'Gila_monster', 'green_lizard', 'African_chameleon', 'Komodo_dragon', 'African_crocodile', 'American_alligator', 'triceratops', 'thunder_snake', 'ringneck_snake', 'hognose_snake', 'green_snake', 'king_snake', 'garter_snake', 'water_snake']

    # Check if the given ImageNet class is related to plants
    return any(plant_class in image_net_class.lower() for plant_class in plant_classes)


def classify_frame(frame, model):
    img_array = cv2.resize(frame, (224, 224))
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict the class probabilities
    predictions = model.predict(img_array)

    # Decode and print the top-3 predicted classes
    decoded_predictions = decode_predictions(predictions, top=5)[0]
    new_prediction_labels = []
    for i in decoded_predictions:
        if is_plant(i[1]):
            new_value = 'Plant'
        else:
            new_value = 'Not-Plant'
        i = i + (new_value,)
        new_prediction_labels.append(i)
    print(new_prediction_labels)

    count_of_plant = sum(1 for (_, _, _, label) in new_prediction_labels if label == 'Plant')
    if count_of_plant > 0:
        return {"status": "success", "message": "Send to Inception V3"}
    else:
        return {"status": "error", "message": "Invalid Image. Please Upload Plant Image"}

# Open a connection to the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

# Set camera properties (adjust focus by changing the value of 10, you may need to experiment)
cap.set(10, 0.5)  # 0.5 is an example value, adjust as needed

# Define the input shape expected by the Inception V3 model
input_shape = (299, 299)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Classify the frame using the ResNet50 model
    classification_result = classify_frame(frame, resnet_model)

    if classification_result["status"] == "success":
        # Proceed with live processing using Inception V3

        # Resize the frame to match the expected input shape of the Inception V3 model
        frame = cv2.resize(frame, input_shape)

        # Perform any necessary pre-processing on the frame
        # (normalization, etc. depending on your Inception V3 model's requirements)

        # Make predictions using the Inception V3 model
        input_data = np.expand_dims(frame, axis=0)  # Add batch dimension
        predictions = inception_model.predict(input_data)
        predicted_class = np.argmax(predictions)

        # Get the corresponding class label
        predicted_label = class_labels[predicted_class]

        # Draw a green rectangle around the focused area
        cv2.rectangle(frame, (50, 50), (250, 250), (0, 255, 0), 2)

        # Draw the prediction inside the rectangle
        cv2.putText(frame, predicted_label, (60, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        # Draw a square box with no label when status is error
        frame = cv2.resize(frame, input_shape)
        cv2.rectangle(frame, (50, 50), (250, 250), (0, 0, 255), 2)
    # Display the frame
    cv2.imshow('Live Image Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
