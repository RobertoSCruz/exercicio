carros = ["L200","HB20","Civic","Polo","Clio","Voyage","Renegade","Toro","Compass"]

#Maneira mais elaborada pra obter o ultimo item

tamanho_da_lista = len(carros)
index_ultimo_item = tamanho_da_lista -1
ultimo_item = carros[index_ultimo_item]
print(ultimo_item)

#Maneira Simples para obter o ultimo item

ultimo_item_simples = carros[-1]
print(ultimo_item_simples)

#Obter o penultimo item 

ultimo_item_simples = carros[-2]
print(ultimo_item_simples)

#Obter Sublista a partir de Lista
tres_ultimos_carros = carros[6:]
print(tres_ultimos_carros)

tres_primeiros_carros = carros[:3]
print(tres_primeiros_carros)
