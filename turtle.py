'''#Desafio 01
def gerar_nome_completo(nome,sobrenome):
   print(f'nome {nome} e sobrenome {sobrenome} ')

gerar_nome_completo('Bianor','Ramos')

#Desafio 02

def calcular_valor(preço, qauntidade = ):
    print(preço * qauntidade)

calcular_valor(10)'''

#Desafio de argumentos posicionais e dinâmicos 
'''def gerar_ojeto_personalizado(cor,*, altura, formato):
    print(cor, altura, formato)

gerar_ojeto_personalizado('azul', altura='155', formato='qualquer')'''

#Simplificar
from turtle import Turtle
t = Turtle()

def obter_distancia():
    respostas = int(input('Qauntos pixels devemos movimentar para frente? '))
    return respostas

def rotacionar_turtle(turtle):
    movimentar_para_lado = input(
        'Rotacionar para d:direita ou para e:esquerda, n: não rotacionar: ')
    if movimentar_para_lado == 'd':
        rotacionar_para_direita(turtle)
    elif movimentar_para_lado == 'e':
        rotacionar_para_esquerda(turtle)


def rotacionar_para_direita(turtle):
    angulo = int(input('Quanto para direita devemos ir? '))
    t.right(angulo)

def rotacionar_para_esquerda(turtle):
    angulo = int(input('Quanto para direita devemos ir? '))
    t.right(angulo)


while True:
    direcao = input('Para qual direção devemos ir "f:frente" ou "t:trás"')
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('continuar andando')
    if resposta not in ('sim', 's'):
            break