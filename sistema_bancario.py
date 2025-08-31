
from py_compile import main


def menu():
    menu =  '''\n
    ====Menu da Conta====
    1. Depositar
    2. Sacar
    3. Extrato
    4. Nova Conta
    5. Listar contas
    6. Novo usuario
    7. Sair
    Escolha uma opção:'''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    valor = float(input("Digite o valor a ser depositado: "))
    if valor > 0:
        saldo += valor
        extrato.append(("Deposito: R$", valor))
        print("\n===Depósito realizado com sucesso!===")
    else:
        print("\n@@@Valor inválido para depósito!@@@")

    return saldo, extrato

def sacar(* saldo, valor, extrato, limite, numero_saques, limite_saques):


    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@Saldo insuficiente!@@@")
    elif excedeu_limite:
        print("\n@@@Limite de saque excedido!@@@")
    elif excedeu_saques:
        print("\n@@@Número máximo de saques atingido!@@@")
    elif valor > 0:
        saldo -= valor
        extrato.append(("Saque: R$", valor))
        print("\n===Saque realizado com sucesso!===")
    else:
        print("\n@@@Valor inválido para saque!@@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================EXTRATO================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")   
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            Número da Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 1000)
        print(linha)

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            criar_usuario(usuarios)
        elif opcao == "7":
            print("===Sistema encerrado!===")
            break
        else:
            print("@@@Opção inválida!@@@")


main()
