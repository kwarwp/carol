# gabriela
from _spy.vitollino.main import Cena,Elemento,Texto

CINDERELA="http://imagensemoldes.com.br/wp-content/uploads/2018/04/Imagem-de-Personagens-Princesa-Cinderela-10-PNG-244x300.png"
def Historia():
    cenaCastelo = Cena(img ="https://www.vaipradisney.com/blog/wp-content/uploads/2017/05/QUARTO-CASTELO-CINDERELA-13.jpg")
    cinderela = Elemento(img=CINDERELA,
                tit ="cinderela"
                style = dict(left=150, top=60, width=60, heighy=200))
    cinderela.entra(cenaCastelo)
    cenaCastelo.vai()    
Historia()