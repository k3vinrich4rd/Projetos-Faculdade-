Aluno = input("Digite o seu nome completo: ")
print()
nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))
nota4 = int(input("Informe a quarta nota: "))

media_das_notas = (nota1 + nota2 + nota3 + nota4) // 4
if media_das_notas >= 6:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado")
print(f'A medida de notas do aluno {Aluno}é: {media_das_notas}.')
