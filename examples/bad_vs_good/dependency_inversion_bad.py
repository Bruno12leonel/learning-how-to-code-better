class StudyTopicReader:
    def load(self):
        return [
            {"name": "Meaningful names", "category": "clean_code"},
            {"name": "Single responsibility", "category": "solid"},
        ]


class StudyReportService:
    def __init__(self):
        self.reader = StudyTopicReader()

    def build_report(self):
        topics = self.reader.load()
        topic_names = [topic["name"] for topic in topics]
        return ", ".join(topic_names)
