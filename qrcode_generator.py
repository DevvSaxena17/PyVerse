# qrcode_generator.py
import qrcode

data = "https://hacktoberfest.com"
img = qrcode.make(data)
img.save("hacktoberfest_qr.png")
print("QR Code saved as hacktoberfest_qr.png")
