import unittest
from datetime import datetime
from note_manager.base_note import Note

class TestBaseNote(unittest.TestCase):
    def test_create_note(self):
        note = Note("Test Title", ["test"], 1)
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.tags, ["test"])
        self.assertEqual(note.importance, 1)
        self.assertIsInstance(note.created_at, datetime)
        self.assertIsInstance(note.updated_at, datetime)

    def test_update_note(self):
        note = Note("Test Title", ["test"], 1)
        old_updated_at = note.updated_at
        note.update()
        self.assertNotEqual(note.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
