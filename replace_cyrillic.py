import pandas as pd


def ru_to_en(text):
    # Таблица соответствий русских букв английским символам
    mapping = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'YO', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
        'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    result = []
    for char in text:
        if char in mapping:
            result.append(mapping.get(char))
        else:
            result.append(char)
    return ''.join(result)


def replace_cyrillic(dataframe):
    """
    Функция заменяет все русские символы в каждом значении DataFrame на аналоги английского алфавита.
    Возвращает измененный DataFrame.
    """
    df_copy = dataframe.copy()
    for col in df_copy.columns:
        df_copy[col] = df_copy[col].apply(lambda x: ru_to_en(str(x)))
    return df_copy


# Пример использования:
data = {'Имя': ['Иван', 'Петя'], 'Город': ['Москва', 'Санкт-Петербург']}
df = pd.DataFrame(data)
result_df = replace_cyrillic(df)
print(result_df)