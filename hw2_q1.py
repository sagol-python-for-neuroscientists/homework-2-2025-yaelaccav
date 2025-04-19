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

def english_to_morse(
    input_file: str = "homework-2-2025-yaelaccav/lorem.txt",
    output_file: str = "lorem_morse.txt"
) -> None:
    """
    Converts the contents of a text file to Morse code and writes it to a new file.

    Parameters
    ----------
    input_file : str
        Path to the input file containing English text.
    output_file : str
        Path where the converted Morse code output will be saved.

    Notes
    -----
    - Each word in the input will appear on a new line in the output file.
    - Characters not found in the MORSE_CODE dictionary are ignored.
    - Conversion uses str methods for efficiency (no explicit character looping).
    """
    # Read text from the input file
    with open(input_file, "r") as file:
        text = file.read()
       


          # Split by line breaks but keep them using a capturing group
    final_words = [
        word
        for part in re.split(r'(\n)', text)
        for word in ([part] if part == '\n' else part.split())
    ]

    # Convert words to Morse (empty string for '\n' to create a blank line)
    morse_words = [
        ' '.join(MORSE_CODE.get(c.upper(), '') for c in word) if word != '\n' else ''
        for word in final_words
    ]



    # Write output
    with open(output_file, "w") as file:
        file.write('\n'.join(morse_words))

if __name__ == "__main__":
    input_path = "homework-2-2025-yaelaccav/lorem.txt"
    output_path = "homework-2-2025-yaelaccav/lorem_morse.txt"
    result = english_to_morse(input_path, output_path)
    print("Question 1 solution: Morse code file written to", output_path)