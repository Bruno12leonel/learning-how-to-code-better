from src.core.study_catalog import build_default_catalog_service


def lookup_study_topic(topic: str) -> dict[str, str]:
    """Busca um topico de estudo e retorna um resumo curto com referencia."""

    catalog_service = build_default_catalog_service()
    return catalog_service.build_study_response(topic)
