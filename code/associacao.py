class Pub_company:

    def __init__(self, name_company, cnpj) -> None:

        self.name_company = name_company
        self.cnpj = cnpj

    def get_cnpj(self):

        return self.cnpj


class Book:

    def __init__(self, title: str, pub_company: Pub_company) -> None:

        self.title = title
        self.pub_company = pub_company


pub_company = Pub_company(name_company='Saraiva', cnpj=123456)
book = Book(title='Alice', pub_company=pub_company)

# Consigo acessar um metodo dentro de outra classe
print(book.pub_company.get_cnpj())


# Quest POO#04 - Cliente e Endereço
# ​Implemente uma classe que instancie um Cliente e um Endereço.

# O Endereço deve conter os seguintes atributos: Rua e Numero.

# - Deve ser possível definir/alterar e obter a Rua e o Numero do Endereço.

# - Deve existir um método que traga em uma única string as informações unificadas do Endereço.

# O Cliente deve conter os seguintes atributos: Nome e Endereço.

# - Deve ser possível definir/alterar e obter o Nome e o Endereço.

# - Endereço deve ser um objeto do tipo Endereço.

# Externamente as classes, exiba o endereço de um cliente.


class Endereco:

    def __init__(self, rua: str, numero: int) -> None:

        self.rua = rua
        self.numero = numero

    def getRua(self):

        return self.rua

    def getNumero(self):

        return self.numero

    def getFullAdress(self):

        return f"""Sua rua :{self.rua} , seu numero : {self.numero}"""


class Cliente:

    def __init__(self, nome: str, endereco: Endereco) -> None:

        self.nome = nome
        self.endereco = endereco


Adress = Endereco(rua='Sao Cristovao', numero=11904)

cliente = Cliente(nome='Johns', endereco=Adress)

print(cliente.endereco.getFullAdress())

# -------------------------------------------------------------------------------------------------------------


class Cart:

    def __init__(self) -> None:
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(f"""{product.name} ,{product.value} """)


class Product:

    def __init__(self, product_name, product_value) -> None:
        self.name = product_name
        self.value = product_value


p1 = Product("Caneta", 10)
p2 = Product("Caderno", 7)
p3 = Product("Borracha", 1)

cart = Cart()

cart.insert_product(p1)
cart.insert_product(p2)
cart.insert_product(p3)

print(cart.list_products())
