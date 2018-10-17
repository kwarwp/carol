#Cibele
from _spy.vitollino.main import Cena, Elemento, Texto 

Chica="https://www.google.com.br/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwinuPvVrI7eAhWKIZAKHQ7cDWsQjRx6BAgBEAU&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F53128470583809726%2F&psig=AOvVaw1Dx2WPQc_aO0Aom3IEpQ1H&ust=1539895692884798"
def Historia():
        CenaTeatro = Cena(img ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdPLYgHZx_3F32cbuvh1F1JCtI7wCETneHux09yVAqsmfEOX5C")
        chica = Elemento(img=Chica,
                tit ="Chica",
                style = dict(left=150, top=60, width=60, height=200))
        CenaTeatro.vai()
Historia()