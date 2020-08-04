
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    dicionario_rotacao_direita ={
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    dicionario_rotacao_esquerda = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.dicionario_rotacao_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.dicionario_rotacao_esquerda[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0, self.velocidade)


direcao = Direcao()

print(direcao.valor)
direcao.girar_a_direita()
print(direcao.valor)
direcao.girar_a_esquerda()
print(direcao.valor)





