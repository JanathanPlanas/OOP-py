class Pay:
    def __init__(self, work_hours) -> None:
        self.work_hours = work_hours
        self.extra_hours = None
        self.salary = self.work_hours * Pay.pay_per_hour()

    @staticmethod
    def pay_per_hour():
        return 80

    def __call__(self, hours):
        self.extra_hours = hours
        self.work_hours += self.extra_hours
        self.salary = self.work_hours * Pay.pay_per_hour()
        return self.salary


pay_test = Pay(8)
# print(pay_test.__dict__)
# pay_test(12)
# print(pay_test.__dict__)
print(pay_test(2))

# Quest POO#10 - Resolvendo um polinômio
# Polinômio é uma expressão algébrica formada por monômios. Um polinômio nada mais é que a soma algébrica de monômios, ou seja, são mais monômios separados por adição ou subtração entre si.

# De forma geral, um polinômio pode ter vários termos, ele é representado algebricamente por:




# Veja mais sobre "Polinômios" em: https://brasilescola.uol.com.br/matematica/polinom...
# Implemente uma Classe que instancia um objeto com a lista dos coeficientes e a partir do método __call__ possa resolver o polinômio para um valor de X informado durante a chamada.



class Poli:
    def __init__(self, list_coef) -> None:
        self.coefs = list_coef

    def __call__(self, x_value) -> float:
        sum_value = 0
        for index in range(0, len(self.coefs)):
            sum_value += self.coefs[index] * (x_value ** index)
        return sum_value

poli = Poli([1, 2, 3, 4])
print(poli(2))
# 1 + 2*2**1 + 3*2**2 + 4*2**3
# 1 + 4 + 12 + 32
# 5 + 44
# 49