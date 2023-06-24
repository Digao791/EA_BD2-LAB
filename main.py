# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
from CRUD import festa
from database import Database

db = Database("bolt://localhost:7687", "neo4j", "senha123")

# Criando uma instância da classe Family para interagir com o banco de dados

clube = festa(db)

print("Seja bem vindo ao Club Penguin !!!!")
print("Aposto que sentiu saudades, para isso vamos fazer uma grande festa !!!!")
print("")

print("Precisamos criar a nossa lista de convidados, vale lembrar que eles irão trazer seus Puffles")

while True:
    print("Quem você quer convidar para a festa ?")
    print("Preciso saber o nome, idade, cor, e a sua faixa do Card-Jutsu")

    nome = input("Nome: ")
    idade = int(input("idade :"))
    cor = input("Cor: ")
    faixa = input("Faixa do card-jutsu: ")

    clube.create_penguin(nome, idade, cor, faixa)

    print("Ele tem Puffles ? S-SIM N-NAO")

    res = input()

    if res == "S":
        print("Quantos Puffles ele tem ?")
        qnt = int(input())
        for i in range(qnt):
            nome_p = input("Nome do Puffle: ")
            cor_p = input("Cor do Puffle: ")
            tempo = int(input("Cuida a quanto tempo do Puffle: "))

            clube.create_puffle(nome_p, cor_p)
            clube.create_relation_with_puffle(nome, idade, cor, faixa, nome_p, cor_p, tempo)

    print("Temos mais convidados ? S-SIM N-NAO")

    res = input()

    if res == 'N':
        break

print("Vamos verificar nossos convidados ?")


print("Quem é amigo de quem na nossa lista de convidados ?")

while True:
    nome1 = input("Nome1: ").split()
    nome2 = input("Nome2: ").split()
    clube.create_relation_with_penguin(nome1,nome2)
    print("Mais relacionamentos de pinguin a fazer ? S-SIM N-NAO")
    res = input()
    if res == 'N':
        break

print("Deseja fazer alguma alteração na lista ? S-SIM N-NAO")
res = input()
if res == 'S':
    while True:
        print("O que deseja fazer ? 1 - Verificar Convidado, 2 - Verificar relacionamento, 3 - Verificar Puffles ")
        res = int(input())
        if res == 1:
            nome = input("Qual o nome do convidado a verificar ? : ")
            clube.show_convidado(nome)


        elif res == 2:
            print("Qual o tipo de relacionamento que deseja verificar ?")
            print("1 - AMIGO_DE, 2 - DONO_DE, 3")
            res = int(input())
            if res == 1:
                print("Qual propriedade deseja usar 1 - Nome, 2 - Idade, 3 - Cor, 4 - Faixa, 5 - Quantidade de Puffles, 6 - Nenhuma)")
                res = int(input())
                propriedade = ["nome", "idade", "cor", "faixa"]
                if res == 5:
                    qnt = int(input("Digite a quantidade de puffles que esse convidado tem : "))
                    clube.show_relation(None, qnt, "DONO_DE", 5)
                elif res == 6:
                        clube.show_relation(None, None, "AMIGO_DE", 6)
                else:
                    valor = input("Digite o valor da propriedade escolhida: ")
                    clube.show_relation(propriedade[res - 1], valor, "AMIGO_DE", res)

            elif res == 2:
                print("Qual propriedade deseja usar 1 - Nome, 2 - Cor, 3 - Nome do Dono, 4 - Nenhuma")
                res = int(input())
                propriedade = ["nome", "cor"]
                if res == 3:
                    nome = input("Nome do dono: ")
                    clube.show_puffles_relations(None, nome,None, 3)
                elif res == 4:
                    clube.show_puffles_relations(None, None, None, 4)
                else:
                    valor = input("Informe o valor da propriedade escolhida: ")
                    clube.show_puffles_relations(propriedade[res - 1], valor, "DONO_DE", res)
        else:
            print("Qual propriedade deseja verificar do puffle ? Nome ou Cor ?")
            propriedade = input()
            valor = input("Digite o valor dessa propriedade: ")
            clube.show_puffle(propriedade, valor)

        print("Deseja concluir a verificação da lista de convidados ? S-SIM N-NAO")
        res = input()
        if res == 'S':
            break



