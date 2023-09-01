# ERICK KUWAHARA DA SILVA
# RM: 550371
# TURMA: 1TDSPN

import os

# ================ SUBALGORITMOS 

def menu() -> None:
    print(f"""
MENU
          
0 - SAIR
1 - Digite um nome completo
2 - Exibe separado o Nome do Sobrenome
3 - Conta quantas palavras há no nome completo
4 - Exibir em formato de bibliografia
""")

nome = ""
def nome_completo() -> str:
    nomeCompleto = input("Digite um nome completo: ")
    return nomeCompleto

def separa_nome_completo(nc: str) -> None:
    if nc == "":
        print("\nPrimeiramente digite um nome na opção 1")
    else:
        nome_separado = nc.split()

        if len(nome_separado) <= 1:
            print("\nNome completo inválido, digite a opção 1 corretamente")
        else:
            nome = nome_separado[0]
            sobrenome = " ".join(nome_separado[1:])
            print(f"\nNome: {nome}")
            print(f"Sobrenome: {sobrenome}")

def conta_palavras(nc: str) -> None:
    if nc == "":
        print("\nPrimeiramente digite um nome na opção 1")
    else:
        numero_palavras = nc.split()
        print(f"\nO nome {nc} tem {len(numero_palavras)} palavras.")

def exibir_forma_bibliografia(nc: str) -> None:
    if nc == "":
        print("\nPrimeiramente digite um nome na opção 1")
    else:
        nome_separado = nc.split()

        if len(nome_separado) <= 1:
            print("\nNome completo inválido, digite a opção 1 corretamente")
        else:
            ultimo_sobrenome = nc.split()[-1]
            nome_separado_sem_ultimo_sobrenome = nc.split()[:-1]

            nome_separado_sem_ultimo_sobrenome = " ".join(nome_separado_sem_ultimo_sobrenome)

            print(f"\n{ultimo_sobrenome.upper()}, {nome_separado_sem_ultimo_sobrenome}")

# ================ PROGRAMA PRINCIPAL

while True:
    os.system("cls")
    menu();
    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            nome = nome_completo()
            input("\nDigite algo para continuar o programa...")
        case 2:
            separa_nome_completo(nome)
            input("\nDigite algo para continuar o programa...")
        case 3:
            conta_palavras(nome)
            input("\nDigite algo para continuar o programa...")
        case 4:
            exibir_forma_bibliografia(nome)
            input("\nDigite algo para continuar o programa...")
        case 0:
            break
        case _:
            print("Opção inválida, digite um item de 0 a 4")
            input("\nDigite algo para continuar o programa...")