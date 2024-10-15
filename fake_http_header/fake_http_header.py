import random
from dataclasses import dataclass

from fake_http_header.constants import (
    BROWSER_TO_ACCEPT_VALUES,
    BROWSER_TO_USER_AGENT,
    BROWSERS,
    COUNTRY_TOP_LEVEL_DOMAINS,
)
from fake_http_header.util import (
    _generate_accept_encoding,
    _generate_accept_language,
    _generate_referer_site,
)


@dataclass
class FakeHttpHeader:
    """
    A class to generate fake HTTP headers.

    Attributes:
        user_agent (str): The user agent string representing the browser.
        accept_language (str): The accepted languages for the HTTP header.
        accept_encoding (str): The accepted encodings for the HTTP header.
        accept (str): The accepted content types for the HTTP header.
        referer (str): The referer URL for the HTTP header.
    """

    user_agent: str
    accept_language: str
    accept_encoding: str
    accept: str
    referer: str

    def __init__(
        self,
        browser: str = random.choice(BROWSERS),
        domain_code: str = random.choice(COUNTRY_TOP_LEVEL_DOMAINS),
        referer: str = None,
    ):
        """Initializer for a FakeHttpHeader object

        Args:
            :browser (str, optional): Specifies of which browser type the user agent
            should be (for instance 'chrome' or 'firefox').
            :domain_code (str, optional): Specifies, which domain code the referer site should have.
            This arguments has also impact on the generated accept language field.
            :referer (str, optional): Specifies the referer URL for the HTTP header. If not provided,
            it will be randomly generated based on the domain_code.
        """

        self.user_agent = random.choice(BROWSER_TO_USER_AGENT[browser])
        self.accept_language = _generate_accept_language(domain_code)
        self.accept_encoding = _generate_accept_encoding()
        self.accept = BROWSER_TO_ACCEPT_VALUES[browser]
        self.referer = referer if referer else _generate_referer_site(domain_code)

    def as_header_dict(self) -> dict:
        """transform a FakeHttpHeader object into a dict representation that is compatible to the requests library

        Returns:
            dict: A dict representation of the FakeHttpHeader object
        """
        dict_rep = {
            "User-Agent": self.user_agent,
            "Accept-language": self.accept_language,
            "Accept-encoding": self.accept_encoding,
            "Accept": self.accept,
            "Referer": self.referer,
        }
        return dict_rep
