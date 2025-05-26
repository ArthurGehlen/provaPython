class Triangulo:
    def __init__(self, primeiro_lado, segundo_lado, terceiro_lado) -> None:
        self.primeiro_lado = primeiro_lado
        self.segundo_lado = segundo_lado
        self.terceiro_lado = terceiro_lado
        self.area = 0
        self.semiperimetro = 0
        self.perimetro = 0

    def calcular_area(self):
        self.semiperimetro = self.perimetro / 2
        self.area = (self.semiperimetro * (self.semiperimetro - self.primeiro_lado) * (self.semiperimetro - self.segundo_lado) * (self.semiperimetro - self.terceiro_lado)) ** (1/2) 
        return f'Área = √ semiperímetro * (semiperímetro - {primeiro_lado})(semiperímetro - {segundo_lado})(semiperímetro - {terceiro_lado}) = {self.area:.2f}'
        
    def calcular_perimetro(self):
        self.perimetro = self.primeiro_lado + self.segundo_lado + self.terceiro_lado 
        return f'Perímetro = {self.primeiro_lado} + {self.segundo_lado} + {self.terceiro_lado} = {self.perimetro:.2f}'


if __name__ == "__main__":
    primeiro_lado = float(input('Informe o primeiro lado: '))
    segundo_lado = float(input('Informe o segundo lado: '))
    terceiro_lado = float(input('Informe o terceiro lado: '))

    triangulo = Triangulo(primeiro_lado, segundo_lado, terceiro_lado)
    print(triangulo.calcular_perimetro())
    print(triangulo.calcular_area())