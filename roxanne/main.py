#davy
from _spy.vitollino.main import Cena,Elemento,Texto

COLOSOS ='https://upload.wikimedia.org/wikipedia/az/b/bb/Colossus.png'
def Historia():
    cenaParque = Cena(img = "https://cdn.civitatis.com/argentina/buenos-aires/guia/parque-tres-febrero-grid-m.jpg")
    colosos = Elemento(img=COLOSOS,
              tit ="Colosos",
              style = dict(left=150, top=60, width=60, height=200))
    colosos.entra(cenaParque)   
    cenaParque.vai()
Historia()