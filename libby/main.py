#laura
from _spy.vitollino.main import Cena,Elemento,Texto

MALVADO ="http://56.media.tumblr.com/b29d0f586c54e40d71c8566efba0cecd/tumblr_o31t6fLBbo1tx4472o1_1280.png" 
def Historia():
    cenaCastelo = Cena(img= "http://i67.tinypic.com/f24z7l.jpg")
    malvado= Elemento(imgmalvado,
           tit="malvado",
           style = dict(left=150, top=60,width=60, height=200))
    cenaCastelo.vai()
           
Historia()

