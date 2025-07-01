funcionario=[{
    "Nome":"Alex",
    "Idade":"26",
    "Profissão":"Cafetão"},
    {
        "Nome":"Rafa",
        "Idade":"19",
        "Profissão":"Amor da minha vida"},
    {
        "Nome":"Thay",
        "Idade":"25",
        "Profissão":"Advogata"}]

print(funcionario)

nome_funcionario=input("Nome do Colaborador:")
idade_funcionario= int(input("Idade do Colaborador:"))
profissao_funcionario=input("Profissão do Colaborador:")

funcionario.append ({
    "Nome:": nome_funcionario,
    "Idade:": idade_funcionario,
    "Profissão:": profissao_funcionario
})

print(funcionario)
