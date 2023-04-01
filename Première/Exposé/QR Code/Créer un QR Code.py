import qrcode
import image
import qrcode.image.svg
from qrcode.image.pil import PilImage

ver = int(input("Taille du QR code (nombre entre 1 et 40):"))
box = int(input("Nombre de pixel de chaque boîte du QR code:"))
border_size = int(input("Taille de la bordure du QR code (minimum 4):"))
color = input("Couleur du QR Code:")
data = input("Informations contenuent dans le QR code:")
file = data = input("Nom de l'image du QR code (avec l'extension):")

#Caractéristique du QR code 
qr = qrcode.QRCode(
    #Complexité
    version = ver,
    #Taille de la bordure
    box_size = box,
    #Taile du QR code
    border = border_size,
)

#Données contenu dans le QR code
qr.add_data(data)
#Génération de l'image du QR code
qr.make(fit = True)
#Couleur du QR code
img = qr.make_image(fill_color=color, back_color="white")
#Sauvegarde de l'image
img.save(file)
