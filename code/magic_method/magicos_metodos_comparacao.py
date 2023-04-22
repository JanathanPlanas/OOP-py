class Word:
    def __init__(self, word) -> None:
        self.content = word

    def __eq__(self, __o: object) -> bool: #equal
        print("Comparando igualdade...")
        return len(self.content) == len(__o.content) 
 
    def __gt__(self, __o:object) -> bool:  # greater than

        print("Comparando > ..")
        return len(self.content) > len(__o.content)

    def __lt__(self, __o: object) -> bool:  #less than
        print("Comparando <...")
        return len(self.content) < len(__o.content)

    def __le__(self, __o: object) -> bool:   # less or equal
        print("Comparando <=...")
        return len(self.content) <= len(__o.content)

    def __ge__(self, __o: object) -> bool:  # greater or equal
        print("Comparando >=...")
        return len(self.content) >= len(__o.content)

    def __ne__(self, __o: object) -> bool:  # not equal
        print("Comparando !=...")
        return len(self.content) != len(__o.content)


word_1 = Word("Carro")
word_2 = Word("Bicicleta")
print(word_1 == word_2)
print(word_1 != word_2)
print(word_1 >= word_2)
print(word_1 <= word_2)
print(word_1 > word_2)
print(word_1 < word_2)