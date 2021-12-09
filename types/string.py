"""A collection of string constants.

Public module variables:

whitespace -- a string containing all ASCII whitespace
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
cyrillic_lowercase -- a string containing all Cyrillic lowercase letters
cyrillic_uppercase -- a string containing all Cyrillic uppercase letters
cyrillic_letters -- a string containing all Cyrillic letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
punctuation -- a string containing all ASCII punctuation characters
printable -- a string containing all ASCII characters considered printable

"""

__all__ = ["ascii_letters", "ascii_lowercase", "ascii_uppercase",
           "cyrillic_letters", "cyrillic_lowercase", "cyrillic_uppercase",
           "digits", "hexdigits", "octdigits", "printable", "punctuation",
           "whitespace"]


whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
cyrillic_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyrillic_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_letters = cyrillic_lowercase + cyrillic_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace
