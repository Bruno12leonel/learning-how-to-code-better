from dataclasses import dataclass


@dataclass(frozen=True)
class StudyTopic:
    name: str
    category: str
    summary: str
    example_path: str
