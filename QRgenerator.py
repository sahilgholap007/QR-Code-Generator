
import pyqrcode
import png
from pyqrcode import QRCode
  
  

s = "https://github.com/sahilgholap007"
  

url = pyqrcode.create(s)
  

url.svg("myqr.svg", scale = 8)
  

url.png('myqr.png', scale = 6)