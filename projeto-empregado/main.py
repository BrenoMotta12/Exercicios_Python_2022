from classes import Desenvolvedor, GerenteProjeto

breno = Desenvolvedor(
    nome_completo='Breno da Motta',
    email='brenomotta0012@gmail.com',
    matricula_funcional='001',
    salario=2500,
    linguagens_programacao=['java', 'c++', 'python'])

joao = Desenvolvedor(
    nome_completo='Joao marcos miguel',
    email='jmdadz7@gmail.com',
    matricula_funcional='002',
    salario=2700,
    linguagens_programacao=['COBOL', 'Assembly', 'Fortan'])

nicolas = GerenteProjeto(
    nome_completo='Nicolas Lage',
    email='nicolaslage@gmail.com',
    matricula_funcional='003',
    salario=5000,
    time=[joao, breno],
    projetos_envolvidos=['empregados', 'automovel'])

# Breno, João e Nicolas iniciam sua Jornada!
breno.iniciar_jornada()
nicolas.iniciar_jornada()
joao.iniciar_jornada()

# Breno e João aprendem novas linguagens
breno.adicionar_linguagem('C#')
joao.adicionar_linguagem('Lisp')

# Nicolas começa a participar de mais um projeto e recebe um aumento salarial
nicolas.participar_projeto('IBGE')
nicolas.receber_aumento()

# João é removido da equipe do Nicolas
nicolas.remover_desenvolvedor(joao)

# Breno fica sobrecarregado e acaba tomando café demais...
breno.beber_cafe(2.5)
# Resultando em um Burnout!!!
