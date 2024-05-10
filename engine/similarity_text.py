import nltk
from nltk.metrics import edit_distance




def similarity_word(word,plant):
	data=[]
	for i in plant:
		
		word1 = word.replace(" ", "").lower()
		i=i.replace(" ", "").lower()
		# Calculate Levenshtein distance
		distance = edit_distance(word1, i)

		# Calculate similarity as a ratio of similarity to the length of the longer word
		similarity = 1 - (distance / max(len(word1), len(i)))
		data.append({'plant':i,'similarity':similarity*100})
	sorted_data = sorted(data, key=lambda x: x['similarity'], reverse=True)
	# Set the threshold
	threshold = 50

	# Filter the data based on the threshold
	filtered_data = [item for item in data if item['similarity'] > threshold]

	print(filtered_data)
	if len(filtered_data)>0:
		return {'message':"Data successful","data":filtered_data[0]}
	if len (filtered_data)==0:
		return {'error':"No such plant found","data":0}
	else:
		return {'message':"Data not found","data":filtered_data}


plant= ['Aloevera',  'Curry Leaves' , 'Mint', 'Neem', 'Papaya','Pattharchatta' , 'Tulsi']

# main=similarity_word("Neema", plant)
# print(main)