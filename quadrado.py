class Quadrado:
    def __init__(self, lado) -> None:
        self.lado = lado
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = self.lado * self.lado
        return f'Área = {self.lado}² = {self.area:.2f}'

    def calcular_perimetro(self):
        self.perimetro = 4 * self.lado 
        return f'Perímetro = 4 * {self.lado} = {self.perimetro:.2f}'


if __name__ == "__main__":
    lado = int(input('Informe a medida do lado: '))

    quadrado = Quadrado(lado)
    print(quadrado.calcular_area())
    print(quadrado.calcular_perimetro())