class First:

    def __init__(self) -> None:
        self.attr_1 = 'iury'
        print("primeira")


class Second:

    def __init__(self) -> None:
        self.attr_2 = "davi"
        print("segunda")


class Third (First, Second):

    def __init__(self) -> None:
        # super().__init__()   # prioriza o primeiro parametro
        First.__init__(self)
        Second.__init__(self)


third = Third()
print(third.__dict__)
