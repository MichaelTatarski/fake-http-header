import random
from dataclasses import dataclass
from fake_http_header.data import *
from fake_http_header.constants import (
    BROWSERS,
    COUNTRY_TOP_LEVEL_DOMAINS,
    BROWSER_TO_USER_AGENT,
    BROWSER_TO_ACCEPT_VALUES,
)
from fake_http_header.util import (
    _generate_accept_language,
    _generate_accept_encoding,
    _generate_referer_site,
)


@dataclass
class FakeHttpHeader:
    user_agent: str
    accept_language: str
    accept_encoding: str
    accept: str
    referer: str

    def __init__(
        self,
        browser: str = random.choice(BROWSERS),
        domain_name: str = random.choice(COUNTRY_TOP_LEVEL_DOMAINS),
    ):
        """Initializer for a FakeHttpHeader object

        Args:
            browser (str, optional): Specifies of which browser type the user agent
            should be (for instance chrome or firefox). Defaults to random.choice(BROWSERS).
            domain_name (str, optional): Specifies, which domain name the referer site should have.
            This arguments has also impact on the generated accept language field. Defaults to
            random.choice(COUNTRY_TOP_LEVEL_DOMAINS).
        """
        self.user_agent = random.choice(BROWSER_TO_USER_AGENT[browser])
        self.accept_language = _generate_accept_language(domain_name)
        self.accept_encoding = _generate_accept_encoding()
        self.accept = BROWSER_TO_ACCEPT_VALUES[browser]
        self.referer = _generate_referer_site(domain_name)

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
