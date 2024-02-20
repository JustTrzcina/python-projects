from typing import TypedDict,List
from os import path

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
    'z': '--..',
    ' ': '/'
}

class MorseDict(TypedDict):
    letter:str
    morse_combination:str

class MorseConverter():
    def __init__(self,conversion_table:MorseDict) -> None:
        self.conversion_table = conversion_table
        self.inverted_table = {v: k for k, v in MORSE_CODE.items()}
        self.user_functions={'a':self.from_letters,'b':self.from_morse}
        self.menu_text='Select the type of conversion:\na) To morse\nb) To text\nq) To quit\nEnter "a","b" or "q": '

    def _parse_file(self,path)-> List[str]:
        with open(path,mode='r') as f:
            text_data = f.readlines()
        words = []
        for line in text_data:
            words.extend(line.split())
        return words
    
    def from_letters(self,path):
        words = self._parse_file(path)
        results=[]
        for word in words:
            morse_word=[]
            for letter in word:
                morse_word.append(self.conversion_table.get(letter.lower(),'?'))
            morse_string = ' '.join(morse_word)
            results.append(morse_string)
        final_string = (' / '.join(results))
        with open('result_morse.txt','w') as f:
            f.write(final_string)

    def from_morse(self,path):
        words = self._parse_file(path)
        final_string =  ''.join(self.inverted_table.get(code, '?') for code in words)
        with open('result_text.txt','w') as f:
            f.write(final_string)

    def morse_run(self):
        
        user_input = input(self.menu_text)
        while user_input!='q':
            if user_input in self.user_functions:
                operation = self.user_functions[user_input]
                user_path = input('Specify the file path: ')
                if not path.isfile(user_path):
                    print(f'{user_path} does not exist')
                else:
                    try:
                        operation(user_path)
                    except Exception as e:
                        print(f'An error occured during conversion:{e}')
                    print('Conversion successful')
                    operation(user_path)
            else:
                print('Invalid command')
            user_input = input(self.menu_text)

if __name__ =='__main__':
    converter = MorseConverter(MORSE_CODE)
    val = converter.morse_run()
