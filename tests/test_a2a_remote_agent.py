from src.remote_a2a.study_explainer.agent import build_agent_card


def test_build_agent_card_uses_expected_name():
    agent_card = build_agent_card()

    assert agent_card.name == "study_explainer_agent"
    assert str(agent_card.url).startswith("http://")
