import pytest

from lab.iter import LinkedList

def test_for_in():

    foods = LinkedList(("Pizza","Potato","Checken"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert foods_list == ["Pizza","Potato","Checken"]


def test_list_comprehension():

    foods = LinkedList(("Pizza","Potato","Checken"))

    cap_foods = [food.upper() for food in foods]

    assert cap_foods == ["PIZZA","POTATO","CHECKEN"]

def test_list_cast():

    food_list = ["Pizza","Potato","Checken"]

    foods = LinkedList(food_list)

    assert list(foods) == food_list

def test_range():

    num_range = range(1,20+1)

    nums = LinkedList(num_range)

    assert len(nums) == 20


def test_filter():

    nums = LinkedList(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]

def test_next():

    foods = LinkedList(["Pizza","Potato","Checken"])

    iterator = iter(foods)

    assert next(iterator) == "Pizza"
    assert next(iterator) == "Potato"
    assert next(iterator) == "Checken"

def test_stop_iteration():

    foods = LinkedList(["Pizza","Potato","Checken"])

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)


def test_str():
    foods = LinkedList(["Pizza","Potato","Checken"])
    assert str(foods) == "[ Pizza ] -> [ Potato ] -> [ Checken ] -> None"

# dunder method tests

def test_equals():

    lla = LinkedList(["Pizza","Potato","Checken"])
    llb = LinkedList(["Pizza","Potato","Checken"])

    assert lla == llb

def test_get_item():

    foods = LinkedList(["Pizza","Potato","Checken"])

    assert foods[0] == "Pizza"

def test_get_item_out_of_range():

    foods = LinkedList(["Pizza","Potato","Checken"])

    with pytest.raises(IndexError):
        foods[100]