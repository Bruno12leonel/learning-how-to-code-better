from src.core.study_explainer import build_default_study_explainer


def test_build_explanation_for_known_topic():
    explainer = build_default_study_explainer()

    explanation = explainer.build_explanation("meaningful names")

    assert "Topico: Meaningful names" in explanation
    assert "Exemplo recomendado" in explanation


def test_build_explanation_for_unknown_topic():
    explainer = build_default_study_explainer()

    explanation = explainer.build_explanation("open closed")

    assert "Ainda nao consigo aprofundar esse topico" in explanation
