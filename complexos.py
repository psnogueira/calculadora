# Calculadora de Números Complexos

class Complexo:
    # Construtor da classe 'Complexo'
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Adição
    def __add__(self, other):
        return Complexo(self.real + other.real, self.imag + other.imag)

    # Subtração
    def __sub__(self, other):
        return Complexo(self.real - other.real, self.imag - other.imag)

    # Multiplicação
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complexo(real, imag)

    # Exponenciação
    def __pow__(self, power, modulo=None):
        x = Complexo(self.real, self.imag)
        for i in range(1, power):
         x = x * self
        return Complexo(x.real, x.imag)

    # Retorna o número complexo formatado Ex: (1,3) => "1+3i"
    def __str__(self):
        if self.imag < 0:
            return f"{round(self.real, 3)}{round(self.imag, 3)}i"
        else:
            return f"{round(self.real, 3)}+{round(self.imag, 3)}i"


# Exemplo de uso
a = Complexo(1, 1) # número complexo "1+1i"
b = Complexo(1, 1/3) # número complexo "-2+1i"
c = Complexo(-6/5, 3) # número complexo "-(6/5)+3i" 

# Operações ()
soma = a + b
subtracao = a - b
multiplicacao = b * c
exponenciacao = c**3

# Exemplo
eq = a * b + c**2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Potênciacao: {exponenciacao}")
print(f"Exemplo: {eq}")

# Saída esperada:
#
# Soma: 2+1.333i
# Subtração: 0+0.667i
# Multiplicação: -2.2+2.6i
# Potênciacao: 30.672-14.04i
# Exemplo: -6.893-5.867i
