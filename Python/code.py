import pyqrcode
import png
from pyqrcode import QRCode
link=input("ENTER LINK :")
download=pyqrcode.create(link)
download.png("(//name of the qr code u want).png",scale=4)
print("Downloaded..")
