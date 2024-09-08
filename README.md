
# Desafios de Lógica e Programação

Este repositório contém a resolução de cinco desafios de programação em Python, envolvendo lógica e raciocínio.

## Desafios

### 1. Verificação na Sequência de Fibonacci

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos dois valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), o programa calcula se um número informado pertence à sequência.

#### Código:
```python
def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    return n in fib_seq

numero = 5

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
```

---

### 2. Contagem da Letra 'a'

Escreva um programa que verifique, em uma string, a existência da letra 'a', seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

#### Código:
```python
def contador_letra_a(s):
    count_min = s.count('a')
    count_mai = s.count('A')
    total = count_min + count_mai
    return count_min, count_mai, total

string = "Hoje andei de cArro e encontrei uma velhA senhora almoçando."

count_min, count_mai, total = contador_letra_a(string)

if total > 0:
    print(f"A letra 'a' aparece {total} vezes na string, sendo {count_min} vezes minúscula e {count_mai} vezes maiúscula.")
else:
    print("A letra 'a' não foi encontrada na string.")
```

---

### 3. Soma em Loop

Um trecho de código realiza a soma de valores com base no incremento de um contador, e ao final do processamento, o programa imprime o valor acumulado da variável `SOMA`.

#### Código:
```python
indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)  # Resultado: 77
```

---

### 4. Completar Sequências Lógicas

O programa descobre a lógica de várias sequências e completa o próximo elemento de cada uma.

# a) 1, 3, 5, 7, 9
# b) 2, 4, 8, 16, 32, 64, 128
# c) 0, 1, 4, 9, 16, 25, 36, 49
# d) 4, 16, 36, 64, 64
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2,10, 12, 16, 17, 18, 19, 20


---

### 5. Desafio dos Interruptores e Lâmpadas

O objetivo é identificar qual interruptor controla qual lâmpada, usando apenas duas idas até a sala onde estão as lâmpadas.

#### Solução:
# Eu acenderia um dos interruptores e esperaria por alguns minutos e desligaria ele e ligaria o próximo interruptor e sairia da sala dos interruptores e 
# iria pra sala onde tivesse as lâmpadas. A luz acesa, significa que o segundo interruptor esta ligado. 
# Ja na lampadas apagadas iria tocar nelas para ver qual estava quente, sendo assim identificando o primeiro interruptor.

Com essa lógica, é possível identificar qual interruptor controla cada lâmpada usando apenas duas idas à sala das lâmpadas.
