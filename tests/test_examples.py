from examples.bad_vs_good.meaningful_names_good import count_clean_code_topics


def test_meaningful_names_example_counts_clean_code_topics():
    topics = [
        {"category": "clean_code"},
        {"category": "solid"},
        {"category": "clean_code"},
    ]

    result = count_clean_code_topics(topics)

    assert result == {
        "count": 2,
        "status": "topics_found",
    }
