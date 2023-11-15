# Write tests using Pytest that test all the functions in helper_functions.py
# Run the tests using pytest

import pytest
from helper_functions import *

def test_capitalise_name():
    # create tests for the capitalise_name function that are based on the name Matilda
    assert capitalise_name("matilda") == "Matilda"
    assert capitalise_name("MATILDA") == "Matilda"
    assert capitalise_name("mAtIlDa") == "Matilda"
    # create more tests with different girls names
    assert capitalise_name("sarah") == "Sarah"
    assert capitalise_name("SARAH") == "Sarah"
    assert capitalise_name("SaRaH") == "Sarah"
    # Add some tests that check that it is not incorrectly capitalising non-anglo names
    assert capitalise_name("mohammed") == "Mohammed"
    assert capitalise_name("MOHAMMED") == "Mohammed"
    assert capitalise_name("MoHaMmEd") == "Mohammed"
    # # test that it raises a TypeError when passed a number as an argument
    # with pytest.raises(TypeError):
    #     capitalise_name(123)

def test_get_colours():
    # create tests for the get_colours function that check that it returns the correct number of colours
    assert len(get_colours(3)) == 3
    assert len(get_colours(5)) == 5
    assert len(get_colours(7)) == 7
    # create tests for the get_colours function that check that it returns the correct colours
    assert get_colours(3) == ["red", "blue", "green"]
    assert get_colours(5) == ["red", "blue", "green", "yellow", "orange"]
    assert get_colours(7) == ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
    # # test that it raises a TypeError when passed a string as an argument
    # with pytest.raises(TypeError):
    #     get_colours("hello")

def test_get_names_starting_with():
    # create tests for the get_names_starting_with function that check that it returns the correct names
    assert get_names_starting_with(["Matilda", "Sarah", "Hannah", "Samantha", "Jenny", "Sue"], "S") == ["Sarah", "Samantha", "Sue"]
    assert get_names_starting_with(["Matilda", "Sarah", "Hannah", "Samantha", "Jenny", "Sue"], "M") == ["Matilda"]
    assert get_names_starting_with(["atilda", "Sarah", "Hannah", "Samantha", "Jenny", "Sue"], "J") == ["Jenny"]
    # test that it raises a TypeError when passed a number as an argument
    # with pytest.raises(TypeError):
    #     get_names_starting_with(123, "S")
    # # test that it raises a TypeError when passed a number as an argument
    # with pytest.raises(TypeError):
    #     get_names_starting_with(["Matilda", "Sarah", "Hannah", "Samantha", "Jenny", "Sue"], 123)

pytest.main() 