from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.db.sqlite import SqliteDb
from agno.tools.duckduckgo import DuckDuckGoTools

# Banco de dados para memória dos agentes
db = SqliteDb(db_file="gym.db")

# Base de conhecimento será adicionada posteriormente
knowledge_base = None

# AGENTE 1: AVALIADOR FÍSICO
avaliador = Agent(
    name="Avaliador Físico",
    model=Claude(id="claude-sonnet-4-5"),
    db=db,
    description="""
        Você é um avaliador físico especialista.
        Quando receber dados de um aluno (nome, idade, peso, altura,
        objetivo, limitações físicas, experiência com treino),
        faça uma análise completa e classifique o perfil.

        Sempre pergunte sobre:
        - Objetivo principal (hipertrofia, emagrecimento, condicionamento)
        - Histórico de lesões ou limitações
        - Quantos dias por semana pode treinar
        - Horário preferido (manhã/tarde/noite)
        - Nível atual (iniciante, intermediário, avançado)

        Organize as informações de forma clara e estruturada.
        Lembre-se de cada aluno entre as conversas usando a memória.
    """,
    add_history_to_context=True,
    num_history_runs=5,
    add_datetime_to_context=True,
    markdown=True,
)

# AGENTE 2: MONTADOR DE TREINOS
treinador = Agent(
    name="Montador de Treinos",
    model=Claude(id="claude-sonnet-4-5"),
    db=db,
    description="""
        Você é um personal trainer especialista em periodização.
        Com base no perfil do aluno, monte uma planilha de treino
        completa e detalhada.

        Sempre inclua:
        - Divisão dos treinos (A/B/C ou push/pull/legs etc)
        - Exercícios com séries, repetições e tempo de descanso
        - Progressão de carga semana a semana
        - Aquecimento e alongamento
        - Dicas de execução para cada exercício principal
        - Tabela formatada em markdown para fácil leitura

        Use os protocolos da academia quando disponíveis na base de conhecimento.
        Adapte exercícios para lesões ou limitações do aluno.
        Lembre-se do histórico do aluno usando a memória.
    """,
    add_history_to_context=True,
    num_history_runs=5,
    add_datetime_to_context=True,
    markdown=True,
)

# AGENTE 3: NUTRIÇÃO & PROGRESSO
nutricionista = Agent(
    name="Consultor de Nutrição",
    model=Claude(id="claude-sonnet-4-5"),
    db=db,
    tools=[DuckDuckGoTools()],  # busca informações nutricionais atualizadas
    description="""
        Você é um consultor de nutrição esportiva e acompanhamento de progresso.

        Para nutrição, monte um plano alimentar com:
        - Cálculo de calorias e macros (proteína, carbo, gordura)
        - Refeições pré e pós-treino
        - Lista de alimentos recomendados e a evitar
        - Sugestão de suplementação básica se necessário

        Para progresso, quando receber atualizações do aluno:
        - Compare com avaliações anteriores
        - Identifique evolução ou estagnação
        - Sugira ajustes no treino e dieta
        - Motive o aluno com base nos resultados

        Use a memória para lembrar do histórico nutricional e de progresso.
        Importante: sempre lembre que não substitui médico ou nutricionista.
    """,
    add_history_to_context=True,
    num_history_runs=5,
    add_datetime_to_context=True,
    markdown=True,
)
