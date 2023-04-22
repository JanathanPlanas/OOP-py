import random


class Clients:

    def __init__(self, name) -> None:
        self.name = name
        self.address = []

    def insert_address(self, city, state, street, number):

        self.address.append(Address(city, state, street, number))

    def list_address(self):
        for address in self.address:
            print(f"{address.city} {address.state}")

    def __del__(self):
        print(f"Cliente {self.name} foi deletado")


class Address:

    def __init__(self, city, state, street, number) -> None:

        self.city = city
        self.state = state
        self.street = street
        self.number = number


cliente = Clients('Johns')
cliente.insert_address("Fortaleza", " Ceara", "Rua a", "1234")
cliente.insert_address("Recife", " Bahia", "Rua B", "1234")
cliente.insert_address("Pernambuco", " Salvador", "Rua C", "1234")
cliente.list_address()


# Quest POO#05 - Deck de Cartas
# Há 52 cartas em um baralho, e cada uma pertence a 1 dos 4 naipes e a 1 dos 13 valores. Os naipes são espadas, copas, ouros e paus (no bridge, em ordem descendente). A ordem dos valores é 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 e 13.
# Desenvolva uma classe que represente a carta (Card), tendo como característica o naipe e seu número. Crie um deck de cartas que gere todas as cartas do baralho, tendo a opção de embaralhar (suffle), adicionar uma carta (append_card) e retirar uma carta (pop_card).
# Desenvolva a classe Player que pode construir seu baralho (tanto puxar uma carta do deck, como receber 12 diferentes cartas de uma vez).
# Para esta quest, trabalhe com a lógica da Composição e Associação.
# Dica: Utilize o random.randint para auxiliar na função shuffle


class Card:

    def __init__(self, card_suit: str, card_rank: int) -> None:

        self.suit = card_suit
        self.rank = card_rank

    def show(self):
        return f"{self.suit} - {self.rank} "

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value in ['ouros', 'copas', 'espadas', 'paus']:
            self._suit = value
        else:
            raise ValueError("Naipe inválido .. ")

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value >= 1 and value <= 13:
            self._rank = value
        else:
            raise ValueError("Valor de carta inválida")



class Deck:


    def __init__(self) -> None:
        self.cards = self.generate_deck()

    def generate_deck(self):

        list_of_cards = []

        for suit in ["ouros", "espadas", "paus", "copas"]:

            for rank in range(0, 13):

                list_of_cards.append(Card(suit, rank+1))

        return list_of_cards

    def create_deck(self):

        self.cards = self.generate_deck()


    def show(self):

        for card in self.cards:

            print(card.show())


    def append_card(self, card: Card):

        self.cards.append(card)


    def pop_card(self):

        return self.cards.pop()


    def shuffle(self):

        for card_i in range(len(self.cards)-1, 0, -1):
            card_j = random.randint(0, card_i)
            self.cards[card_i], self.cards[card_j] = self.cards[card_j], self.cards[card_i]



class Player:

    def __init__(self, person_name) -> None:
        self.name = person_name
        self.hand = []

    def pick_card(self, deck : Deck):

        self.hand.append(deck.pop_card())

    def build_hand(self, deck: Deck, number_of_cards: int):

        self.hand = []

        for i in range(number_of_cards):

            self.pick_card(deck)

    def show(self):
        for card in self.hand:

            print(card.show())






deck = Deck()
deck.shuffle()

player_1 =Player("Johns")
player_2 = Player("Ze")


print('Johs')
player_1.build_hand(deck,1)
player_1.show()


print("Ze")
player_2.build_hand(deck,2)
player_2.show()


print(len(deck.cards))
print("########")
deck.show()


######################################
