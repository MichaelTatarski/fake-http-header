from importlib.resources import read_text

from fake_http_header.data_import import load_dict

domain_to_search_engine_binary = read_text("fake_http_header.data", "top-level-domain-to-search-engines.json")
domain_to_languages_binary = read_text("fake_http_header.data", "top-level-domain-to-languages.json")
browser_to_user_agent = read_text("fake_http_header.data", "browser-to-user-agent.json")
encoding_values_dict_binary = read_text("fake_http_header.data", "encoding-values.json")
browser_to_accept_value_binary = read_text("fake_http_header.data", "browser-to-accept-values.json")

MINIMAL_GENERIC_TOP_LEVEL_DOMAIN_LENGTH = 3
MINIMAL_ENCODING_VALUE_LENGTH = 1
MAXIMUM_ENCODING_VALUE_LENGTH = 5

# Dicts that are extracted from json files

DOMAIN_TO_SEARCH_ENGINES = load_dict(domain_to_search_engine_binary)
DOMAIN_TO_LANGUAGES = load_dict(domain_to_languages_binary)
BROWSER_TO_USER_AGENT = load_dict(browser_to_user_agent)
encoding_values_dict = load_dict(encoding_values_dict_binary)
BROWSER_TO_ACCEPT_VALUES = load_dict(browser_to_accept_value_binary)
ENCODING_VALUES = encoding_values_dict["Accept-Encoding"]

# addidtional constants to to create country and browser specific

BROWSERS = list(BROWSER_TO_USER_AGENT.keys())
ALL_TOP_LEVEL_DOMAINS = list(DOMAIN_TO_SEARCH_ENGINES.keys())
GENERIC_TOP_LEVEL_DOMAINS = [
    generic_domain
    for generic_domain in ALL_TOP_LEVEL_DOMAINS
    if len(generic_domain) >= MINIMAL_GENERIC_TOP_LEVEL_DOMAIN_LENGTH
]
COUNTRY_TOP_LEVEL_DOMAINS = [country for country in ALL_TOP_LEVEL_DOMAINS if country not in GENERIC_TOP_LEVEL_DOMAINS]
