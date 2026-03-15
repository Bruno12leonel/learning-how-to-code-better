def count_clean_code_topics(topics):
    clean_code_topic_count = 0

    for topic in topics:
        if topic["category"] == "clean_code":
            clean_code_topic_count += 1

    return {
        "count": clean_code_topic_count,
        "status": "topics_found" if clean_code_topic_count > 0 else "no_topics_found",
    }
