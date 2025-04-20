import re

MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', ':': '---...',
    "'": '.----.', '-': '-....-',
}

def english_to_morse(input_file: str = "lorem.txt", output_file: str = "lorem_morse.txt") -> None:
    with open(input_file, "r") as file:
        text = file.read()

    # Replace paragraph breaks (\n\n or more) with a unique marker
    text_with_markers = re.sub(r'\n\s*\n+', ' <<PARA>> ', text)

    # Split text into words and markers
    words_and_paragraphs = text_with_markers.split()

    # Convert each word to Morse or marker to empty line
    morse_lines = [
        ''.join(MORSE_CODE.get(char.upper(), '') for char in word)
        if word != '<<PARA>>' else ''
        for word in words_and_paragraphs
    ]

    with open(output_file, "w") as file:
        file.write('\n'.join(morse_lines))

if __name__ == "__main__":
    input_path = "lorem.txt"
    output_path = "lorem_morse.txt"
    english_to_morse(input_path, output_path)
    print("Question 1 solution: Morse code file written to", output_path)
