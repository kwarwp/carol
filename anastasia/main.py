#matheus
from _spy.vitollino.main import Cena, Elemento, Texto

SAPO ="http://clipart.coolclips.com/480/vectors/tf05031/CoolClips_anim0220.png"

def Historia():
    CASTELO = Cena(img = "http://obviousmag.org/grifo/assets_c/2016/05/castelo-thumb-800x400-149789.jpg")
    sapo = Elemento(img=SAPO, tit="Sapo", style=dict(left=150, top=60, width=60, height=200))
    sapo.entra(CASTELO)
    txtsapo= Texto(CASTELO, "Hello")
    sapo.vai=txtsapo.vai
    CASTELO.vai()
Historia()
    