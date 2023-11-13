from argparse import ArgumentParser
from g2pk import G2p

def romanize_korean(text):
    # Mapping of Korean characters to their Romanized equivalents
    # This is a simplified version and might not cover all cases
    mapping = {
        # Consonants (initial)
        "ㄱ": "g",
        "ㄲ": "kk",
        "ㄴ": "n",
        "ㄷ": "d",
        "ㄸ": "tt",
        "ㄹ": "r",
        "ㅁ": "m",
        "ㅂ": "b",
        "ㅃ": "pp",
        "ㅅ": "s",
        "ㅆ": "ss",
        "ㅇ": "",
        "ㅈ": "j",
        "ㅉ": "jj",
        "ㅊ": "ch",
        "ㅋ": "k",
        "ㅌ": "t",
        "ㅍ": "p",
        "ㅎ": "h",
        # Vowels
        "ㅏ": "a",
        "ㅐ": "ae",
        "ㅑ": "ya",
        "ㅒ": "yae",
        "ㅓ": "eo",
        "ㅔ": "e",
        "ㅕ": "yeo",
        "ㅖ": "ye",
        "ㅗ": "o",
        "ㅘ": "wa",
        "ㅙ": "wae",
        "ㅚ": "oe",
        "ㅛ": "yo",
        "ㅜ": "u",
        "ㅝ": "wo",
        "ㅞ": "we",
        "ㅟ": "wi",
        "ㅠ": "yu",
        "ㅡ": "eu",
        "ㅢ": "ui",
        "ㅣ": "i",
        # Consonants (final)
        "ㄱㄱ": "k",
        "ㄱㅅ": "ks",
        "ㄴㅈ": "nj",
        "ㄴㅎ": "nh",
        "ㄹㄱ": "lg",
        "ㄹㅁ": "lm",
        "ㄹㅂ": "lb",
        "ㄹㅅ": "ls",
        "ㄹㅌ": "lt",
        "ㄹㅍ": "lp",
        "ㄹㅎ": "lh",
        "ㅂㅅ": "bs",
        "ㅇㅇ": "ng",
        # ... more combinations as needed
    }

    romanized_text = ""
    for char in text:
        romanized_text += mapping.get(
            char, char
        )  # Default to the character itself if not found in mapping

    return romanized_text


def decompose_hangul(sentence):
    # Hangul Unicode ranges
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

    # Hangul Choseong (initial consonants)
    CHOSUNG_LIST = [
        "ㄱ",
        "ㄲ",
        "ㄴ",
        "ㄷ",
        "ㄸ",
        "ㄹ",
        "ㅁ",
        "ㅂ",
        "ㅃ",
        "ㅅ",
        "ㅆ",
        "ㅇ",
        "ㅈ",
        "ㅉ",
        "ㅊ",
        "ㅋ",
        "ㅌ",
        "ㅍ",
        "ㅎ",
    ]

    # Hangul Jungsung (medial vowels)
    JUNGSUNG_LIST = [
        "ㅏ",
        "ㅐ",
        "ㅑ",
        "ㅒ",
        "ㅓ",
        "ㅔ",
        "ㅕ",
        "ㅖ",
        "ㅗ",
        "ㅘ",
        "ㅙ",
        "ㅚ",
        "ㅛ",
        "ㅜ",
        "ㅝ",
        "ㅞ",
        "ㅟ",
        "ㅠ",
        "ㅡ",
        "ㅢ",
        "ㅣ",
    ]

    # Hangul Jongseong (final consonants)
    JONGSUNG_LIST = [
        "",
        "ㄱ",
        "ㄲ",
        "ㄳ",
        "ㄴ",
        "ㄵ",
        "ㄶ",
        "ㄷ",
        "ㄹ",
        "ㄺ",
        "ㄻ",
        "ㄼ",
        "ㄽ",
        "ㄾ",
        "ㄿ",
        "ㅀ",
        "ㅁ",
        "ㅂ",
        "ㅄ",
        "ㅅ",
        "ㅆ",
        "ㅇ",
        "ㅈ",
        "ㅊ",
        "ㅋ",
        "ㅌ",
        "ㅍ",
        "ㅎ",
    ]

    decomposed_sentence = ""

    for char in sentence:
        if ord(char) >= BASE_CODE and ord(char) <= (BASE_CODE + 11171):
            char_code = ord(char) - BASE_CODE
            choseong = CHOSUNG_LIST[char_code // CHOSUNG]
            jungsung = JUNGSUNG_LIST[(char_code % CHOSUNG) // JUNGSUNG]
            jongsung = JONGSUNG_LIST[char_code % JUNGSUNG]
            decomposed_sentence += choseong + jungsung + jongsung
        else:
            decomposed_sentence += char

    return decomposed_sentence


def convert_to_phonetic(korean_sentence):
    g2p = G2p()
    phonetic_transcription = g2p(korean_sentence)
    return phonetic_transcription

def main():
    parser = ArgumentParser(description="Convert Korean text to phonetic symbols")
    parser.add_argument(
        "sentence", type=str, help="Korean sentence to convert to phonetic symbols"
    )
    try:
        args = parser.parse_args()
        if args.sentence is None:
            parser.print_help()
            raise ValueError
    except:
        parser.print_help()
        exit(0)

    phonetic_symbols = convert_to_phonetic(args.sentence)
    decomposed_sentence = decompose_hangul(phonetic_symbols)
    romanized_sentence = romanize_korean(decomposed_sentence)
    print(phonetic_symbols)
    print(decomposed_sentence)
    print(romanized_sentence)

if __name__ == "__main__":
    main()
