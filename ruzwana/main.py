#Cibele
from _spy.vitollino.main import Cena, Elemento, Texto 

Chica=
def Historia():
        cenaTeatro = Cena(img ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdPLYgHZx_3F32cbuvh1F1JCtI7wCETneHux09yVAqsmfEOX5C")
        chica = Elemento(img =Chica,
                tit ="Chica",
                style = dict(left=150, top=60, width=60, height=200))
        chica.entra(cenaTeatro)
        cenaTeatro.vai()
Historia()