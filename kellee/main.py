# vitoria
from _spy.vitollino.main import Cena,Elemento,Texto
PERSONAGEM ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjmwdSo2PfdAhVtuVkKHdWDAMoQjRx6BAgBEAU&url=http%3A%2F%2Flife-writer.tumblr.com%2Fpost%2F123761609710%2Fi-missed-my-kids&psig=AOvVaw1kWh3XpDoI0P2G30m_UH6o&ust=1539116915250785.png"
def Historia():
    cenaSea = Cena(img = "https://media-cdn.tripadvisor.com/media/photo-s/11/56/f7/65/grande-teatro-palacio.jpg")
    personagem = Elemento(img= PERSONAGEM,
                 tit ="Personagem",
                 style = dict(left=150, top=60, width=60, height= 200))
    personagem.entra(cenaSea)
    txtpersonagem = Texto (cenaSea, "Hello")
    personagem.vai = txtpersonagem.vai
    cenaSea.vai
Historia()