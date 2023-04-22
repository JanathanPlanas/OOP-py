class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str: # Sempre é printado na tela apos chamar a classe 
        return f"Pessoa chamada {self.name}, com idade de {self.age}"

    def __repr__(self) -> str: #printa como a classe foi escrita
        return f"{self.__class__.__name__}({self.name}, {self.age})"

        

person = Person("Johns", 23)

print(person)

print(repr(person))