import qrcode

# création d'un QRcode par défaut
img = qrcode.make("https://www.instagram.com/kodebar.pro/")
img.save('qrcode_Kodebar.png')

""" Personnaliser son Qrcode"""
qr = qrcode.QRCode(
    version=3,
    box_size =3,
    border=5
)

qr.add_data('https://www.instagram.com/kodebar.pro/')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save('qrcode_Kodebar_V2.png')