# carol.courtney.main.py
# yasmin.
from _spy.vitollino.main import Cena,Elemento,Texto
PERSONAGEM ="http://3.bp.blogspot.com/-EUuOvz2jl9w/T43K0qeYjFI/AAAAAAAAAOc/OcDgvqPOn64/s1600/3.png"
def Historia():
    cenaSea = Cena(img = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiHltyB3vfdAhWOzlkKHR49B8gQjRx6BAgBEAU&url=http%3A%2F%2Fpt-br.contos-de-hora-de-aventura.wikia.com%2Fwiki%2FArquivo%3A294392_Papel-de-Parede-Castelo-Doce-Hora-da-Aventura_1920x1080.jpg&psig=AOvVaw3Csk-jnuzvEvpqP_P6cRev&ust=1539118413301038")
    personagem=Elemento(img=PERSONAGEM,
               tit="historias da neve",
               style = dict(left=150,top=60,width=60,height=200))
    personagem.entra(cenaSea)
    txtpersonagem = Texto (cenaSea,"Hello")
    personagem.vai()
    cenaSea.vai
Historia()   