import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np

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


