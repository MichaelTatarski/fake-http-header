import re
import unittest

from fake_http_header.constants import COUNTRY_TOP_LEVEL_DOMAINS, DOMAIN_TO_LANGUAGES
from fake_http_header.util import _generate_accept_language


class TestGenerateAcceptLanguage(unittest.TestCase):

    def test_valid_country_domain(self):
        """
        Test that _generate_accept_language returns valid languages for each country domain.
        Ensures that the result is not empty and that all languages in the result are valid
        for the given domain.
        """
        for domain_name in COUNTRY_TOP_LEVEL_DOMAINS:
            with self.subTest(domain=domain_name):
                result = _generate_accept_language(domain_name)
                self.assertTrue(result)
                languages = [lang.split(";")[0] for lang in result.split(",")]
                for lang in languages:
                    self.assertIn(lang.strip(), DOMAIN_TO_LANGUAGES[domain_name] + ["*"])

    def test_non_empty_string(self):
        """
        Test that _generate_accept_language returns a non-empty string for a generic domain.
        """
        domain_name = "org"
        result = _generate_accept_language(domain_name)
        self.assertTrue(result)

    def test_valid_language_codes(self):
        """
        Test that _generate_accept_language returns valid language codes for a given domain.
        Ensures that the language codes match the expected pattern.
        """
        domain_name = "net"
        result = _generate_accept_language(domain_name)
        languages = [lang.split(";")[0] for lang in result.split(",")]
        pattern = re.compile(r"^[a-z]{2,3}(-[A-Z]{2})?$")
        for lang in languages:
            if lang.strip() != "*":
                self.assertTrue(pattern.match(lang.strip()))


if __name__ == "__main__":
    unittest.main()
