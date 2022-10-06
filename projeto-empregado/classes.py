from datetime import datetime


class Empregado:
    numero_empregados = 0

    # Construtor da classe Empregado
    def __init__(self, nome_completo: str, email: str, matricula_funcional: str, salario: int):
        Empregado.numero_empregados += 1  # Incrementa o numero de empregados da empresa
        self.nome_completo = nome_completo
        self.email = email
        self.matricula_funcional = matricula_funcional
        self.salario = salario

    def iniciar_jornada(self):
        print(f'O empregado {self.matricula_funcional} {self.nome_completo} iniciou sua jornada as {datetime.now()}')

    def finalizar_jornada(self):
        print(f'O empregado {self.matricula_funcional} {self.nome_completo} encerrou sua jornada as {datetime.now()}')

    def receber_aumento(self):
        raise NotImplementedError

# CLASSE DESENVOLVEDOR ------------------------------------------------------------------------------------------------


class Desenvolvedor(Empregado):
    porcentagem_aumento = 1.05

    # Contrutor da classe Desenvolvedor
    def __init__(self, nome_completo: str, email: str,
                 matricula_funcional: str, salario: int,
                 linguagens_programacao: list, litros_cafe: float = 0,
                 burnout: bool = False):
        # Chamando contrutor da classe superior (Empregado)
        super(Desenvolvedor, self).__init__(nome_completo, email, matricula_funcional, salario)
        self.linguagens_programacao = linguagens_programacao
        self.litros_cafe = litros_cafe
        self.burnout = burnout

    # Metodo para adicionar linguagem a lista de linguagens do programador
    def adicionar_linguagem(self, nova_linguagem: str):
        self.linguagens_programacao.append(nova_linguagem)
        print(f'A linguagem {nova_linguagem} foi adicionada a lista de linguagens do programador {self.nome_completo}')

    def beber_cafe(self, quantidade_cafe: float):
        self.litros_cafe += quantidade_cafe
        if self.litros_cafe > 2.:
            self.burnout = True
            print(f"O desenvolvedor {self.nome_completo} esta em burnout 😵😵")

    # Metodo abstrato herdado da classe superior // aumenta o salario baseado na variavel porcentagem_aumento
    def receber_aumento(self):
        print(f'Salario do programador {self.nome_completo} aumentado de R${self.salario:.2f}', end=' ')
        self.salario = self.salario * self.porcentagem_aumento
        print(f'para R${self.salario:.2f}')

# CLASSE GERENTE DE PROJETO --------------------------------------------------------------------------------------


class GerenteProjeto(Empregado):
    porcentagem_aumento = 1.12

    # Contrutor da classe GerenteProjeto
    def __init__(self, nome_completo: str, email: str,
                 matricula_funcional: str, salario,
                 time: list, projetos_envolvidos: list):
        # Chamando contrutor da classe superior (Empregado)
        super(GerenteProjeto, self).__init__(nome_completo, email, matricula_funcional, salario)
        self.time = time
        self.projetos_envolvidos = projetos_envolvidos

    # Metodo para adicionar um desenvolvedor ao time
    def adicionar_desenvolvedor(self, dev: Desenvolvedor):
        self.time.append(dev)
        print(f'Desenvolvedor {dev.nome_completo} adicionado ao time do gerente de projeto {self.nome_completo}')

    # Metodo para remover um desenvolvedor do time
    def remover_desenvolvedor(self, dev: Desenvolvedor):
        self.time.remove(dev)
        print(f'O desenvolvedor {dev.nome_completo} foi removido do time do gerente de projeto {self.nome_completo}')

    # Metodo para adicionar um projeto a lista de projetos do gerente
    def participar_projeto(self, proj: str):
        self.projetos_envolvidos.append(proj)
        print(f'{self.nome_completo} agora participa do projeto {proj}')

    # Metodo para remover um projeto a lista de projetos do gerente
    def sair_projeto(self, proj: str):
        self.projetos_envolvidos.remove(proj)
        print(f'{self.nome_completo} agora não participa mais do projeto {proj}')

    # Metodo abstrato herdado da classe superior // aumenta o salario baseado na variavel porcentagem_aumento
    def receber_aumento(self):
        print(f'Salario do programador {self.nome_completo} aumentado de R${self.salario:.2f}', end=' ')
        self.salario = self.salario * self.porcentagem_aumento
        print(f'para R${self.salario:.2f}')
