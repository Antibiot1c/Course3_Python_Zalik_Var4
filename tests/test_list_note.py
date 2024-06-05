import unittest
from note_manager.list_note import ListNote

class TestListNote(unittest.TestCase):
    def test_create_list_note(self):
        note = ListNote("Test Title", ["item1", "item2"], ["test"], 1)
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.items, ["item1", "item2"])
        self.assertEqual(note.tags, ["test"])
        self.assertEqual(note.importance, 1)

    def test_update_list_note(self):
        note = ListNote("Test Title", ["item1", "item2"], ["test"], 1)
        old_updated_at = note.updated_at
        note.update()
        self.assertNotEqual(note.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
