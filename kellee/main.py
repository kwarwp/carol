# vitoria
from _spy.vitollino.main import Cena,Elemento,Texto
PERSONAGEM ="https://images.vexels.com/media/users/3/130955/isolated/preview/08c00870e43aa206e86e5f3b3495e902-personagem-de-desenho-animado-da-menina-hipster-by-vexels.png"
def Historia():
    cenaSea = Cena(img = "https://media-cdn.tripadvisor.com/media/photo-s/11/56/f7/65/grande-teatro-palacio.jpg")
    personagem = Elemento(img= PERSONAGEM,
                 tit ="Personagem",
                 style = dict(left=150, top=60, width=60, height= 200))
    personagem.entra(cenaSea)
    txtpersonagem = Texto (cenaSea, "Hello")
    personagem.vai = txtpersonagem.vai
    cenaSea.vai()
Historia()