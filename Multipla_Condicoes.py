nfs = [ "1356","4568","3072","9014","0702","1702","0404"]
pesquisar_nota = input ("Qual nota deseja pesquisar? ")

posicao = nfs.index(pesquisar_nota)

if posicao == 0 :
    print("É a Primeira nota")
    
elif posicao == 1 :
    print("É a Segunda nota")
    
elif posicao == 2 :
    print("É a Terceira nota")
    
elif posicao == 3 :
    print("É a Quarta nota")
    
elif posicao == 4 :
    print("É a Quinta nota")
    
elif posicao == 5 :
    print("É a Sexta nota")
    
elif posicao == 6 :
    print("É a Setima nota")

else:
    print("Essa Nota não existe")

    