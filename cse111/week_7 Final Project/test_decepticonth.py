import pytest 
import os

from decepticonth import make_lower_case, open_url, comparing


def test_make_lower_case():
    document = ['LOL']
    expected = ['lol']
    assert make_lower_case(document) == expected

    document = ['LumberJack, TACO']
    expected = ['lumberjack, taco']
    assert make_lower_case(document) == expected


def test_comparing():

    name = "the"
    document = ["the"]
    test_total = "It is repeated is 1 times"

    assert test_total == comparing(name, document)

    name = "bro"
    document = ["bro","go", "play", "minecraft", "bro"]
    test_total = "It is repeated is 2 times"

    assert test_total == comparing(name, document)

"""

python -m pytest -v -s

"""


