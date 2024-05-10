from data.db_model import *
from functools import wraps
import pandas as pd
from api.data import language_dict
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file, Response
from engine.similarity_text import similarity_word
from engine.geo import *
from engine.objectdetect import *
import os
from engine.qrmaker import * 
import tensorflow as tf
from engine.inception_testModel import *
from engine.train_model.inceptionV3_modeltrain_ifnewadded import *
import cv2
import numpy as np
import tensorflow as tf
import requests
#Image
from PIL import Image
import requests
from io import BytesIO



# http://127.0.0.1:5000/api/plants?language=english&plant_name=neem_leaf
# http://localhost:5000/api/plants?language=english&plant_name=neem_leaf


plant= ['Aloevera',  'Curry Leaves' , 'Mint', 'Neem', 'Papaya','Pattharchatta' , 'Tulsi']

APP_PATH = os.getcwd()

app = Flask(__name__)

# Initialize a variable to store the loaded model
loaded_model = None

def load_model():
    # Load your machine learning model here
    global loaded_model
    global object_detect_model
   
    loaded_model = tf.keras.models.load_model("engine/image_classification_Inceptionmodel.keras")
    print("Plant Image CLassifier model Loaded","image_classification_Inceptionmodel.keras")
    object_detect_model = ResNet50()
    object_detect_model.load_weights('engine/resnet50_weights_tf_dim_ordering_tf_kernels.h5')
    print("Object Detect model Loaded","resnet50_weights_tf_dim_ordering_tf_kernels.h5")
# Load the model when the Flask app starts
load_model()


establish_db_connection()


# Load the pre-trained Keras model
model =loaded_model

# Define the labels for your classes
class_labels = plant

@app.route('/',methods=['GET'])
def index():
	language = request.args.get('language')
	languages=[]
	plant_info=[]
	if language==None:
		language="english"
	cursor = db.cursor()
	table_name = database[language]
	query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
	cursor.execute(query1)
	column_names = [column[0] for column in cursor.fetchall()]
	query = f"SELECT * FROM {table_name}"
	cursor.execute(query)
	results = cursor.fetchall()
	main=[]
	for i in results:
		result_dict = {key: value for key, value in zip(column_names, list(i))}
		result_dict['compounds']= [item.strip() for item in result_dict['compounds'].split(',')]
		result_dict['coordinate']=longlatretriever([item.strip() for item in result_dict['coordinate'].split(',')])
		main.append(result_dict) 
	filtered_languages = [lang for lang in language_dict if lang['language_id'] == language]
	for i in language_dict:
		languages.append({"id":i['language_id'],"name":i['language_name']})
	content=filtered_languages[0]
	return render_template('index.html',data=plant,language=languages,content=content,plant_info_all=main)



@app.route('/profile',methods=['GET'])
def profileind():
	language = request.args.get('language')
	plant_name = request.args.get('plant_name')
	plant_info=[]
	if language==None:
		language="english"
	cursor = db.cursor()
	table_name = database[language]
	query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
	cursor.execute(query1)
	column_names = [column[0] for column in cursor.fetchall()]
	query = f"SELECT * FROM {table_name} WHERE plant_username = '{plant_name}' "
	print(query)
	cursor.execute(query)
	result = cursor.fetchall()
	print("result",result)
	main=[]
	for i in result:
		result_dict = {key: value for key, value in zip(column_names, list(i))}
		result_dict['compounds']= [item.strip() for item in result_dict['compounds'].split(',')]
		result_dict['coordinate']=longlatretriever([item.strip() for item in result_dict['coordinate'].split(',')])
		result_dict['medicines']= [item.strip() for item in result_dict['medicines'].split(',')]
		main.append(result_dict) 
	filtered_languages = [lang for lang in language_dict if lang['language_id'] == language]
	print(filtered_languages)
	main=main[0]
	languages=[]
	for i in language_dict:
		print(i)
		languages.append({"id":i['language_id'],"name":i['language_name']})
	print("languages",languages)
	content=filtered_languages[0]
	return render_template('profileindividual.html',language=languages,content=content,plant_info=main)


@app.route('/api/plants', methods=['GET'])
def get_plant_info():
    language = request.args.get('language')
    plant_name = request.args.get('plant_name')
    cursor = db.cursor()
    table_name = database[language]
    # Query the information schema to get column names
    query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
    cursor.execute(query1)
    # Fetch all the column names
    column_names = [column[0] for column in cursor.fetchall()]
    query = f"SELECT * FROM {table_name} WHERE plant_username = '{plant_name}' "
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    main=[]
    for i in result:
    	result_dict = {key: value for key, value in zip(column_names, list(i))}
    	result_dict['compounds']= [item.strip() for item in result_dict['compounds'].split(',')]
    	result_dict['coordinate']= [item.strip() for item in result_dict['coordinate'].split(',')]
    	main.append(result_dict) 
    print(main)
    if len(main)>0:
    	 return jsonify({'identifier':'profile_one','data':main[0]})
    else:
    	return jsonify({"message":"Data don't found"})


