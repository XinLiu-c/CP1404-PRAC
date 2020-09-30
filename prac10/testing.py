"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac6.car import Car


def repeat_string(s, n):
    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    # TODO: 4. Fix the failing is_long_word function
    # (don't change the tests, change the function!)
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these

    test_car = Car()
    assert test_car.fuel == 0
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

def phrase_to_sentence(phrase):
    # TODO: 5. Write and test a function to format a phrase as a sentence,
    """
        Determine if the word is as long or longer than the length passed in
        >>> phrase_to_sentence("hello")
        "Hello.'
        >>> phrase_to_sentence("It is an ex parrot.")
        "It is an ex parrot."
        >>> phrase_to_sentence("yahoo.")
        "Yahoo."
        """

    sentence = phrase.capitalize()
    if sentence[-1] !='.':
        sentence+='.'
    return sentence

run_tests()

doctest.testmod()


