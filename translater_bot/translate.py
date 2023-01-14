from googletrans import Translator
from translatepy.models import TranslationResult

def translater(text: str, language: str='en') -> TranslationResult:
    translator = Translator()
    result = translator.translate(text, language)
    return result



print(translater('Самолет', 'en'))
