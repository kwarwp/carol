# jussiara
from _spy.vitollino.main import Cena, Elemento, Texto

MACACO ="http://imagensemoldes.com.br/wp-content/uploads/2018/03/Imagem-de-Desenhos-%E2%80%93-Imagem-Bob-Zoom-Macaco-1-PNG-236x300.png"

def Historia():
    MATA = Cena(img = "https://mundoeducacao.bol.uol.com.br/upload/conteudo_legenda/203947a3b090fb4199854898fda07ae9.jpg") 
    macaco= Elemento(img=MACACO, tit="macaco", style=dict(left=150, top=60, width=60, height=200))
    macaco.entra(MATA)
    MATA.vai()
Historia()