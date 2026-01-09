from django.test import TestCase
from .models import Note

class NoteModelTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")

    def test_note_string_representation(self):
        self.assertEqual(str(self.note), "Test Note")