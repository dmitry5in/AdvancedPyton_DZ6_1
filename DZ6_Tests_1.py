from unittest import TestCase
import app


class TestApp(TestCase):

    def test_show_document_info(self):
        for document in app.documents:
            self.assertIsInstance(app.show_document_info(document), str)

    def test_add_new_doc(self):
        self.assertEqual(app.add_new_doc('123', 'passport', 'Иван Иванов', '3'), '3')

    def test_delete_doc(self):
        self.assertEqual(app.delete_doc('11-2'), ('11-2', True))


