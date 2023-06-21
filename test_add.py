import pytest
from hello_word import addition_Jhon

def test_addition_returns_result_when_have_two_numbers():
    first_number = 3
    second_number = 7
    expected_result = 10

    result = addition_Jhon(first_number, second_number)

    assert expected_result == result
