from datetime import datetime
import uuid

class Note:
    def __init__(self, title: str, tags: list, importance: int):
        self.id = str(uuid.uuid4())
        self.title = title
        self.tags = tags
        self.importance = importance
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self):
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"Note(title={self.title}, importance={self.importance}, updated_at={self.updated_at})"
