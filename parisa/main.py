#Arthur Correa  
from _spy.vitollino.main import Cena, Elemento,Texto

CACADOR="http://www.culturamix.com/wp-content/gallery/cacador-2/images.png"
def Historia():
    cenaFloresta=Cena(img="http://homeroreis.com/wp-content/uploads/2015/10/floresta.jpg")
    cacador = Elemento(img= CACADOR,
              tit ="Caçador",
              style = dict(left=150, top=60, width=60, height=200))
    cacador.entra(cenaFloresta)
    cenaFloresta.vai()
Historia()