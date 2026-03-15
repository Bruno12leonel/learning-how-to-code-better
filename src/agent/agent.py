from google.adk.agents import Agent

from src.tools.study_lookup import lookup_study_topic


root_agent = Agent(
    name="study_clean_code_agent",
    model="gemini-2.0-flash",
    description="Agente educacional para estudar Clean Code e SOLID.",
    instruction=(
        "Voce ajuda a estudar Clean Code e SOLID. "
        "Sempre use a tool 'lookup_study_topic' quando o usuario pedir um conceito, "
        "um resumo ou um exemplo. "
        "Se a tool retornar um exemplo, cite o caminho do arquivo para o aluno continuar estudando."
    ),
    tools=[lookup_study_topic],
)
