# eidimar
from _spy.vitollino.main import Cena, Elemento, Texto

ANDORINHAS = "https://meiosdigitais2014.files.wordpress.com/2014/05/passaros.png"

def Historia():
    PORDOSOL = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/c/ce/P%C3%B4r_do_Sol.jpg")
    andorinhas = Elemento(img=ANDORINHAS, tit="Andorinhas", style=dict(left=150, top=60, width=60, height=200))
    PORDOSOL.vai()
Historia()
