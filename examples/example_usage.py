from note_manager.note_manager import NoteManager
from note_manager.text_note import TextNote
from note_manager.list_note import ListNote
from note_manager.image_note import ImageNote
from datetime import datetime

note_manager = NoteManager()
note_manager.add_note(TextNote("Shopping List", "Buy milk and eggs", ["shopping", "errands"], 2))
note_manager.add_note(ListNote("Project Tasks", ["Setup environment", "Write code", "Test features"], ["work", "project"], 3))
note_manager.add_note(ImageNote("Vacation Photo", "/images/vacation.jpg", ["vacation", "photo"], 1))

# Пошук нотатків
print(note_manager.find_notes(keyword="Project"))
print(note_manager.find_notes(date_range=(datetime(2023, 1, 1), datetime(2024, 1, 1))))
print(note_manager.find_notes(tags=["shopping"]))

# Сортування нотатків
print(note_manager.sort_notes(by="time"))
print(note_manager.sort_notes(by="importance"))
print(note_manager.sort_notes(by="title"))
