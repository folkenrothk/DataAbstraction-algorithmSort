"""Tests for the sorting function to ensure that sort algorithms work correctly."""


import pytest

from listsorting import sorting


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_sorting_algorithms_multiple_inputs(list_inputs, expected_answer):
    """Check the sorting algorithm functions with multiple inputs."""
    sorted_list = sorting.bubble_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.insertion_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.merge_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.quick_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.tim_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([10, 3, 1], [1, 3, 10])],
)
def test_bubble_sort_single(list_inputs, expected_answer):
    """Check the sorting algorithm functions with one input."""
    sorted_list = sorting.bubble_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.insertion_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.merge_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.quick_sort(list_inputs)
    assert sorted_list == expected_answer
    sorted_list = sorting.tim_sort(list_inputs)
    assert sorted_list == expected_answer
