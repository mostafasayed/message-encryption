import string
from num2words import num2words
import itertools

LETTERS = list(iter(string.ascii_uppercase))
PUNCTUATION = [' ', ',', '.', '?', '(', ')']


def convert_number_to_word(word):
    """Check type of the parameter if it integer or float then convert the number to words
    :param word: parameter to be converted to word
    :type word: str
    :Example::
    >>> convert_number_to_word("16")
    sixteen
    :return: the word version of number if it integer or float
    :rtype: str
    """
    try:
        word = num2words(float(word))
    except:
        try:
            word = num2words(int(word))
        except:
            word = word
    return word


def convert_sentence_to_word(sentence):
    """This Function take sentence and check if this sentence contain number it will convert it to words
    then return capitalized sentence
    :param sentence: string to be converted to capitalized
    :type sentence: str
    :return: capitalized sentence after converting any number to word
    """
    res = []
    for word in sentence.split(' '):
        word = convert_number_to_word(word)
        res.append(word.upper())
    return ' '.join(res)


def caesar_shift_message(shift, sentence):
    """Shifting letter using specified shifting indicator then get equivalent bit for each element
    A-Z --> 0-25
    [' ', ',', '.', '?', '(', ')'] --> 26-31
    :param shift: number of letter to be shifted
    :type shift: int
    :param sentence: sentence to be shifted using shift
    :type sentence: str
    :Example::
    >>>caesar_shift_message(3, 'AB')
    '34'
    :return: bits of shifted sentence
    """
    res = ''
    converted_sentense = convert_sentence_to_word(sentence)
    for letter in converted_sentense:
        if letter in LETTERS:
            new_position = LETTERS.index(letter) + shift
            res += str(new_position % 26)
        elif letter in PUNCTUATION:
            res += str(PUNCTUATION.index(letter) + 26)
    return res


def equivalent_binary(num):
    """Convert string number input to binary
    :param num: parameter to be converted to binary
    :type num: str
    :return: string of binary equivalent to input
    """
    return "{0:02b}".format(int(num))


def encode_binary(binary):
    """Encode binary with summing each element with his surrounding elements
    :param binary: binary number to be encoded
    :type binary: str
    :return: encoded input
    """
    res = ''
    for i in range(len(binary)):
        if i == 0:
            res += str(int(binary[i])+int(binary[i+1]))
        elif i == len(binary) - 1:
            res += str(int(binary[i])+int(binary[i-1]))
        else:
            res += str(int(binary[i])+int(binary[i+1])+int(binary[i-1]))
    return res


def convert_encode_to_bin(encoded):
    """
    Convert each element in input to binary then return them
    :param encoded: encoded binary to be converted to binary
    :return: binary of each element of input
    """
    res = [equivalent_binary(num) for num in encoded]
    return ''.join(res)


def convert_to_hex(binary):
    """Convert binary to hex
    :param binary: string
    :return: hexadecimal
    """
    return hex(int(binary, 2))[2:]


def encrypt_message():
    """Encrypt message from user input use old technique that make caesar shifting (after converting numbers to words) and convert them to
    bits then convert bit to binary then encode this binary then convert encoded binary to binary and finally return
    hexadecimal value for it
    :param msg: message to be encrypted first space will be caesar shifting and other will be the message
    :type msg: str
    :Example::
    >>>encrypt_message()
    >>> 1
    >>> "3 A"
    A
        caesar shift: 3
        shifting of A: D and equivalent bit: 3
        binary of 3: 11
        encoded of binary: 22
        binary of encoded: 1010
        hexadecimal: A
    :return: Encrypted message (hexadecimal)
    :rtype: str
    """
    result = []
    input_length = input("Put number of messages to be encrypted:\n")
    for i in range(int(input_length)):
        msg = input("Put your msg:\n")
        shift, sentence = msg.split(" ", 1)
        sentence = convert_sentence_to_word(sentence)
        caesar = caesar_shift_message(int(shift), sentence)
        binary = equivalent_binary(caesar)
        encoded = encode_binary(binary)
        binary_encoded = convert_encode_to_bin(encoded)
        msg_hex = convert_to_hex(binary_encoded).upper()
        print(msg_hex)
        result.append(msg_hex)
    return result


if __name__ == "__main__":
    encrypt_message()
