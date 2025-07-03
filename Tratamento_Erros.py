nomes =["Alex","Rafael","Thay","BabyGirl","Barbie","Advogata"]
nome_pesquisado = input("Digite o nome que deseja procurar: ")

try:
    index_nome = nomes.index(nome_pesquisado)
    print("O Nome Existe")

except Exception:
    print("O Nome Não existe")