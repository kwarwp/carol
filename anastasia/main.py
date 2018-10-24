#matheus
from _spy.vitollino.main import Cena, Elemento, Texto

SAPO ="https://www.imagenspng.com.br/wp-content/uploads/2015/04/galinha-pintadinha-sapo-1.png"

def Historia():
    CASTELO = Cena(img = "http://obviousmag.org/grifo/assets_c/2016/05/castelo-thumb-800x400-149789.jpg")
    sapo = Elemento(img=SAPO, tit="Sapo", style=dict(left=150, top=60, width=60, height=200))
    sapo.entra(CASTELO)
    txtsapo= Texto(CASTELO, "Hello")
    sapo.vai=txtsapo.vai
    CASTELO.vai()
Historia()
    