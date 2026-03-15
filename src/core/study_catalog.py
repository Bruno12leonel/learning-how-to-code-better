from collections.abc import Sequence

from .contracts import StudyContentProvider
from .models import StudyTopic


class InMemoryStudyContentProvider:
    """Mantem os topicos iniciais em memoria para o MVP."""

    def __init__(self) -> None:
        self._topics = (
            StudyTopic(
                name="Meaningful names",
                category="clean_code",
                summary=(
                    "Use nomes que mostrem intencao e reduzam a necessidade de comentarios."
                ),
                example_path="examples/bad_vs_good/meaningful_names_good.py",
            ),
            StudyTopic(
                name="Single responsibility",
                category="solid",
                summary=(
                    "Cada funcao, modulo ou classe deve ter um motivo principal para mudar."
                ),
                example_path="examples/bad_vs_good/single_responsibility_good.py",
            ),
            StudyTopic(
                name="Dependency inversion",
                category="solid",
                summary=(
                    "Servicos importantes devem depender de abstracoes, nao de detalhes concretos."
                ),
                example_path="examples/bad_vs_good/dependency_inversion_good.py",
            ),
        )

    def list_topics(self) -> Sequence[StudyTopic]:
        return self._topics


class StudyCatalogService:
    """Centraliza a busca e a explicacao dos topicos de estudo."""

    def __init__(self, content_provider: StudyContentProvider) -> None:
        self._content_provider = content_provider

    def find_topic(self, query: str) -> StudyTopic | None:
        normalized_query = self._normalize(query)

        for topic in self._content_provider.list_topics():
            topic_name = self._normalize(topic.name)
            topic_category = self._normalize(topic.category)

            if normalized_query in topic_name or normalized_query in topic_category:
                return topic

        return None

    def build_study_response(self, query: str) -> dict[str, str]:
        topic = self.find_topic(query)

        if topic is None:
            return {
                "status": "not_found",
                "message": (
                    "Nao encontrei esse topico ainda. Tente algo como "
                    "'meaningful names', 'single responsibility' ou 'dependency inversion'."
                ),
            }

        return {
            "status": "success",
            "topic": topic.name,
            "category": topic.category,
            "summary": topic.summary,
            "example_path": topic.example_path,
        }

    @staticmethod
    def _normalize(value: str) -> str:
        return value.strip().lower().replace("-", " ").replace("_", " ")


def build_default_catalog_service() -> StudyCatalogService:
    return StudyCatalogService(content_provider=InMemoryStudyContentProvider())
