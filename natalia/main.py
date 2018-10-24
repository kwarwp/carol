#nathan
from _spy.vitollino.main import Cena,Elemento,Texto

GOKU="https://2.bp.blogspot.com/-TLxp11naewU/WY3Ff6Iu6iI/AAAAAAAAIFE/r7yeQjVKXuYDzuDkBJ8q0oAC51Z58JnHgCLcBGAs/s1600/Goku%2BSuper%2BSayajin%2Bdeus.png"

def Historia():
    cenaFloresta=Cena(img="https://upload.wikimedia.org/wikipedia/commons/f/f5/Floresta_de_Chantilly.JPG")
    gokudeussupersayjin = Elemento(img = GOKU,
                          tit= " goku deus super sayjin",
                          style=dict(left=150, top=60, width= 60, height= 200))
                        
    gokudeussupersayjin.entra(cenaFloresta)
    txtGoKu=Texto (cenaFloresta, "Hello")
    gokudeussupersayjin.vai=txtgokudeussupersayjin.vai
    cenaFloresta.vai()
Historia()  