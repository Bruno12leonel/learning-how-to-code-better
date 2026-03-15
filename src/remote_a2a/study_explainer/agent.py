import os

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.apps import A2AFastAPIApplication
from a2a.server.events import EventQueue, InMemoryQueueManager
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from a2a.utils import new_agent_text_message

from src.core.study_explainer import StudyConceptExplainer, build_default_study_explainer


class StudyConceptAgentExecutor(AgentExecutor):
    """Conecta o protocolo A2A ao servico de explicacao do dominio."""

    def __init__(self, explainer: StudyConceptExplainer) -> None:
        self._explainer = explainer

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        explanation = self._explainer.build_explanation(context.get_user_input())

        await event_queue.enqueue_event(
            new_agent_text_message(
                explanation,
                context_id=context.context_id,
                task_id=context.task_id,
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise RuntimeError("Cancelamento ainda nao suportado neste agente educacional.")


def build_agent_card() -> AgentCard:
    base_url = os.getenv("STUDY_EXPLAINER_A2A_URL", "http://localhost:8001")

    return AgentCard(
        name="study_explainer_agent",
        description="Agente remoto especializado em explicar conceitos de Clean Code e SOLID.",
        url=base_url,
        version="0.1.0",
        capabilities=AgentCapabilities(streaming=False),
        defaultInputModes=["text/plain"],
        defaultOutputModes=["text/plain"],
        skills=[
            AgentSkill(
                id="explain_clean_code_and_solid",
                name="Explain Clean Code and SOLID",
                description=(
                    "Explica meaningful names, single responsibility e dependency inversion "
                    "com foco educacional e referencia de exemplos locais."
                ),
                tags=["education", "clean-code", "solid", "python"],
            )
        ],
        supportsAuthenticatedExtendedCard=False,
    )


def build_app():
    request_handler = DefaultRequestHandler(
        agent_executor=StudyConceptAgentExecutor(build_default_study_explainer()),
        task_store=InMemoryTaskStore(),
        queue_manager=InMemoryQueueManager(),
    )

    server = A2AFastAPIApplication(
        agent_card=build_agent_card(),
        http_handler=request_handler,
    )
    return server.build()


app = build_app()
