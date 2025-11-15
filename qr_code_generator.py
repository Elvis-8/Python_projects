import qrcode
import webbrowser
import os

url = input('Enter a text or URL: ').strip()
filename = input('Enter the filename (include .png extension): ')
qr_code = qrcode.QRCode(border=4, box_size=10)
qr_code.add_data(url)
image = qr_code.make_image()
image.save(filename)
print(f'QR code saved as {filename}')

full_path = os.path.abspath(filename)
webbrowser.open(f"file://{full_path}")
