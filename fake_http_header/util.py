from fake_http_header.constants import (
    DOMAIN_TO_SEARCH_ENGINES,
    GENERIC_TOP_LEVEL_DOMAINS,
    ENCODING_VALUES,
    MINIMAL_ENCODING_VALUE_LENGTH,
    MAXIMUM_ENCODING_VALUE_LENGTH,
    COUNTRY_TOP_LEVEL_DOMAINS,
    DOMAIN_TO_LANGUAGES,
)
import random


def _generate_referer_site(domain_name: str) -> str:
    if domain_name in DOMAIN_TO_SEARCH_ENGINES.keys():
        return random.choice(DOMAIN_TO_SEARCH_ENGINES[domain_name])
    else:
        random_generic_domain = random.choice(GENERIC_TOP_LEVEL_DOMAINS)
        return random.choice(DOMAIN_TO_SEARCH_ENGINES[random_generic_domain])


def _generate_accept_encoding() -> str:
    encoding_values_array = random.choices(
        ENCODING_VALUES,
        k=random.randint(MINIMAL_ENCODING_VALUE_LENGTH, MAXIMUM_ENCODING_VALUE_LENGTH),
    )
    encoding_values_array_unique = set(encoding_values_array)
    return ",".join(
        [str(encoding_value) for encoding_value in encoding_values_array_unique]
    )


def _generate_accept_language(domain_name) -> str:
    if domain_name in COUNTRY_TOP_LEVEL_DOMAINS:
        return random.choice(DOMAIN_TO_LANGUAGES[domain_name])
    else:
        random_domain = random.choice(COUNTRY_TOP_LEVEL_DOMAINS)
        return random.choice(DOMAIN_TO_SEARCH_ENGINES[random_domain])
