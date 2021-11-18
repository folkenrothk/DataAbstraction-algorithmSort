"""Conduct doubling experiments for provided algorithms that perform list sorting."""

from typing import List
from typing import Tuple
from typing import Union

import random

from timeit import repeat

# Reference for some parts of the experimentation framework:
# https://realpython.com/sorting-algorithms-python/


def format_decimal(number: float):
    """Round a number up and then encode with five decimal places."""
    format_float = "{:.5f}".format(number)
    # multiplier = 10 ** decimals
    # return "{:.5f}".format(math.ceil(n * multiplier) / multiplier)
    return format_float


def generate_random_number(maximum: int) -> int:
    """Generate a random list defined by the size."""
    # generate a random value that is bound by 0 and a maximum
    random_value = random.randint(0, maximum)
    # return the randomly generated number
    return random_value


def generate_random_container(
    size: int,
    maximum: int,
) -> List[int]:
    """Generate a random list defined by the size."""
    # generate a list of random values for a specific size
    # and with a number up to a specific maximum
    random_list = [random.randrange(1, maximum, 1) for _ in range(size)]
    return random_list


def run_sorting_algorithm(algorithm: str, array: List[int]) -> Tuple[str, str, str]:
    """Run a sorting algorithm and profile it with the timeit package."""
    # set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from listsorting.sorting import {algorithm}"
    stmt = f"{algorithm}({array})"
    # execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    # finally, return the amount of execution time summarized as:
    # (minimum execution time, maximum execution time, average execution time)
    return (
        format_decimal(min(times)),
        format_decimal(max(times)),
        format_decimal((sum(times) / len(times))),
    )


def run_sorting_algorithm_experiment_campaign(
    algorithm: str,
    starting_size: int,
    maximum_value: int,
    number_doubles: int,
) -> List[List[Union[int, Tuple[float, float, float]]]]:
    """Run an entire sorting algorithm experiment campaign."""
    data_table = []
    # run a total of number_doubles number of doubles for the input size
    while number_doubles > 0:
        # generate a random list based on the current size of the data
        random_list = generate_random_container(starting_size, maximum_value)
        # run the sorting algorithm and collect the timing data from timeit
        performance_data = run_sorting_algorithm(algorithm, random_list)
        # create the row of data from this specific execution of the algorithm
        data_table_row = [
            starting_size,
            performance_data[0],
            performance_data[1],
            performance_data[2],
        ]
        # add this row to the data table that will contain all of the results
        data_table.append(data_table_row)
        # move to the next round of the doubling experiment
        number_doubles = number_doubles - 1
        starting_size = starting_size * 2
    return data_table
