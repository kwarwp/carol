# bruna de sa
from _spy.vitollino.main import Cena, Elemento,Texto

BINGBONG="https://1.bp.blogspot.com/-Es_iDlKRTbs/V5u5Qt7b99I/AAAAAAAAHqQ/VjTmmynFDREmMq-U5NpUhY8Cxm3q1hZHgCLcB/s640/Bingbong.png"
def Historia():
    cenaFloresta=Cena(img="https://i.pinimg.com/originals/75/37/5f/75375f348c8cc15f919bfc05f37dbb72.jpg")
    bingbong = Elemento(img= BINGBONG,
              tit ="Caçador",
              style = dict(left=150, top=60, width=60, height=200))
    bingbong.entra(cenaFloresta)
    txtcacador = Texto (cenaFloresta, "Hello")
    bingbong.vai = txtcacador.vai
    cenaFloresta.vai()
Historia()