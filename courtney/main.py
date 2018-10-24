# carol.courtney.main.py
# yasmin.
from _spy.vitollino.main import Cena,Elemento,Texto
PERSONAGEM ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjmwdSo2PfdAhVtuVkKHdWDAMoQjRx6BAgBEAU&url=http%3A%2F%2Flife-writer.tumblr.com%2Fpost%2F123761609710%2Fi-missed-my-kids&psig=AOvVaw1kWh3XpDoI0P2G30m_UH6o&ust=1539116915250785.png"
def Historia():
    cenaSea = Cena(img = "https://www.google.com.br/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjH8oXQ_J_eAhWCkJAKHQTIAg8QjRx6BAgBEAU&url=https%3A%2F%2Fpixabay.com%2Fpt%2Ffloresta-%25C3%25A1rvores-plantas-ecologia-148727%2F&psig=AOvVaw0BTrUAOeOZQqkjv_b3oqGo&ust=1540501280689184.png")
    personagem=Elemento(img=PERSONAGEM,
               tit="historias da neve",
               style = dict(left=150,top=60,width=60,height=200))
    personagem.entra(cenaSea)
    txtpersonagem = Texto (cenaSea,"Hello")
    personagem.vai()
    cenaSea.vai
Historia()   