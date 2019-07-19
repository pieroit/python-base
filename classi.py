
class Cittadino:

    a = 10

    def __init__(self, n, s='M', e=20):
        self.nome = n
        self.sesso = s
        self.eta = e

    def __add__(self, other):
        nome_fusione = self.nome + other.nome
        fus = Cittadino(nome_fusione)
        return fus

    def __lt__(self, other):
        return self.eta < other.eta

    def __str__(self):
        return f'nome: {self.nome}, sesso: {self.sesso}, eta: {self.eta}'

    def presentati(self):
        print( f'Ciao sono {self.nome}' )

class Papero(Cittadino):

    def __init__(self, n, colore, s='M', e=20):
        super().__init__(n, s, e)
        self.colore_pinne = colore

    def verso(self):
        print('QUA')

c = Cittadino('Paperino', 'M', 35)
c2 = Cittadino('Qua')

p = Papero('Gastone', 'red')
p.verso()
p.presentati()
print(p.colore_pinne)





