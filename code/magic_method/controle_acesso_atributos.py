class Baggage:
    def __init__(self, items: list) -> None:
        self.items = items

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = value
        else:
            raise Exception("Valor Inválido...")

    def __getattr__(self, attr_name):
        print("__getattr__")
        # Acessado quando o atributo não existe
        return self.__dict__.get(attr_name, None)

    # Acessado quando o atributo não existe, cria o atributo se não existir
    def __setattr__(self, __name, __value) -> None:
        print("__setattr__")
        self.__dict__[__name] = __value
        return __value

    def __delattr__(self, __name) -> None:  # Deleta o atributo
        value = self.__dict__.get(__name, None)
        self.__dict__.__delitem__(__name)
        print(f"Atributo {__name} deletado com valor {value}")


bag = Baggage(["Item 1", "Item 2"])
print(bag.name)
print(bag.items)
bag.name = 'Johns Pena'

bag.items = ['dale', 'arroba']
print(bag.name)
print(bag.__dict__)
