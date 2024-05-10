def longlatretriever(state_names):
		
	state_coordinates = {
	    "Andhra Pradesh": (15.9129, 79.7400),
	    "Arunachal Pradesh": (28.2180, 94.7278),
	    "Assam": (26.2006, 92.9376),
	    "Bihar": (25.0961, 85.3131),
	    "Chhattisgarh": (21.2787, 81.8661),
	    "Goa": (15.2993, 74.1240),
	    "Gujarat": (22.2587, 71.1924),
	    "Haryana": (29.0588, 76.0856),
	    "Himachal Pradesh": (31.1048, 77.1734),
	    "Jharkhand": (23.6102, 85.2799),
	    "Karnataka": (15.3173, 75.7139),
	    "Kerala": (10.8505, 76.2711),
	    "Madhya Pradesh": (22.9734, 78.6569),
	    "Maharashtra": (19.7515, 75.7139),
	    "Manipur": (24.6637, 93.9063),
	    "Meghalaya": (25.4670, 91.3662),
	    "Mizoram": (23.1645, 92.9376),
	    "Nagaland": (26.1584, 94.5624),
	    "Odisha": (20.9517, 85.0985),
	    "Punjab": (31.1471, 75.3412),
	    "Rajasthan": (27.0238, 74.2179),
	    "Sikkim": (27.5330, 88.5122),
	    "Tamil Nadu": (11.1271, 78.6569),
	    "Telangana": (18.1124, 79.0193),
	    "Tripura": (23.9408, 91.9882),
	    "Uttar Pradesh": (26.8467, 80.9462),
	    "Uttarakhand": (30.0668, 79.0193),
	    "West Bengal": (22.9868, 87.8550),
	    "Himalayas": (28.6139, 77.2090),
	    "Orissa": (20.2961, 85.8245),
	    "Mumbai": (19.0760, 72.8777),
	    "Hyderabad": (17.3850, 78.4867),
	    "Kolkata": (22.5726, 88.3639),
	    "Kashmir": (34.0836, 74.7974),
	    # Major cities
	    "Delhi": (28.6139, 77.2090),
	    "Bangalore": (12.9716, 77.5946),
	    "Chennai": (13.0827, 80.2707),
	    "Ahmedabad": (23.0225, 72.5714),
	    "Pune": (18.5204, 73.8567),
	    "Jaipur": (26.9124, 75.7873),
	    "Lucknow": (26.8467, 80.9462),
	    "Kanpur": (26.4499, 80.3319),
	    "Nagpur": (21.1458, 79.0882),
	    "Indore": (22.7196, 75.8577),
	    "Thane": (19.2183, 72.9781),
	    "Bhopal": (23.2599, 77.4126),
	    "Visakhapatnam": (17.6868, 83.2185),
	    "Surat": (21.1702, 72.8311),
	    "Vadodara": (22.3072, 73.1812),
	    "Coimbatore": (11.0168, 76.9558),
	    "Ludhiana": (30.9010, 75.8573),
	    "Madurai": (9.9252, 78.1198),
	    "Agra": (27.1767, 78.0081),
	    "Nashik": (20.5937, 78.9629),
	    "Kochi": (9.9312, 76.2673),
	    "Greater Noida": (28.4744, 77.5036)
	}
	finalData=[]


	for state_name in state_names:
		    coordinates = state_coordinates.get(state_name)
		    if coordinates is not None:
		    	finalData.append({"name":state_name, "lat":coordinates[0], "lon":coordinates[1]})
		    else:
		    	print(f"{state_name} is not found in the dictionary.")
		    	

	return finalData
