from .base_note import Note

class ImageNote(Note):
    def __init__(self, title: str, image_path: str, tags: list, importance: int):
        super().__init__(title, tags, importance)
        self.image_path = image_path

    def __repr__(self):
        return f"ImageNote(title={self.title}, image_path={self.image_path}, importance={self.importance}, updated_at={self.updated_at})"
