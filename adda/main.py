# lucimara
from _ spy.vitollino.main import Cena, Elemento, Texto

SIRI ="https://i.pinimg.com/originals/ff/00/51/ff005199bfa12a152819f86b196a6037.png"

def Historia():
    PRAIA = Cena(img = "https://www.fundospaisagens.com/Imagens/fundo-de-ecra-de-praia.jpg")
    siri = Elemento(img=SIRI, tit="Siri", style=dict(left=150, top=60, whidth=60, height=200))
    siri.entra(PRAIA)
    PRAIA.vai()
Historia()