
class Ventilador:
    model = 'ABC'

    def __init__(self, velocity=0, state=False, rotation=False) -> None:
        self.state = state
        self.velocity = velocity
        self.rotation = rotation

    def turn_on(self):

        self.state = True

    def turn_off(self):

        self.state = False

    def change_velocity(self, velocity):
        real_vel = velocity*self.pick_tax_velocity()
        self.velocity = real_vel

    def turn_on_rotation(self):
        self.rotation = True

    def turn_off_rotation(self):  # método de instância, usa a palavra espcial self
        self.rotation = False

    @classmethod  # Método de classe , usa a palavra especial cls
    def change_model(cls, new_model):
        cls.model = new_model

    @staticmethod
    def pick_tax_velocity():
        return 0.25


ventilador_1 = Ventilador(5)
print(ventilador_1.velocity)
ventilador_1.change_velocity(10)
print(ventilador_1.velocity)

ventilador_2 = Ventilador()
print(ventilador_1.state)
ventilador_1.turn_on()
print(ventilador_1.state)

print(ventilador_1.model)
print(ventilador_2.model)
print(Ventilador.model)

Ventilador.change_model("XYZ")
print(ventilador_1.model)
print(ventilador_2.model)
print(Ventilador.model)


# Usando métodos dentro de outros métodos
class Classtest:

    

    def __init__(self) -> None:

        self.attr1 = 2
        self.attr2 = 'Johns'
        self.attr3 = self.method_attr3()

    def method_attr3(self):
        return self.attr1**2

    def methods(self):
        return self.method_attr3()


teste = Classtest()
print(teste.__dict__)  # Transforma os atributos e valores em diciionarios,


class Circle:

    pi = 3.14

    def __init__(self, radius) -> None:
        self.r = radius

    @classmethod
    def change_pi(cls, new_pi):
        cls.pi = new_pi

    def getArea(self) -> float:
        return ( Circle.pi * (self.r ** 2) )

    def getCircunferencia(self) -> float:

        return ( Circle.pi * 2 * self.r )


Circle.change_pi(new_pi =4) # Mudando o valor de pi
circle = Circle(radius= 5)
print(f"A área do círculo é: {circle.getArea()}")
print(f"A circunferência do círculo é: {circle.getCircunferencia()}")




class Kangaroo:
    def __init__(self, name, contents=[]):
        """Inicialize o conteúdo da bolsa.
        nome: string
        conteúdo: conteúdo inicial da bolsa.
        """
        self.name = name
        self.pouch_contents = contents

        if contents is None :
            self.pouch_contents = []
        else :
            self.pouch_contents = contents


    def __str__(self):
        """Retorne uma representação de string deste Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    def put_in_pouch(self, item):
        """Adiciona um novo item ao conteúdo da bolsa.
        item: objeto a ser adicionado
        """
        self.pouch_contents.append(item)
kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print(kanga)

class Warehouse:

    purpose = 'storage'
    region = 'west'

wi = Warehouse()
wi.region= 'east'
print(wi.region)