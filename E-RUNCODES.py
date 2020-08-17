def main():
    piso = largura * comprimento
    volume_sala = largura * comprimento * altura
    area = 2 * altura * largura + 2 * altura * comprimento
    print(piso)
    print(volume_sala)
    print(area)

altura = float(input(""))
largura = float(input(""))
comprimento = float(input(""))

if __name__ == '__main__':
    main()
