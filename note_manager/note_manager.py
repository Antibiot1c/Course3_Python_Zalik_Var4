from .text_note import TextNote
from .list_note import ListNote
from .image_note import ImageNote

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def find_notes(self, keyword: str = None, date_range: tuple = None, tags: list = None):
        results = self.notes

        if keyword:
            results = [note for note in results if keyword.lower() in note.title.lower() or (hasattr(note, 'content') and keyword.lower() in note.content.lower())]

        if date_range:
            start_date, end_date = date_range
            results = [note for note in results if start_date <= note.updated_at <= end_date]

        if tags:
            results = [note for note in results if any(tag in note.tags for tag in tags)]

        return results

    def sort_notes(self, by: str):
        if by == 'time':
            return sorted(self.notes, key=lambda note: note.updated_at, reverse=True)
        elif by == 'importance':
            return sorted(self.notes, key=lambda note: note.importance, reverse=True)
        elif by == 'title':
            return sorted(self.notes, key=lambda note: note.title)
        else:
            return self.notes

    def __repr__(self):
        return f"NoteManager(notes={self.notes})"
