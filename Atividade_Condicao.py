nome =["Alex","Rafael","Thay","BabyGirl","Barbie","Advogata"]

procurar_nome = input("Digite o nome que deseja procurar:")


if  procurar_nome in nome:
    print("O Nome: " + str(procurar_nome) + " Está na Lista")

else:
    print("O Nome: " + str(procurar_nome) + " Não Está na Lista")