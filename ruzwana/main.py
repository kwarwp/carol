#Raphael
from _spy.vitollino.main import Cena, Elemento, Texto

#Glub Glub

NEMO ="http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg"

def Historia():
    mar = Cena(img="https://media-cdn.tripadvisor.com/media/photo-s/0f/03/76/ef/fundo-do-mar.jpg")
    nemo = Elemento(img=NEMO,tit="NEMO",style=dict(left = 100, top = 120, height = 80, width = 130))
    nemo.entra(mar)
    mar.vai ()
Historia()