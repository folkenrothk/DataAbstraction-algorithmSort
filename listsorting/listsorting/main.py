"""Perform an experiment to study efficiency of sorting."""

# Reference for some algorithm implementations:
# https://realpython.com/sorting-algorithms-python/

from enum import Enum

import typer

from rich.console import Console
from tabulate import tabulate

from listsorting import experiment

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for rich text output
console = Console()

SORT_FUNCTION_BASE = "sort"
UNDERSCORE = "_"


class ListSortingApproach(str, Enum):
    """Define the name for the approach for performing list sorting with different algorithms."""

    bubblesort = "bubble"
    insertionsort = "insertion"
    mergesort = "merge"
    quicksort = "quick"
    timsort = "tim"


@cli.command()
def listsorting(
    starting_size: int = typer.Option(1000000),
    maximum_value: int = typer.Option(10000),
    number_doubles: int = typer.Option(10),
    approach: ListSortingApproach = ListSortingApproach.bubblesort,
) -> None:
    """Conduct a doubling experiment to measure the performance of list sorting for various algorithms."""
    console.print(
        ":sparkles: Conducting and experiment to measure the performance of list sorting!"
    )
    # Display diagnostic details about the configuration of the experiment
    console.print(f"The chosen sorting algorithm: {approach}")
    console.print(f"Starting size of the data container: {starting_size}")
    console.print(f"Number of doubles to execute: {number_doubles}")
    console.print()

    # display the details about the results from running the experiment,
    # first by giving a label so show that the program will provide output
    # create the name of the algorithm as a string using the approach and then appending the _sort postfix to the end of the name;
    # this leads to the creation of names like "merge_sort"
    algorithm = approach + UNDERSCORE + SORT_FUNCTION_BASE
    # conduct a doubling experiment for sorting by calling the run_sorting_algorithm_experiment_campaign
    # function with the inputs in the following order:
    # --> algorithm
    # --> starting_size
    # --> maximum_value
    # --> number_doubles
    results = experiment.run_sorting_algorithm_experiment_campaign(
        algorithm, starting_size, maximum_value, number_doubles
    )

    console.print(":sparkles: Here are the results from running the experiment!")
    # use the tabulate function to create a data table of the experimental_results
    # make sure that the data table has a header that is organized in this fashion:
    # --> Column 1: Input Size
    # --> Column 2: Minimum execution time in seconds
    # --> Column 3: Maximum execution time in seconds
    # --> Column 4: Average execution time in seconds
    # There must be a header that displays these labels and then the data should be displayed below it in rows.
    # There should be a single row for each level of the doubling experiment conducted by run_sorting_algorithm_experiment_campaign
    # Reference for the tabulate package:
    # https://github.com/astanin/python-tabulate
    """Print output and table in the console"""
    printTable = tabulate(
        results, headers=["Input Size", "Min time (s)", "Max time (s)", "Avg time (s)"]
    )
    console.print(printTable)
