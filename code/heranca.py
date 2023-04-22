class Person:

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age

    def set_name(self, value):
        self.name = value

    def get_name(self):
        return self.name


class PhysicPerson(Person):

    def __init__(self, name, age, cpf) -> None:
        super().__init__(name, age)

        self.cpf = cpf

    def set_cpf(self, value):
        self.cpf = value

    def get_cpf(self):
        return self.cpf


class LegalPerson(Person):
    def __init__(self, name, age, cnpj: int) -> None:
        super().__init__(name, age)

        self.cnpj = cnpj

    def set_cnpj(self, value):
        self.cnpj = value

    def get_cnpj(self):
        return self.cnpj


if __name__ == "__main__":

    Johns = PhysicPerson('Johns', 30, 5481)
    print(f"O nome {Johns.name} e idade {Johns.age} \n")
    print(f"O cpf {Johns.get_cpf()} e o nome {Johns.get_name()}")

    Americanas = LegalPerson('Lojas Americanas', 50, 548100018518)
    print(f"O nome {Americanas.name} e idade {Americanas.age} \n")
    print(f"O CNPJ {Americanas.get_cnpj()} e o nome {Americanas.get_name()}")


# Quest POO#07 - Tickets do Cinema
# ​Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimeValor()

# Crie uma classe VIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso VIP (com o adicional incluído).

class Ingresso:

    def __init__(self, value: float) -> None:

        self.reais = value

    def ImprimeValor(self):

        return f"{self.reais} R$"


class VIP(Ingresso):

    def __init__(self, value: float, add_value) -> None:
        super().__init__(value)

        
        self.add_value = add_value

        
    def get_full_valor(self):

        return f"{self.add_value + self.reais} R$ "


ingresso = VIP(23.40, 15.50)
print(ingresso.get_full_valor())
