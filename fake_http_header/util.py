import random

from fake_http_header.constants import (
    COUNTRY_TOP_LEVEL_DOMAINS,
    DOMAIN_TO_LANGUAGES,
    DOMAIN_TO_SEARCH_ENGINES,
    ENCODING_VALUES,
    GENERIC_TOP_LEVEL_DOMAINS,
    MAXIMUM_ENCODING_VALUE_LENGTH,
    MINIMAL_ENCODING_VALUE_LENGTH,
)


def _generate_referer_site(domain_code: str) -> str:
    if domain_code in DOMAIN_TO_SEARCH_ENGINES.keys():
        return random.choice(DOMAIN_TO_SEARCH_ENGINES[domain_code])
    else:
        random_generic_domain = random.choice(GENERIC_TOP_LEVEL_DOMAINS)
        return random.choice(DOMAIN_TO_SEARCH_ENGINES[random_generic_domain])


def _generate_accept_encoding() -> str:
    encoding_values_array = random.choices(
        ENCODING_VALUES,
        k=random.randint(MINIMAL_ENCODING_VALUE_LENGTH, MAXIMUM_ENCODING_VALUE_LENGTH),
    )
    encoding_values_array_unique = set(encoding_values_array)
    return ",".join([str(encoding_value) for encoding_value in encoding_values_array_unique])


def _generate_accept_language(domain_code) -> str:
    if domain_code in COUNTRY_TOP_LEVEL_DOMAINS:
        primary_language = _get_primary_language(domain_code)
        additional_languages = _get_additional_languages(domain_code, primary_language)
        return _combine_languages(primary_language, additional_languages)
    else:
        return _handle_unknown_domain()


def _get_primary_language(domain_code):
    return random.choice(DOMAIN_TO_LANGUAGES[domain_code])


def _get_additional_languages(domain_code, primary_language):
    available_languages = [lang for lang in DOMAIN_TO_LANGUAGES[domain_code] if lang != primary_language]
    if not available_languages:
        return []
    additional_languages = [
        f"{lang};q={q:.1f}"
        for lang, q in zip(
            random.sample(available_languages, k=random.randint(1, len(available_languages))), [0.9, 0.8, 0.7]
        )
    ]
    return additional_languages


def _combine_languages(primary_language, additional_languages):
    if random.random() < 0.5 and additional_languages:  # 50% chance to add additional languages
        return f"{primary_language}," + ",".join(additional_languages) + ",*;q=0.5"
    else:
        return f"{primary_language}"


def _handle_unknown_domain():
    random_domain = random.choice(COUNTRY_TOP_LEVEL_DOMAINS)
    primary_language = random.choice(DOMAIN_TO_LANGUAGES[random_domain])
    return f"{primary_language},*;q=0.5"
