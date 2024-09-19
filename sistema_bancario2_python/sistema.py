from datetime import datetime

# Dados
usuarios = []
contas = []
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Função para cadastrar usuário
def cadastrar_usuario():
    cpf = input("Digite o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: CPF já cadastrado!")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número da residência: ")
    cidade = input("Digite a cidade: ")
    
    data_hora_cadastro = datetime.now().strftime('%d/%m/%Y %H:%M:%S')  # Captura a data e hora do cadastro
    
    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "cidade": cidade
        },
        "data_hora_cadastro": data_hora_cadastro  # Armazena a data e hora do cadastro
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para listar usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for usuario in usuarios:
        print(f"CPF: {usuario['cpf']}, Nome: {usuario['nome']}, Data de Nascimento: {usuario['data_nascimento']}")
        endereco = usuario['endereco']
        print(f"Endereço: {endereco['logradouro']}, {endereco['numero']}, {endereco['cidade']}")
        print(f"Data e hora do cadastro: {usuario['data_hora_cadastro']}")
        print("-------------------------------------------")

# Função para registrar transações no extrato
def registrar_transacao(tipo, valor):
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    extrato.append(f"{data_hora} - {tipo}: R${valor:.2f}")

# Função para depósito
def depositar():
    global saldo
    valor = float(input("Digite o valor do depósito: "))
    saldo += valor
    registrar_transacao("Depósito", valor)
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    print(f"Saldo atual: R${saldo:.2f}")

# Função para saque
def sacar():
    global saldo, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários atingido.")
        return

    valor = float(input("Digite o valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print(f"O valor máximo para saque é de R${limite:.2f}")
    else:
        saldo -= valor
        numero_saques += 1
        registrar_transacao("Saque", valor)
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        print(f"Saldo atual: R${saldo:.2f}")

# Função para exibir extrato
def exibir_extrato():
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\n========== EXTRATO ==========")
        for transacao in extrato:
            print(transacao)
        print(f"Saldo atual: R${saldo:.2f}")
        print("=============================\n")

# Função principal - menu
def menu():
    opcao = """
    [c] Cadastrar Usuário
    [l] Listar Usuários
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    while True:
        escolha = input(opcao)

        if escolha == "c":
            cadastrar_usuario()
        elif escolha == "l":
            listar_usuarios()
        elif escolha == "d":
            depositar()
        elif escolha == "s":
            sacar()
        elif escolha == "e":
            exibir_extrato()
        elif escolha == "q":
            print("Saindo do sistema bancário...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o menu
menu()
