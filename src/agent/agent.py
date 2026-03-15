import os

from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

from src.tools.study_lookup import lookup_study_topic


remote_study_explainer = RemoteA2aAgent(
    name="remote_study_explainer",
    description="Agente remoto A2A para explicacoes mais aprofundadas sobre Clean Code e SOLID.",
    agent_card=os.getenv(
        "STUDY_EXPLAINER_AGENT_CARD_URL",
        "http://localhost:8001/.well-known/agent-card.json",
    ),
)


root_agent = Agent(
    name="study_clean_code_agent",
    model="gemini-2.0-flash",
    description="Agente educacional para estudar Clean Code e SOLID.",
    instruction=(
        "Voce ajuda a estudar Clean Code e SOLID. "
        "Sempre use a tool 'lookup_study_topic' quando o usuario pedir um conceito, "
        "um resumo ou um exemplo. "
        "Se o usuario pedir uma explicacao mais profunda, comparacoes ou orientacao de estudo, "
        "delegue para o agente remoto 'remote_study_explainer'. "
        "Se a tool retornar um exemplo, cite o caminho do arquivo para o aluno continuar estudando."
    ),
    tools=[lookup_study_topic],
    sub_agents=[remote_study_explainer],
)
