
# __variavel -> private

# O Encapsulamente é um dos pilares da orientação a objetos.Serve para proteger dados da classe.
# Encapsular os dados de uma aplicação significa evitar que estes sofram acessos indevidos
class Clients:

    def __init__(self) -> None:
        self.data = []

    def add_client(self, client):
        self.data.append(client)

    def get_clients(self):
        return self.data

    def remove_clients(self, client):
        if client in self.data:
            self.data.remove(client)
            return True
        else:
            return False

    # Getter
    @property
    def data(self):
        return self._data

    # Setter
    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = value
        else:
            print("Valor inválido !")
# Getter e Sett adicionar camada de proteção


clients__data = Clients()
clients__data.data = 'Outro valor'
print(clients__data.__dict__)

# clients__data.__data  # Nesse formato, não consegue acessar a variavel
# Cria uma outra instancia da variavel, sem alterar a classe
# clients__data.__data = 'Um outro valor'

# print(clients__data.__data)  # Consegue acessar a variavel
# print(clients__data._Clients__data)  # Consegue acessar a variavel
# print(clients__data.__dict__)

# Outro exemplo


class Produto:

    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco - self.preco - (self.preco * (percentual/100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, value):
        if isinstance(value, str):
            self._preco = float(value.replace("R$", ''))
        else:
            pass


p1 = Produto(nome="Camiseta", preco=50)
p1.desconto(10)
print(p1.preco)

p2 = Produto(nome="Camiseta", preco='R$50')
p2.desconto(10)
print(p2.preco)

# Implementar uma classe que representa uma Conta Bancária.

# Deve possuir os seguintes atributos: Código da Conta, Nome do Titular, Senha, Email e Saldo.

# O Código da conta é único e imutável;
# A senha deve conter no mínimo 8 caracteres, composta apenas por números.
# A senha pode ser alterada a partir da confirmação do email e da senha atual.
# Para depositar ou retirar do Saldo é necessário validar a senha.
# É possível visualizar a conta imprimindo o Nome do Titular, Código da Conta e Saldo.
# O Saldo da conta não pode ser menor que 0.
# É bacana que todos os atributos possuam setters e getters definidos (isso pode ser usado a seu favor para implementar uma das features solicitadas pelo banco).​

# Dica: Utilize raise para levantar Exceptions em situações inválidas.


class BankAccount:

    account_code = 123456

    def __init__(self, nome, senha, email) -> None:

        self.nome = nome
        self.senha = senha
        self.email = email
        self.__code = BankAccount.account_code
        self.balance = 0

        BankAccount.plus_account_code()

    @classmethod
    def plus_account_code(cls):
        cls.account_code += 1

    
    def troca_senha(self,email, senha_atual, senha_nova) :
        
        if (self.email == email) and (self.senha == senha_atual) :
            self.senha = senha_nova
        else :
            raise Exception("Dados incorretos")


    def withdraw(self, value, senha):

        if senha == self.senha:

            if self.balance > value:
                self.balance = self.balance - value
            else:
                raise Exception("Saldo insuficiente")
        else:

            raise Exception("Senha incorreta")


    def deposit(self, value, senha):

        if (senha == self.senha) and value >= 0:
            self.balance = self.balance +value
        else :
            raise Exception("Senha incorreta")


    @property
    def email(self):

        return self._email

    @email.setter
    def email(self, value):

        if isinstance(value, str) and  "@" in value:
            self._email = value
        else:
            raise Exception('email inválido')

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        if isinstance(value, int) and len(str(value)) >= 8:
            self.__senha = value
        else:
            raise Exception("Senha inválida")

    @property
    def balance(self):

        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, int) and value >= 0:
            self._balance = value

        else:

            raise Exception("Valor inválido")

    def getConta(self):

        return f"""Codigo da conta : {self.__code}
                Nome do titular  : {self.nome}
                Saldo : {self.balance}
            """


johns_account = BankAccount(email='janathan@junior.com',
                     senha = 123456879, nome= 'Johns')


print(johns_account.getConta())
johns_account.deposit(175000,123456879)


print(johns_account.getConta())
johns_account.withdraw(7500,123456879)
print(johns_account.getConta())