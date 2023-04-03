class Locadora():
     
    def __init__(self):
        self.ListaCliente = []
        self.ListaCarro = []
        self.AluguelCarro = []
        self.menu()

    def dados_cliente_aluguel(self):
        self.rg = input('Informe o RG: ')
        self.nome = input('Informe o nome: ')
        Locadora.alugar_carro(self)

    def alugar_carro(self):
        aluguel = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg,
            'categoria': self.categoria,
            'transmissao': self.tpo_transmissao,
            'combustivel': self.tpo_combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'aluguel': self.aluguel,
            'ano': self.ano,
            'placa': self.placa
        }
        self.AluguelCarro.append(aluguel)
        print("O carro foi alugado com sucesso")
        print(self.AluguelCarro)

    def menu(self):
        while True:
            print('-' * 45)
            print("Bem Vindo a locadora LOCACARRO")
            print('-' * 45)
            print("1) Cadastrar um novo veículo")
            print("2) Cadastrar um novo cliente")
            print("3) Realizar a locação de um veículo")
            print("4) Relatório de locação")
            print("5) Encerrar o programa")

            escolha = int(input('\nSelecione uma das opções acima: '))

            if escolha == 1:
                Carro.novo_carro(self)
 
            elif escolha == 2:
                Cliente.novo_cliente(self)
 
            elif escolha == 3:
                Locadora.dados_cliente_aluguel(self)
 
            elif escolha == 4:
                Locadora.alugar_carro(self)

            elif escolha == 5:
                print("\nO progama foi encerrado.")
                break

            else:
                print("\nOpção inválida!\n")

class Carro(Locadora):

    def __init__(self, categoria, tpo_transmissao, tpo_combustivel, marca, modelo, ano, placa):
        self.categoria = categoria
        self.tpo_transmissao = tpo_transmissao
        self.tpo_combustivel = tpo_combustivel
        self.marca = marca
        self.modelo = modelo
        self.ano = ano   
        self.placa = placa    
    
    def novo_carro(self):
        self.categoria = input('Informe a categoria do veículo: ')
        self.tpo_transmissao = input('Informe o tipo de transmissao: ')
        self.tpo_combustivel = input('Infome o tipo de combustível: ')
        self.marca = input('Informe a marca: ')
        self.modelo = input('Informe o modelo: ')
        self.ano = int(input('Informe o ano: '))
        self.placa = input('Informe a placa: ')
        carro = {
            'categoria': self.categoria,
            'transmissao': self.tpo_transmissao,
            'combustivel': self.tpo_combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'placa': self.placa
        }
        self.ListaCarro.append(carro)
        print(self.ListaCarro)

class Cliente(Locadora):
 
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def novo_cliente(self):
        self.cpf = input('Informe o CPF do cliente: ')
        self.nome = input('Informe o nome do cliente: ')
        self.rg = input('Informe o RG do cliente: ')
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }
        self.ListaCliente.append(usuario)
        print(self.ListaCliente)
 
Locadora()

 