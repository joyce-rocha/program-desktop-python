# Gerenciador de Tarefas Simples

# Lista para armazenar tarefas
tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

def menu():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()

"""
Processo de Adaptação e Aprendizado

Atividade: Adaptação do Gerenciador de Tarefas para incluir novas funcionalidades como categorização e prioridade.

Durante o desenvolvimento do projeto, o objetivo principal foi personalizar o gerenciador de tarefas básico, adicionando funcionalidades que o tornassem mais útil e alinhado com os temas discutidos em aula. A prática proporcionou uma oportunidade de consolidar conhecimentos sobre estruturas de dados, controle de fluxo, e boas práticas de programação em Python.

Processo de Adaptação:
Revisão do Código Base:Analisei o código fornecido inicialmente para entender sua estrutura; Identifiquei os pontos onde as novas funcionalidades poderiam ser inseridas sem comprometer o funcionamento básico.

Implementação de Novas Funcionalidades: Cada tarefa passou a ser associada a uma categoria, permitindo melhor organização; Adicionei a funcionalidade de definir a prioridade das tarefas (Alta, Média ou Baixa), permitindo que os usuários atribuam importância a cada item; Substituí a lista simples por uma lista de dicionários, armazenando as tarefas como objetos com chaves (tarefa, categoria, prioridade); Adicionei comentários explicativos em cada função, detalhando o que foi alterado e por quê; Segui o padrão de boas práticas para manter o código limpo e legível.

Testes:
Realizei testes para verificar as novas funcionalidades, incluindo cenários com entradas válidas e inválidas, listas vazias e remoções.
Corrigi problemas menores relacionados a entradas inválidas e tratamento de exceções.


Desafios Enfrentados:
- Estrutura de Dados: O uso de dicionários em uma lista exigiu atenção extra para manipular os dados corretamente.
- Validação de Entradas: Garantir que os usuários inserissem apenas dados válidos (como números inteiros para remoção e strings para categorias/prioridades) foi um desafio superado com condicionais e tratamento de erros.



Aprendizado Adquirido:
- Estruturas de Dados: Aprendi a manipular listas de dicionários para armazenar e exibir informações mais complexas.
- Controle de Fluxo: A implementação do menu e das validações reforçou meu entendimento sobre loops e condicionais.
- Boas Práticas de Programação: Entendi a importância de organizar o código com funções específicas, adicionar comentários claros e escrever código legível.
- Testes: Compreendi como o teste iterativo é essencial para identificar e corrigir problemas antes da entrega final.



Conclusão:
Este projeto foi uma experiência enriquecedora, permitindo não apenas consolidar habilidades em Python, mas também desenvolver a capacidade de adaptar um código existente para atender a novos requisitos. As melhorias adicionaram funcionalidade e tornaram o gerenciador mais prático para uso cotidiano.

Com esse aprendizado, sinto-me mais preparada para enfrentar desafios futuros no desenvolvimento de software, especialmente em projetos que exigem personalização e escalabilidade.
"""
