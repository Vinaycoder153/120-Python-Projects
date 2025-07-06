import asyncio
from googletrans import Translator

translator = Translator()

language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "la": "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

allow = True  # variable to control correct language code input

while allow:  # checking if language code is valid

    user_code = input(
        f"Please input desired language code. To see the language code list enter 'options' \n"
    ).strip().lower()

    if user_code == "options":  # showing language options
        print("Code : Language")  # Heading of language option menu
        for code, lang in language.items():
            print(f"{code} => {lang}")
        print()  # adding an empty space

    elif user_code in language:
        print(f"You have selected {language[user_code]}")
        allow = False
    else:
        print("It's not a valid language code!")

async def translate_loop():
    while True:  # starting translation loop
        string = input(
            "\nWrite the text you want to translate: \nTo exit the program write 'close'\n"
        )

        if string.strip().lower() == "close":  # exit program command
            print(f"\nHave a nice Day!")
            break

        # translating method from googletrans
        try:
            translated = await translator.translate(string, dest=user_code)
        except Exception as e:
            print(f"Translation failed: {e}")
            continue

        # printing translation
        print(f"\n{language[user_code]} translation: {translated.text}")
        # printing pronunciation (may be None)
        print(f"Pronunciation : {translated.pronunciation if translated.pronunciation else 'N/A'}")

        # checking if the source language is listed on language dict and printing it
        src_lang = language.get(translated.src, translated.src)
        print(f"Translated from : {src_lang}")

if __name__ == "__main__":
    asyncio.run(translate_loop())
