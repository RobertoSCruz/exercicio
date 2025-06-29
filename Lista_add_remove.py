nome = []

novo_nome_1 = input ("Adicione um novo nome:")
novo_nome_2 = input ("Adicione um novo nome:")
novo_nome_3 = input ("Adicione um novo nome:")
novo_nome_4 = input ("Adicione um novo nome:")
novo_nome_5 = input ("Adicione um novo nome:")
novo_nome_6 = input ("Adicione um novo nome:")

nome.append (novo_nome_1)
nome.append (novo_nome_2)
nome.append (novo_nome_3)
nome.append (novo_nome_4)
nome.append (novo_nome_5)
nome.append (novo_nome_6)


print (nome)

apagar_nome = input ("Qual nome deseja apagar? :")

nome.remove (apagar_nome)

print (nome)