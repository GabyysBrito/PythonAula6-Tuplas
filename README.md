# 🐍 Anotações de Python - Tuplas 

- As **tuplas** são estruturas de dados imutáveis em Python, usadas para armazenar informações que não devem ser modificadas. Elas são definidas utilizando **parênteses ()**.

## 📌 Características das Tuplas

- **Imutáveis**: Após a criação, os elementos não podem ser alterados diretamente.
- **Mais rápidas**: Como não podem ser modificadas, possuem um desempenho melhor que listas.
- **Ocupa menos espaço na memória**: São mais eficientes quando comparadas a listas.
- **Podem armazenar diferentes tipos de dados**: Tuplas podem conter números, strings e até outras tuplas.
- **Permitem desempacotamento**: É possível atribuir os valores da tupla diretamente a variáveis.

## Estrutura de uma Tupla

```python
# Exemplo
 cores = ("vermelho", "azul", "verde")
 print(cores)
```

## 🔄 Modificando uma Tupla (Convertendo para Lista e de Volta para Tupla)

```python
# Convertendo tupla para lista

cores_lista = list(cores)
cores_lista.append("amarelo")
cores = tuple(cores_lista)
print(cores)  # ('vermelho', 'azul', 'verde', 'amarelo')

```

## 🚀 Exercício Prático - Cadastro de Cliente

```python
# Criando uma tupla vazia para armazenar informações do cliente
cliente = ()

# Convertendo para lista para adicionar informações
cliente_lista = list(cliente)
cliente_lista.append("Nome: Gabrielle")
cliente_lista.append("Idade: 30")
cliente_lista.append("Cidade: Pernambuco")

# Convertendo de volta para tupla
cliente = tuple(cliente_lista)
print(cliente)
```

## 🔹 Mini Introdução a Funções em Python

As **funções** em Python permitem reutilizar código e organizá-lo melhor. São definidas com a palavra-chave `def`.

## 📌 Exemplo de Função com soma()

```python
# Definindo uma função que realiza a soma de dois números
def soma(a, b):
    return a + b

### Chamando a função e imprimindo o resultado
resultado = soma(5, 3)
print(f"A soma é {resultado}")
```





