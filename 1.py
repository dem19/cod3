from funcoes import *
from menu import menu

while True:
    menu()
    opcao = int(input(' Escolhar uma opção :  '))

    if opcao == 1:
        matricula = int(input('matricula: '))
        nome = input('Nome: ')
        aprovado = " "
        recuperacao =" "
        reprovado = " "
        matricular(matricula, nome,aprovado,recuperacao,reprovado)
    elif opcao == 2:
        listar_aluno()
    elif opcao == 3:
        listar_aluno_aprovado()
    elif opcao == 4:
        listar_aluno_recuperacao()
    elif opcao == 5:
        listar_aluno_reprovado()
    elif opcao == 6:
        matricula = int(input('Digite a matricula: '))
        buscar_por_matricula(matricula)
    elif opcao == 7:
        matricula = int(input('Digite a matricula: '))
        excluir(matricula)
    elif opcao == 8:
        matricula = int(input('matricula: '))
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        Lancar_notas(matricula, nota1, nota2,media)
    elif opcao == 9:
        listar_notas()
    elif opcao == 10:
        matricula = int(input('Digite a matricula: '))
        excluir_notas(matricula)
    elif opcao == 11:
        matricula = int(input(("Digite a matricula do aluno referido:")))
        verificar_situacao_aluno(matricula)
    elif opcao==12:
        matricula = int(input('Digite a matricula: '))
        aprovado,reprovado,recuperacao = verificar_media(aprovado,reprovado,)
        atualizar_matricula(aprovado,recuperacao,reprovado)
    elif opcao == 13:
        exit()