import qrcode
from PIL import Image

data = input("Enter anything to generate QR: ")

qr = qrcode.QRCode(version=2, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill="black", back_color="white")

image.save("qr_code.png")
image.open("qr_code.png")