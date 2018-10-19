#Raphael
from _spy.vitollino.main import Cena, Elemento, Texto

#Glub Glub


NEMO ="http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg"

def Historia():
    mar = Cena(img="https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg")
    nemo = Elemento(img=NEMO,tit="NEMO",style=dict(left = 180, top = 40, height = 40, width = 170))
    nemo.entra(mar)
    mar.vai ()
Historia()