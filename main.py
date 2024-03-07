def analisar_nivel_energia(nivel):
    if nivel <= 8000:
        return "Inseto!"
    else:
        return "Mais de 8000!"

# Número de casos de teste
C = int(input("Digite o número de casos de teste: "))

# Processar cada caso de teste
for _ in range(C):
    nivel_energia = int(input("Digite o nível de energia do ser vivo: "))
    resultado = analisar_nivel_energia(nivel_energia)
    print(resultado)
