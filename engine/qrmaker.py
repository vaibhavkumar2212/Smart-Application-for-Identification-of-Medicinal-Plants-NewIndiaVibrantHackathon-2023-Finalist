import qrcode
from PIL import Image, ImageDraw, ImageFont
import os


def qrmakerMain(route,APP_PATH):
	# Create an instance of the QRCode class
	qr = qrcode.QRCode(
	    version=1,
	    error_correction=qrcode.constants.ERROR_CORRECT_L,
	    box_size=10,
	    border=4,
	)

	# Add data to the QR code
	qr.add_data(route)
	qr.make(fit=True)

	# Create an image from the QR Code instance
	img = qr.make_image(fill_color="black", back_color="white")
	path="qrcode/qrcode.png"
	# Save the image to a file (you can also display it or do something else with it)
	img.save(path)
	return {"message":"Ok", "path":path}