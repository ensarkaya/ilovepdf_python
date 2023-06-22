import os
import unittest
from src.api import OfficeToPdfConverter


class TestPdfConverter(unittest.TestCase):
    def setUp(self):
        self.converter = OfficeToPdfConverter(
            "project_public_94b7107f154eade9ddf9d619cd3d8355_m8cuo86a581730c5087ed729eb48a7f3a1504",
            "secret_key_6420af3ae87f5ba120c9d507d4282954_gk2Bu129ba2afe63ddfde5b7e53ca51c062db",
        )

    def test_get_auth_token(self):
        token = self.converter.get_auth_token()
        self.assertIsInstance(token, str)

    def test_start_task(self):
        server, task = self.converter.start_task("officepdf")
        self.assertIsInstance(server, str)
        self.assertIsInstance(task, str)

    def test_upload_file(self):
        # Assuming you have a test file at 'test.docx'
        server, task = self.converter.start_task("officepdf")
        server_filename = self.converter.upload_file(server, task, "tests/test.docx")
        self.assertIsInstance(server_filename, str)

    def test_full_usage(self):
        # Assuming you have a test file at 'tests/test.docx'
        self.converter.convert_to_pdf("tests/test.docx", "output.pdf")
        # Check that the output file exists
        self.assertTrue(os.path.exists("output.pdf"))


if __name__ == "__main__":
    unittest.main()
