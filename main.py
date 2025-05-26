# ESCOLHA CIRCULO, QUADRADO E TRIÂNGULO
# SOLICITAR DADOS DE AREA E PERÍMETRO
# CADA FIGURA SERA UMA CLASSE COM SEUS ATRIBUTOS
# EXIBIR O CALCULO E A FORMULA 
# DEVE HABER UM LOOPING INICIAL QUE SEMPRE  PERMITIRÁ A ESCOLHA DE UMA NOVA FIGURA

from circulo import Circulo
from quadrado import Quadrado
from triangulo import Triangulo

if __name__ == "__main__":
    print('1 - Circulo')
    print('2 - Quadrado')
    print('3 - Triângulo')
    print('4 - Sair')
    opcao = int(input('O que você deseja fazer?: '))

    while opcao != 4:
        if opcao == 1:
            raio = float(input('Informe o raio: '))

            circulo = Circulo(raio)
            print(f'Área = {circulo.calcular_area()}')
            print(f'Perímetro = {circulo.calcular_perimetro()}')
            opcao = int(input('O que você deseja fazer?: '))
        
        if opcao == 2:
            lado = float(input('Informe a medida do lado: '))

            quadrado = Quadrado(lado)
            print(quadrado.calcular_area())
            print(quadrado.calcular_perimetro())
            opcao = int(input('O que você deseja fazer?: '))

        if opcao == 3:
            primeiro_lado = float(input('Informe o primeiro lado: '))
            segundo_lado = float(input('Informe o segundo lado: '))
            terceiro_lado = float(input('Informe o terceiro lado: '))

            triangulo = Triangulo(primeiro_lado, segundo_lado, terceiro_lado)
            print(triangulo.calcular_perimetro())
            print(triangulo.calcular_area())
