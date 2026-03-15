from .study_catalog import StudyCatalogService, build_default_catalog_service


class StudyConceptExplainer:
    """Gera explicacoes mais profundas a partir do catalogo de estudo."""

    def __init__(self, catalog_service: StudyCatalogService) -> None:
        self._catalog_service = catalog_service

    def build_explanation(self, query: str) -> str:
        topic_response = self._catalog_service.build_study_response(query)

        if topic_response["status"] != "success":
            return (
                "Ainda nao consigo aprofundar esse topico. "
                "Tente pedir uma explicacao sobre meaningful names, "
                "single responsibility ou dependency inversion."
            )

        topic_name = topic_response["topic"]
        summary = topic_response["summary"]
        example_path = topic_response["example_path"]
        detailed_explanation = self._build_detailed_explanation(topic_name)

        return (
            f"Topico: {topic_name}\n"
            f"Resumo: {summary}\n"
            f"Por que isso importa: {detailed_explanation}\n"
            "Como praticar: leia o exemplo indicado, compare a versao ruim e a boa, "
            "e tente explicar em voz alta qual responsabilidade foi isolada.\n"
            f"Exemplo recomendado: {example_path}"
        )

    @staticmethod
    def _build_detailed_explanation(topic_name: str) -> str:
        detailed_explanations = {
            "Meaningful names": (
                "bons nomes reduzem carga cognitiva e fazem o leitor entender o codigo "
                "sem precisar traduzir siglas vagas ou adivinhar intencao"
            ),
            "Single responsibility": (
                "quando cada unidade faz uma coisa principal, mudancas futuras ficam "
                "mais localizadas e os testes ficam mais simples"
            ),
            "Dependency inversion": (
                "depender de abstracoes evita que regras importantes fiquem presas "
                "a detalhes concretos, o que melhora manutencao e testabilidade"
            ),
        }

        return detailed_explanations.get(
            topic_name,
            "esse conceito ajuda a tornar o sistema mais legivel, flexivel e previsivel.",
        )


def build_default_study_explainer() -> StudyConceptExplainer:
    return StudyConceptExplainer(catalog_service=build_default_catalog_service())
