# Criando um cadastro de cliente utilizando tupla

cliente = () #tupla vazia

cliente = list(cliente) # Convertendo para lista para adicionar dados

# Adicionando as informações 
cliente.append('Lívia') # append: uma manipulação para adicionar em uma lista
cliente.append(987654210)
cliente.append('10/02/2025')

cliente = tuple(cliente) # Convertendo para tupla 

print('\n Dados do cliente cadastrados: ', cliente)

