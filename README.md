# sistemaBancario_com_python
 Criando um Sistema Bancário com Python

# Sistema Bancário

Este projeto consiste em um sistema bancário simples desenvolvido em Python, onde é possível cadastrar usuários, gerenciar contas e realizar transações financeiras. O sistema foi criado com o objetivo de aplicar e reforçar conceitos fundamentais de programação, como estruturas de controle, funções, manipulação de dados e boas práticas de desenvolvimento.

## Funcionalidades
Cadastro de Usuários

O sistema permite o cadastro de usuários contendo as seguintes informações:

CPF (único e não repetido)

Nome completo

Data de nascimento

Endereço completo (logradouro, número, cidade)

Cada usuário pode ter uma ou mais contas associadas.


## Operações Bancárias

**Depósito**: Os usuários podem realizar depósitos em suas contas. A data e hora da transação são registradas automaticamente.

**Saque**: Saques podem ser efetuados, respeitando o saldo disponível na conta e um limite de três saques diários.

**Extrato**: Exibe o histórico de transações realizadas, incluindo depósitos e saques, com o valor, data e hora de cada operação.

## Listagem de Contas

O sistema permite listar todas as contas cadastradas, exibindo informações sobre os titulares e suas respectivas contas.

**Organização do Código**

O sistema foi implementado de maneira modular, utilizando funções para separar as responsabilidades e facilitar a manutenção e expansão futura. As principais funções são:

cadastrar_usuario(): Responsável por criar um novo usuário.

cadastrar_conta(): Cria uma nova conta para um usuário existente.

realizar_deposito(): Função para realizar depósitos em uma conta.

realizar_saque(): Função que processa saques, com verificações de saldo e limite de saques diários.

exibir_extrato(): Exibe o extrato de todas as transações de uma conta.

listar_contas(): Exibe a lista de todas as contas cadastradas no sistema.

## Tecnologias Utilizadas

**Linguagem**: Python 3.x

**Bibliotecas**: Nenhuma biblioteca externa foi utilizada, o projeto usa apenas recursos nativos do Python.

**Persistência de Dados**: O armazenamento dos dados é feito em memória durante a execução do programa, ou seja, os dados são voláteis e não persistem após o encerramento da execução.
