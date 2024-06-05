import unittest
from datetime import datetime, timedelta
from note_manager.note_manager import NoteManager
from note_manager.text_note import TextNote
from note_manager.list_note import ListNote
from note_manager.image_note import ImageNote

class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.note_manager = NoteManager()
        self.text_note = TextNote("Test Title", "Test Content", ["test"], 1)
        self.list_note = ListNote("Test List", ["item1", "item2"], ["test"], 2)
        self.image_note = ImageNote("Test Image", "/path/to/image.jpg", ["test"], 3)
        self.note_manager.add_note(self.text_note)
        self.note_manager.add_note(self.list_note)
        self.note_manager.add_note(self.image_note)

    def test_add_note(self):
        note = TextNote("Another Title", "Another Content", ["another"], 2)
        self.note_manager.add_note(note)
        self.assertIn(note, self.note_manager.notes)

    def test_find_notes_by_keyword(self):
        results = self.note_manager.find_notes(keyword="Test")
        self.assertIn(self.text_note, results)
        self.assertIn(self.list_note, results)
        self.assertIn(self.image_note, results)

    def test_find_notes_by_date_range(self):
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=1)
        results = self.note_manager.find_notes(date_range=(start_date, end_date))
        self.assertIn(self.text_note, results)
        self.assertIn(self.list_note, results)
        self.assertIn(self.image_note, results)

    def test_find_notes_by_tags(self):
        results = self.note_manager.find_notes(tags=["test"])
        self.assertIn(self.text_note, results)
        self.assertIn(self.list_note, results)
        self.assertIn(self.image_note, results)

    def test_sort_notes_by_time(self):
        self.text_note.update()
        sorted_notes = self.note_manager.sort_notes(by="time")
        self.assertEqual(sorted_notes[0], self.text_note)

    def test_sort_notes_by_importance(self):
        sorted_notes = self.note_manager.sort_notes(by="importance")
        self.assertEqual(sorted_notes[0], self.image_note)

    def test_sort_notes_by_title(self):
        sorted_notes = self.note_manager.sort_notes(by="title")
        self.assertEqual(sorted_notes[0], self.image_note)

if __name__ == '__main__':
    unittest.main()
