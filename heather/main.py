#Heather
from _spy.vitollino.main import Cena, Elemento, Texto

PRANCHA ="https://s3.amazonaws.com/images.shaperbuddy.com/43/surfboards/27100185252f23.png"

def Historia():
    PRAIA = Cena(img = "https://static1.squarespace.com/static/595257a1e110eb8ad5afc365/59710c1137c5815bfac4bc6b/59710cd4cd39c303e0182262/1500581128697/Praia97.jpg")
    prancha = Elemento(img=PRANCHA, tit="Prancha", style=dict(left=150, top=60, width=60, height=200))
    PRAIA.vai()
Historia()