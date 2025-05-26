class Circulo:
    def __init__(self, raio) -> None:
        self.raio = raio
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        self.area = 3.14 * (self.raio * self.raio)
        return f'Área = π * {self.raio}² = {self.area:.2f} cm²'

    def calcular_perimetro(self):
        self.perimetro = 2 * 3.14 * self.raio
        return f'Perímetro = 2 * π * {self.raio} = {self.perimetro:.2f} cm'
    

if __name__ == "__main__":
    raio = int(input('Informe o raio: '))

    circulo = Circulo(raio)
    print(circulo.calcular_area())
    print(circulo.calcular_perimetro())