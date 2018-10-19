#Raphael
from _spy.vitollino.main import Cena, Elemento, Texto 

oceano = "https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg"
nemo = "http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg"
#Glub Glub
def historia():
   cenaoceano = Cena(img="https://mardehistorias.files.wordpress.com/2010/11/oceano.jpg")              
   nemo = Elemento(img="http://www.araguaiaaquarios.com.br/loja/modules/possequence/images/image_1.jpg",
                  tit="nemo",
                  style = dict (top = 180, left = 40, height = 40, width = 170))
   nemo.entra(cenaoceano)
   txtNemo = Texto(cenaoceano,
                  "Glub Glub")
   nemo.vai = txtNemo.vai
   cenaoceano.vai()
Historia()

from _spy.vitollino.main import Cena, Elemento, Texto

ZUMBI ="http://www.deezer-blog.com/assets/http://www.deezer-blog.com/assets/sites/8/2015/10/zumbiblog.pngsites/8/2015/10/zumbiblog.png"

def Historia():
    ILHA = Cena(img ="https://ogimg.infoglobo.com.br/in/21993934-fe0-499/FT1086A/652/x06_10_2017.-Jornal-O-Globo.-Ilha-Grande-4.jpg.pagespeed.ic.NPxcsQST9i.jpg")
    zumbi9= Elemento(img=ZUMBI,tit="ZUMBI",style=dict(left=150, top=60, width=60,height=200))
    ILHA.vai ()
Historia()