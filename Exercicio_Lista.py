funcionario = ["Alex","Rafa","Jao","Xande","Roberto","Mark","Pedro"]
print(funcionario)

funcionario_procurado = input("Digite o Funcionario que deseja procurar:")
posicao = funcionario.index (funcionario_procurado) +1
print("Vendedor:" + str(funcionario_procurado)  + "\nSua localização é:" + str(posicao))