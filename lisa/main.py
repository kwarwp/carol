#Carol 
from _spy.vitollino.main import Cena, Elemento, Texto

GOKU ="http://www.stickpng.com/assets/images/584e83616a5ae41a83ddee39.png"
def Historia():
    cenaTeatro = Cena(img ="http://1.bp.blogspot.com/-aGwacYjRKw8/T-St9kEVvMI/AAAAAAAAAvs/ximTg6O8XUA/s1600/ESCENARIOS29+%282%.jpg")
    goku = Elemento(img= GOKU,
           tit ="Goku",
           style = dict(left=150, top=60,width=200, height=50))
    goku.entra(cenaTeatro)
    txtgoku = Texto (cenaTeatro, "Hello")
    goku.vai = txtgoku.vai
    cenaTeatro.vai()
Historia()
