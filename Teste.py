nomes = ["Wagner" , "Raquel", "Karina", "César", "Douglas", "Rodrigo", "Ricardo"]
nome_pesquisado = input ("Me informe o nome e te informarei se existe ou não na lista: ")

try:
    index_nome = nomes.index(nome_pesquisado)
    print("O Nome existe certinho")

except Exception:
    print("Deu erro, o nome não existe na lista")