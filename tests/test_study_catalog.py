from src.core.models import StudyTopic
from src.core.study_catalog import StudyCatalogService


class FakeStudyContentProvider:
    def list_topics(self):
        return [
            StudyTopic(
                name="Meaningful names",
                category="clean_code",
                summary="Use nomes claros.",
                example_path="examples/bad_vs_good/meaningful_names_good.py",
            )
        ]


def test_find_topic_by_name():
    service = StudyCatalogService(content_provider=FakeStudyContentProvider())

    topic = service.find_topic("meaningful")

    assert topic is not None
    assert topic.name == "Meaningful names"


def test_build_study_response_returns_not_found_message():
    service = StudyCatalogService(content_provider=FakeStudyContentProvider())

    response = service.build_study_response("open closed")

    assert response["status"] == "not_found"
    assert "Nao encontrei" in response["message"]
