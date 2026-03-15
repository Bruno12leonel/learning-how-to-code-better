from collections.abc import Sequence
from typing import Protocol

from .models import StudyTopic


class StudyContentProvider(Protocol):
    """Define o contrato minimo para obter topicos de estudo."""

    def list_topics(self) -> Sequence[StudyTopic]:
        """Retorna os topicos disponiveis para consulta."""
