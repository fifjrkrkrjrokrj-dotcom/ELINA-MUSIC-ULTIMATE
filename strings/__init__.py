import os
from typing import List

import yaml

languages = {}
languages_present = {}


class SafeDict(dict):
    def __getitem__(self, item):
        if item in self:
            return super().__getitem__(item)
        if "en" in languages and item in languages["en"]:
            return languages["en"][item]
        return str(item)


def get_string(lang: str):
    if lang not in languages:
        lang = "en"
    return languages[lang]


for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        raw_en = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages["en"] = SafeDict(raw_en)
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        raw_lang = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        languages[language_name] = SafeDict(raw_lang)
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()
