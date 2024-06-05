import unittest
from note_manager.image_note import ImageNote

class TestImageNote(unittest.TestCase):
    def test_create_image_note(self):
        note = ImageNote("Test Title", "/path/to/image.jpg", ["test"], 1)
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.image_path, "/path/to/image.jpg")
        self.assertEqual(note.tags, ["test"])
        self.assertEqual(note.importance, 1)

    def test_update_image_note(self):
        note = ImageNote("Test Title", "/path/to/image.jpg", ["test"], 1)
        old_updated_at = note.updated_at
        note.update()
        self.assertNotEqual(note.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
