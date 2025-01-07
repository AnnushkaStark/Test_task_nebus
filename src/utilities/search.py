from transliterate import detect_language, translit
from transliterate.exceptions import LanguageDetectionError


async def get_transliterated_value(query: str) -> str:
    translited_ru = None
    translited_en = None
    result_query = []
    try:
        result_query.append(query)
        query_lang = detect_language(query)
    except LanguageDetectionError:
        pass
    if query_lang == "ru":
        translited_en = translit(query, reversed=True)
        result_query.append(translited_en)
    translited_ru = translit(query, "ru")
    result_query.append(translited_ru)
    return list(set(result_query))
