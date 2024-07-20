import pyqrcode
import png
from pyqrcode import QRCode

s = "https://www.meetup.com/gittogether-luanda/"
url = pyqrcode.create(s)
url.svg("GitTogetherLuanda.svg", scale = 8)
url.png('GitTogetherLuanda.png', scale = 6)