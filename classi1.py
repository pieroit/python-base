
class Gruppo:
    def __init__(self, membri=[]):
        self.membri = membri

    def aggiungi(self, membro):
        self.membri.append(membro)

    def __str__(self):
        s = 'Gruppo:\n'
        for m in self.membri:
            s = s + m.nome + '\t'

        return s



class Persona:

    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        print('ciao sono ' + self.nome)

    def __add__(self, other):
        #p3_nome = self.nome + other.nome
        #p3 = Persona(p3_nome)
        #return p3

        # modo 1
        g = Gruppo([self, other])

        return g



p1 = Persona('Filippo')
p2 = Persona('Dario')

print(p1.nome)
p1.saluta()

print(p2.nome)
p2.saluta()

gruppo = p1 + p2
print(type(gruppo))
print(gruppo)



class Tecnico(Persona):

    def __init__(self, nome, mansione):
        super().__init__(nome)
        self.mansione = mansione

    def ripara(self):
        print('Spegni e riaccenni')

t = Tecnico('Giulio', 'sistemista')
print(t.nome, t.mansione)
t.ripara()
t.saluta()

t2 = Tecnico('Sara', 'front-end developer')
team = t + t2
print(team)

class Jeep:

    def __init__(self, modello, trazione):
        self.modello = modello
        self.trazione = trazione

    def clacson(self):
        print('BEEEEEEEEEP')

class Transformer(Persona, Jeep):

    def __init__(self, nome, modello, trazione):
        super().__init__(nome)
        Jeep.__init__(self, modello, trazione)

trans = Transformer('Rinaldo', 'Panda', '4*4')
trans.saluta()
trans.clacson()
print(trans.modello, trans.trazione)