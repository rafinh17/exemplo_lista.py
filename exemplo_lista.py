nomes = ["Joaquim", "Maria", "Ana"]

print(nomes[0]) #Joaquim
print(nomes[1])
print(nomes[2])

nomes[0] = "Joao" # estava Joaquim

print(nomes[0])  # alterado para Joao 
print(nomes[1])
print(nomes[2])

nomes.append("joao")
nomes.append("joana")
print(nomes)

print(nomes[0])  # alterado para Joao 
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])

nomes.insert(0, "fernanda") # Insere "Fernanda" na posiçao 0
print("apos insert:", nomes)

# Modificando elementos 
nomes[1] = "Paulo" # Modifica elemento no indice 1
print("apos modificacao:", nomes)

# Remova elementos 
del nomes[2] # Remove o elemento no indice 2
print("apos del:", nomes)

nomes.remove("Paulo") # Remove a primeira ocorrencia de "Paulo"
print("Apos remove:", nomes)

removido = nomes.pop(1) # Remove e retorna o elemento no indice 1
print(f"Apos pop (removido '{removido}'):", nomes)

nomes.clear() # Esvazia a lista
print("Apos clear:", nomes)