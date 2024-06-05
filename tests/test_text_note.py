import unittest
from note_manager.text_note import TextNote

class TestTextNote(unittest.TestCase):
    def test_create_text_note(self):
        note = TextNote("Test Title", "Test Content", ["test"], 1)
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.content, "Test Content")
        self.assertEqual(note.tags, ["test"])
        self.assertEqual(note.importance, 1)

if __name__ == '__main__':
    unittest.main()
