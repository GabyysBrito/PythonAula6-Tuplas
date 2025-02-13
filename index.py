# =========================================================================================

# Tuplas 
# --> São uma estrutura exclusiva do python, que guardam uma quantidade quase infinita de informação, porém essas informações são imutáveis

# =========================================================================================

#imutáveis : guardam informações que não mudam
# usam () parênteses

# devedores = ('Waldecy', 'Vagner', 'Jakeline', 'Luciana', 'Emanuelle', 'Gabrielle')

# print(devedores[0])

#--------------------------------

# Não irá funcionar!
# devedores[1] = 'Ezequiel'

#--------------------------------

# Tupla vazia
# pessoas = ()

# Exiba no terminal o tipo de variável
# print(type(pessoas))

# pessoas será convertida em uma lista e será modificada
# pessoas = list(pessoas)

# exiba no terminal o novo tipo após a conversação 
# print(type(pessoas))

# Adicionando informaçoes à lista

# pessoas.append('Douglas')
# pessoas.append(1234567890)
# pessoas.append(987654321)
# print(f'Aqui o tipo é {type(pessoas)}')

# Convertendo de volta para tupla

# pessoas = tuple(pessoas)
# print('Tupla modificada', pessoas)
#print('Tipo final: ', type(pessoas)) # saída <class 'tuple'>

#---------------------------------------------------

# Criando uma tupla vazia e adicionando um valor

data = ()
data = list(data)
data.append('Qualquer coisa')
data = tuple(data)

print("Dados armazenados na tupla:", data)   

# =========================================================================================

# Início de função
# Funções 
# --> São blocos de código que executam tarefas específicas e podem ser reutilizados.

# =========================================================================================

# Exemplo de operações matemáticas

print('Operções matemáticas simples: ')
print(123454 + 948392)
print(23432 - 897)

# Exemplo de função simples de soma

def soma():
    return 1 + 1

print(soma())