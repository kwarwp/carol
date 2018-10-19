#Raphael
from _spy.vitollino.main import Cena, Elemento, Texto 

#Glub Glub

mar = "https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg"
nemo = "http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg"

def Historia():
    cenamar = Cena(img="https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg")
    nemo= Elemento(img="http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg",
                   tit="nemo",
                   style=dict(left=180, left = 40, height = 40, width = 170))
    nemo.entra(mar)
    mar.vai ()
Historia()