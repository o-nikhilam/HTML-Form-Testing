import unittest
from pathlib import Path
from html.parser import HTMLParser


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)
        elif tag == "input":
            self.inputs.append(attrs)
        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        file_path = Path(__file__).parent / "index.html"
        cls.parser = FormParser()

        with open(file_path, encoding="utf-8") as file:
            cls.parser.feed(file.read())

    def test_form_exists(self):
        self.assertTrue(
            len(self.parser.forms) > 0,
            "Form is missing"
        )

    def test_name_field(self):
        self.assertTrue(
            any(field.get("name") == "name" for field in self.parser.inputs),
            "Name field is missing"
        )

    def test_email_field(self):
        self.assertTrue(
            any(field.get("name") == "email" for field in self.parser.inputs),
            "Email field is missing"
        )

    def test_contact_field(self):
        self.assertTrue(
            any(field.get("name") == "contact" for field in self.parser.inputs),
            "Contact Number field is missing"
        )

    def test_submit_button(self):
        self.assertTrue(
            any(button.get("type") == "submit" for button in self.parser.buttons),
            "Submit button is missing"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
