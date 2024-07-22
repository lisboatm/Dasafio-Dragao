## README

### Descrição

Este script Python lê um número de casos de teste e, para cada caso, determina se o nível de energia de um ser vivo está abaixo ou acima de 8000. O resultado é uma mensagem indicando se o nível de energia é "Inseto!" ou "Mais de 8000!".

### Funcionalidades

- Lê o número de casos de teste.
- Para cada caso de teste, lê um valor de nível de energia.
- Avalia o nível de energia e retorna uma mensagem correspondente:
  - "Inseto!" se o nível de energia for menor ou igual a 8000.
  - "Mais de 8000!" se o nível de energia for maior que 8000.
- Imprime a mensagem correspondente para cada nível de energia.

### Requisitos

- Python 3.6 ou superior.

### Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código em um arquivo, por exemplo, `main.py`.
3. Execute o script usando o comando:

```bash
python main.py
```

4. Siga as instruções no terminal para inserir o número de casos de teste e os valores de nível de energia para cada caso.

### Entrada

O programa solicita ao usuário que insira:

1. O número de casos de teste \( C \).
2. Para cada caso de teste, o nível de energia do ser vivo.

### Saída

Para cada caso de teste, o programa imprime:

- "Inseto!" se o nível de energia for menor ou igual a 8000.
- "Mais de 8000!" se o nível de energia for maior que 8000.

### Exemplo de Execução

```plaintext
Digite o número de casos de teste: 3
Digite o nível de energia do ser vivo: 5000
Inseto!
Digite o nível de energia do ser vivo: 8000
Inseto!
Digite o nível de energia do ser vivo: 9000
Mais de 8000!
```

### Explicação do Código

1. **Função `analisar_nivel_energia`:**
    ```python
    def analisar_nivel_energia(nivel):
        if nivel <= 8000:
            return "Inseto!"
        else:
            return "Mais de 8000!"
    ```
    Esta função recebe um valor de nível de energia e retorna uma mensagem baseada nesse valor.

2. **Leitura do Número de Casos de Teste:**
    ```python
    C = int(input("Digite o número de casos de teste: "))
    ```

3. **Loop Através dos Casos de Teste:**
    ```python
    for _ in range(C):
        nivel_energia = int(input("Digite o nível de energia do ser vivo: "))
        resultado = analisar_nivel_energia(nivel_energia)
        print(resultado)
    ```

### Contribuição

Sinta-se à vontade para contribuir com melhorias no código ou na documentação, abrindo issues ou pull requests no repositório correspondente.
