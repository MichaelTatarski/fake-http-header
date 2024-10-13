import unittest

from fake_http_header import FakeHttpHeader


class TestFakeHttpHeader(unittest.TestCase):

    def test_default_initialization(self):
        header = FakeHttpHeader()
        self.assertIsNotNone(header.user_agent)
        self.assertIsNotNone(header.accept_language)
        self.assertIsNotNone(header.accept_encoding)
        self.assertIsNotNone(header.accept)
        self.assertIsNotNone(header.referer)

    def test_custom_initialization(self):
        header = FakeHttpHeader(browser="chrome", domain_code="de")
        self.assertIn("Chrome", header.user_agent)
        self.assertIn("de", header.accept_language)
        self.assertIn("de", header.referer)

    def test_as_header_dict(self):
        header = FakeHttpHeader(browser="firefox", domain_code="org")
        header_dict = header.as_header_dict()
        self.assertEqual(header_dict["User-Agent"], header.user_agent)
        self.assertEqual(header_dict["Accept-language"], header.accept_language)
        self.assertEqual(header_dict["Accept-encoding"], header.accept_encoding)
        self.assertEqual(header_dict["Accept"], header.accept)
        self.assertEqual(header_dict["Referer"], header.referer)

    def test_custom_referer(self):
        custom_referer = "http://example.com"
        header = FakeHttpHeader(browser="safari", domain_code="uk", referer=custom_referer)
        self.assertIn("Safari", header.user_agent)
        self.assertEqual(header.referer, custom_referer)


if __name__ == "__main__":
    unittest.main()
