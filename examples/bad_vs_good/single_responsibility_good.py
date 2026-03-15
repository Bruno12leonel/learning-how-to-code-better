def normalize_topic_name(topic_name):
    normalized_name = topic_name.strip().title()

    if not normalized_name:
        raise ValueError("Topic name is required.")

    return normalized_name


def build_topic_record(topic_name, category):
    return {
        "topic_name": normalize_topic_name(topic_name),
        "category": category.lower(),
    }


def format_topic_record(record):
    return f'{record["topic_name"]},{record["category"]}\n'


def save_topic_record(record, file_path):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(format_topic_record(record))


def register_study_topic(topic_name, category, file_path):
    record = build_topic_record(topic_name, category)
    save_topic_record(record, file_path)
    return f'Saved topic "{record["topic_name"]}"'
