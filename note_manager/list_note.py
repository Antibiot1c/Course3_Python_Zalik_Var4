from .base_note import Note

class ListNote(Note):
    def __init__(self, title: str, items: list, tags: list, importance: int):
        super().__init__(title, tags, importance)
        self.items = items

    def __repr__(self):
        return f"ListNote(title={self.title}, items={self.items}, importance={self.importance}, updated_at={self.updated_at})"
