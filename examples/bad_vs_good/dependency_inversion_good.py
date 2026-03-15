from typing import Protocol


class TopicProvider(Protocol):
    def load(self):
        ...


class InMemoryTopicProvider:
    def load(self):
        return [
            {"name": "Meaningful names", "category": "clean_code"},
            {"name": "Single responsibility", "category": "solid"},
        ]


class StudyReportService:
    def __init__(self, topic_provider: TopicProvider):
        self.topic_provider = topic_provider

    def build_report(self):
        topics = self.topic_provider.load()
        topic_names = [topic["name"] for topic in topics]
        return ", ".join(topic_names)
