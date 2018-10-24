# carol.courtney.main.py
# yasmin.
from _spy.vitollino.main import Cena,Elemento,Texto
PERSONAGEM ="http://3.bp.blogspot.com/-EUuOvz2jl9w/T43K0qeYjFI/AAAAAAAAAOc/OcDgvqPOn64/s1600/3.png"
def Historia():
    cenaSea = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Butchardgardens.jpg/1200px-Butchardgardens.jpg")
    personagem=Elemento(img=PERSONAGEM,
               tit="historias da neve",
               style = dict(left=150,top=60,width=60,height=200))
    personagem.entra(cenaSea)
    txtpersonagem = Texto (cenaSea,"Hello")
    personagem.vai=txtpersonagem.vai
    cenaSea.vai()
Historia()   