def register_study_topic(topic_name, category):
    normalized_name = topic_name.strip().title()

    if not normalized_name:
        raise ValueError("Topic name is required.")

    record = {
        "topic_name": normalized_name,
        "category": category.lower(),
    }

    line = f'{record["topic_name"]},{record["category"]}\n'

    with open("topics.txt", "a", encoding="utf-8") as file:
        file.write(line)

    return f'Saved topic "{record["topic_name"]}"'
