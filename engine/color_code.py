
import webcolors

def color_hexcode(color_name):
	color_name=color_name.to_lower()
	try:
	    # Get the RGB value for the color name
	    color_rgb = webcolors.name_to_rgb(color_name)
	    # Convert the RGB value to a hex color code
	    color_hex = "#{:02x}{:02x}{:02x}".format(*color_rgb)
	    return jsonify({'color_name':color_name,'hex_code':color_hex})
	except ValueError:
	    return jsonify({'color_name':color_name,'hex_code':"not found"})