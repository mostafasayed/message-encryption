import pytest
from unittest.mock import MagicMock
import encrypt


def test_caesar_shift_message_negative_caesar_word_contain_punctuation():
    res = encrypt.caesar_shift_message(-3, 'TWO TWO ( 16.31 )')
    assert res == '16191126161911263026155201611102612115101626164141126111012631'


def test_encode_binary_return_111221_with_100110():
    res = encrypt.encode_binary('100110')
    assert res == '111221'


def test_call_convert_encode_to_bin_return_1010010101_with_22111():
    res = encrypt.convert_encode_to_bin('22111')
    assert res == '1010010101'


def test_encrypt_message_return(monkeypatch):
    mock_input = MagicMock()
    mock_input.side_effect = ["2", "3 A", "-1 A"]
    monkeypatch.setattr("builtins.input", mock_input)
    res = encrypt.encrypt_message()
    assert res == ["A", "295"]
