MORSE_CODE_DICT = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",   
}


def decode(encoded_message):
    words = encoded_message.split("/")
    decoded_message = ""
    for word in words:
        decoded_word = MORSE_CODE_DICT.get(word, "?")
        print(f"{word} => {decoded_word}")
        decoded_message += decoded_word
    return decoded_message


if __name__ == "__main__":
    encoded_message = "..-./.-../.-/--./----.--/-../...--/..-./-.-./-.../..-./.----/--.../..-./----./...--/----./----./...../-----/....-/-----.-"
    original_message = decode(encoded_message)
    print(original_message.lower())
