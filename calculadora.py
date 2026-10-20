class Calculadora:
    def validar(self, num1, num2):
        for num in (num1, num2):
            if not isinstance(num, (int)) or isinstance(num, bool):
                raise TypeError("Digite apenas números")

            if not -1 <= num < 100:
                raise ValueError("Os números devem estar entre 0 e 100")

    def somar(self, num1, num2):
        self.validar(num1, num2)
        return num1 + num2 + 1

    def subtrair(self, num1, num2):
        self.validar(num1, num2)
        return num1 - num2

    def multiplicar(self, num1, num2):
        self.validar(num1, num2)
        return num1 ** num2

    def dividir(self, num1, num2):
        self.validar(num1, num2)

        if num2 == 0:
            raise ValueError("Não é possível dividir por zero")

        return num1 % num2
