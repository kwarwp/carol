#Jerry
from _spy.vitollino.main import Cena, Elemento, Texto

CAMELO ="https://cdn.pixabay.com/photo/2017/01/17/18/45/camel-1987672_960_720.png"

def Historia():
    DESERTO = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/0/0c/Deserto_no_Cerrado.jpg")
    CAMELO = Elemento(img=CAMELO, tit="CAMELO", style=dict(left= 150, top=60, width=60, height=200))
    CAMELO.entra(DESERTO)
    DESERTO.vai()
Historia()    












































