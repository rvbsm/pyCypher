from .types.string import ascii_letters, ascii_lowercase, ascii_uppercase, \
                        cyrillic_letters, cyrillic_lowercase, cyrillic_uppercase, \
                        punctuation

import random

class Encoder:
    def __init__(self):
        with open("english.txt", "r") as file:
            self.dictionary = file.read().splitlines()
    
    def Caesar(
        self, 
        text: str = None, 
        shift: int = 3,
        ignore_case: bool = False
        ) -> str:
        """
        Encrypting text with Caesar cipher (Shift)
        
        Parameters
        ----------
        text : str
            The text to be encrypted
        shift : int
            Shift amount (default is 3)
        ignore_case: bool
            When true - all characters be uppercase

        Returns
        -------
        str
            Encrypted text
        """
        if not text:
            raise TypeError("text must be str, not " + type(text))
        
        if ignore_case:
            text = text.upper()
        
        result = ''
        for char in text:
            if not char.isalpha():
                result += char
                continue
            
            if char not in (ascii_letters + cyrillic_letters):
                raise ValueError("Supported only ASCII and Cyrillic letters")

            if char.isupper():
                if char in ascii_letters:
                    new_char = ascii_uppercase.index(char) + shift
                    new_char = new_char % 26 + 26
                if char in cyrillic_letters:
                    new_char = cyrillic_uppercase.index(char) + shift
                    new_char = new_char % 33 + 33
            else:
                if char in ascii_letters:
                    new_char = ascii_lowercase.index(char) + shift
                    new_char = new_char % 26
                if char in cyrillic_letters:
                    new_char = cyrillic_lowercase.index(char) + shift
                    new_char = new_char % 33

            result += ascii_letters[new_char] if (char in ascii_letters) else cyrillic_letters[new_char]
        
        return result

    def ROT1(
        self,
        text: str
        ) -> str:
        """
        Encrypting text with ROT13

        Parameters
        ----------
        text : str
            The text to be encrypted

        Returns
        -------
        str
            Encrypted text
        """

        return self.Caesar(text, shift=1)

    def ROT13(
        self,
        text: str
        ) -> str:
        """
        Encrypting text with ROT13

        Parameters
        ----------
        text : str
            The text to be encrypted

        Returns
        -------
        str
            Encrypted text
        """

        return self.Caesar(text, shift=13)
    
    def A1Z26(
        self,
        text: str
        ) -> str:
        """
        Encrypting text with A1Z26 cipher

        Parameters
        ----------
        text : str
            The text to be encrypted

        Returns
        -------
        str
            Encrypted text
        """
        if not text:
            raise TypeError("text must be str, not " + type(text))
        
        result = ''
        for char in text:
            if not char.isalpha():
                continue

            if char not in (ascii_letters + cyrillic_letters):
                raise ValueError("Supported only ASCII and Cyrillic letters")

            if char.isupper():
                if char in ascii_letters:
                    result += str(ascii_uppercase.index(char) + 1) + ' '
                elif char in cyrillic_letters:
                    result += str(cyrillic_uppercase.index(char) + 1) + ' '
            else:
                if char in ascii_letters:
                    result += str(ascii_lowercase.index(char) + 1) + ' '
                elif char in cyrillic_letters:
                    result += str(cyrillic_lowercase.index(char) + 1) + ' '
        result = result.strip()
        
        return result

    def Vigenere(
        self,
        text: str,
        key: str = None,
        cyrillic: bool = False,
        ignore_case: bool = False,
        shift: int = 0
        ) -> str:
        """
        Encrypting text with Vigenère cipher

        Parameters
        ----------
        text : str
            The text to be encrypted
        key : str
            Encryption key (default is random char's in the range from 2 to 16)
        cyrillic : bool
            If need to encode Russian language - True (default is False)
        ignore_case : bool
            When true - all characters be uppercase

        Returns
        -------
        str
            Encrypted text
        """
        if not text:
            raise TypeError("text must be str, not " + type(text))

        alphabet = ascii_uppercase if not cyrillic else cyrillic_uppercase

        if not key:
            key = ''.join(random.choice(alphabet) for _ in random.randrange(2, 16))

        if shift > 0:
            text = self.Caesar(text, shift)

        if ignore_case:
            text = text.upper()

        key = key.strip(punctuation + ' ').upper()

        if len(key) != len(text):
            if len(key) > len(text):
                key = key[:len(text)]
            else:
                for i in range(len(text) - len(key)):
                    key += key[i % len(key)]

        result = ''
        keyIndex = 0
        for char_text in text:
            if not char_text.isalpha():
                result += char_text
                continue
            
            if char_text not in (ascii_letters + cyrillic_letters):
                raise ValueError("Supported only ASCII or Cyrillic letters")

            if char_text.isupper():
                index = alphabet.index(char_text) + alphabet.index(key[keyIndex])
                index = index % len(alphabet)
                result += alphabet[index]
            else:
                index = alphabet.lower().index(char_text) + alphabet.index(key[keyIndex])
                index = index % len(alphabet)
                result += alphabet.lower()[index]

            keyIndex += 1

        return result

    def Hill(
        self,
        text: str,
        key: str,
        cyrillic: bool = False
        ) -> str:
        """
        Encrypting text with  cipher

        Parameters
        ----------
        text : str
            The text to be encrypted
        key : str
            Encryption key (default is random char's in the range from 2 to 16)
        cyrillic : bool
            If need to encode Russian language - True (default is False)
        
        Returns
        -------
        str
            Encrypted text
        """
        if not text:
            raise TypeError("text must be str, not " + type(text))
        
        text = ''.join([c for c in text if c not in punctuation]).upper()

        key = key.upper()
        alphabet = (ascii_uppercase if not cyrillic else cyrillic_uppercase) + ' '

        key_root = int(len(key) ** 0.5)
        text_len = len(text) / key_root

        if text_len % 1 != 0:
            text_len = int(text_len) + 1

        text_len = int(text_len)

        if not (len(key) ** 0.5).is_integer():
            raise ValueError("key length should be square of integer")

        key_matrix = [
            [k for k in key[i:i+key_root]] for i in range(0, len(key), key_root)
        ]

        text_vectors = [
            [t for t in text[i:i+key_root]] for i in range(0, len(text), key_root)
        ]

        if len(text_vectors[-1]) != len(text_vectors[0]):
            for i in range(len(text_vectors[0]) - len(text_vectors[-1])):
                text_vectors[-1].append("Z")


        key_matrix = [[alphabet.index(i) for i in line] for line in key_matrix]

        text_vectors = [[alphabet.index(i) for i in line] for line in text_vectors]

        result_vectors = [[sum(a*b for a,b in zip(vector_row, key_column))%len(alphabet) for key_column in zip(*key_matrix)] for vector_row in text_vectors]

        result = ''
        for row in result_vectors:
            for el in row:
                result += alphabet[el] 
        
        return result