import pytest 

from word_puzzle import make_underscore, make_upper


def test_make_underscore():
    secret_word = "mosiah"
    hide_word = "_ _ _ _ _ _"
    assert make_underscore(secret_word) == hide_word

def test_make_upper():
    secret_word = "mosiah"
    guess = "mosiah"
    guess_incorrect ="mosiaa"
    assert make_upper(guess, secret_word) == "MOSIAH"
    assert make_upper(guess_incorrect, secret_word) == "MOSIA_"

"""
python -m pytest -v -s
"""
