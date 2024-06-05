from .base_note import Note

class TextNote(Note):
    def __init__(self, title: str, content: str, tags: list, importance: int):
        super().__init__(title, tags, importance)
        self.content = content

    def __repr__(self):
        return f"TextNote(title={self.title}, content={self.content}, importance={self.importance}, updated_at={self.updated_at})"