@app.route('/api/plants_all', methods=['GET'])
def get_plantall_info():
    language = request.args.get('language')
    cursor = db.cursor()
    table_name = database[language]
    # Query the information schema to get column names
    query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
    cursor.execute(query1)
    # Fetch all the column names
    column_names = [column[0] for column in cursor.fetchall()]

    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()


    main=[]
    for i in results:
    	print(list(i))
    	result_dict = {key: value for key, value in zip(column_names, list(i))}
    	result_dict['compounds']= [item.strip() for item in result_dict['compounds'].split(',')]
    	result_dict['coordinate']= [item.strip() for item in result_dict['coordinate'].split(',')]
    	main.append(result_dict) 
    return jsonify({'identifier':'profile_all','data':main})
    
    


@app.route('/translator', methods=['POST'])
def maintranslator():
	data = request.get_json()
	# a=translator("Gujrati",data['search'])
	
	response = {"message": "Data received successfully","data":data}
	result=similarity_word(word=response['data']['search'],plant=plant) 
	response['plant_name']=result
	print(response)
	return jsonify(response)



@app.route('/addnewimage', methods=['GET'])
def addnewimage():
	update_and_train_model(loaded_model, '/engine/train_model/new Images', 'new.keras', num_epochs=10)
	return jsonify({'response':'Yes'})


@app.route('/update_content', methods=['POST'])
def languageconvertors():
	data = request.get_json()

	if data:
	    response = {"message": "Data received successfully","data":data}
	    main=response['data']
	    for i in language_dict:
	    	
	    	if i['language_id']== main['language']:
	    		response['data']=i

	    # response['plant_info']=plant_info
	    print("res", response)
	    return jsonify(response)
	else:
		return jsonify({'error': 'Invalid data received'})



@app.route('/upload', methods=['POST'])
def upload_file():
	print('Akash')
	global loaded_model
	# Check if the model is loaded
	if loaded_model is None:
		load_model()  # Load the model if it's not loaded
	try:
		uploaded_file = request.files['file']
		if uploaded_file:
		# Save the uploaded file to a specific folder
			save_path = os.path.join('uploads', uploaded_file.filename)
			uploaded_file.save(save_path)
			object_detect=classify_image(save_path,object_detect_model)
			print(object_detect)
			if object_detect['status']=='error':
				return jsonify(object_detect)
			else:
				main=image_clasiifier(save_path,plant,loaded_model)
				print(main)
				return jsonify({'message': 'Prediction successfully','data':main['data']})
		else:
			return jsonify({'message': 'No file selected'})
	except Exception as e:
		return jsonify({'message': 'Error occurred: ' + str(e)})


@app.route('/predict', methods=['GET'])
def predictor():
	try:
		image_url = request.args.get('url')
		response = requests.get(image_url)
		if response.status_code == 200:
			image = Image.open(BytesIO(response.content))
			save_directory = 'uploads/'
			image_filename = 'predict.jpg'
			image.save(save_directory + image_filename)
			print(f'Image saved as {save_directory + image_filename}')
			save_path=save_directory+image_filename
			print("A")
			main=image_clasiifier(save_path,plant,loaded_model)
			print(main)
			return jsonify({'message': 'Prediction successfully','data':main['data']})
		else:
			print(f'Failed to download the image. Status code: {response.status_code}')

	except Exception as e:
		return jsonify({'message': 'Error occurred: ' + str(e)})




@app.route('/qrcode', methods=['POST'])
def qrcode():
	try:
		data = request.get_json()
		url=data.get('url')
		if url:
			print(url)
			main=qrmakerMain(url,APP_PATH.replace('\\', '/'))
			print(main)
			return jsonify({'message': 'QR Downloaded successfully','path':main['path']})
			# return send_file(main['path'], as_attachment=True)
		else:
			return jsonify({'message': 'No QR Found'})
	except Exception as e:
		return jsonify({'message': 'Error occurred: ' + str(e)})

@app.route('/download_image')
def download_image():
    # Send the image file for download
    image_path=APP_PATH+"/qrcode/qrcode.png"
    return send_file(image_path, as_attachment=True)

if __name__ == '__main__':
    app.run()




