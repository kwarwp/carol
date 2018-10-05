# luana cristina
from _spy.vitollino.main import Cena,Elemento,Texto

HOMEM = "https://1.bp.blogspot.com/-RilnuddcuWQ/Wc2BC-eYG8I/AAAAAAAABGs/tLwWjcNOig4gxl7RGF6lN-uPKrLVoKPqQCLcBGAs/s320/arvore_que_abraca%2B2.png"
def Historia():
    ARVORES = Cena(img = "https://pensamentoverde.com.br/wp-content/uploads/2016/11/1-arvore.jpg")
    homem = Elemento(img=HOMEM, tit="Homem", style=dict(left=150, top=60, width=60, height=200))
    ARVORES.vai()
Historia()