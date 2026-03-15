from src.tools.study_lookup import lookup_study_topic


def test_lookup_study_topic_returns_known_topic():
    response = lookup_study_topic("dependency inversion")

    assert response["status"] == "success"
    assert response["topic"] == "Dependency inversion"
    assert response["example_path"].endswith("dependency_inversion_good.py")
