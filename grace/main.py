#GabrielLucas e Brenno
from _spy.vitollino.main import Cena, Elemento, Texto
MarioBros= "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/MarioSMBW.png/220px-MarioSMBW.png"
def Historia():
    cenaCastle = Cena(img = "https://http2.mlstatic.com/fundo-fotografico-tecido-newborn-3d-castelo-150m-x-220m-D_NQ_NP_812472-MLB27642632585_062018-O.webp")
    mario= Elemento(img=MarioBros,
            tit = "Mario",
            style = dict(left=150, top=60, width=60, height=200))
    mario.entra(cenaCastle)
    txtmario = Texto (cenaCastle,  "Hello")
    txtmario.vai=mario.vai
    cenaCastle.vai()
Historia()