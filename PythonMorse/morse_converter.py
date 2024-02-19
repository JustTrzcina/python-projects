from typing import TypedDict,List

MORSE_CODE = {
    'a': '.-', 
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

class MorseDict(TypedDict):
    letter:str
    morse_combination:str

class MorseConverter():
    def __init__(self,conversion_table:MorseDict) -> None:
        self.conversion_table = conversion_table
        self.inverted_table = {v: k for k, v in MORSE_CODE.items()}


    def _parse_file(self,path)-> List[str]:
        with open(path,mode='r') as f:
            text_data = f.readlines()
        words = []
        for line in text_data:
            words.extend(line.strip().split())
        return words
    
    def from_letters(self,path):
        words = self._parse_file(path)
        results=[]
        for word in words:
            morse_word=[]
            for letter in word:
                morse_word.append(self.conversion_table.get(letter.lower(),'_'))
            morse_string = ' '.join(morse_word)
            results.append(morse_string)
        final_string = (' / '.join(results))
        with open('result.txt','w') as f:
            f.write(final_string)

    def from_morse(self,morse_code):
        return ''.join(self.inverted_table.get(code, '') for code in morse_code.split())


converter = MorseConverter(MORSE_CODE)
converter.from_letters('sample.txt')
print(converter.from_morse('.-.. --- -. --. / ... . -. - . -. -.-. .'))