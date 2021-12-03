# Sorting Algorithms

## Kate Folkenroth

## Program Output

### Report at least five examples of program output to demonstrate that your `listsorting` program works correctly

Below are the example outputs from running the `listsorting` program.  Each output has been collected for research question 1 (RQ1). The parameters are described thoroughly in the [Experiment Design](#Experiment-Design) section below. In each section, labeled with the command inputted to the terminal and the subsequent output.

#### BubbleSort output from running the `listsorting` program

`poetry run listsorting --starting-size 105 --number-doubles 5 --approach bubble`

```
✨ Conducting and experiment to measure the performance of list sorting!
The chosen sorting algorithm: bubble
Starting size of the data container: 105
Number of doubles to execute: 5

✨ Here are the results from running the experiment!
  Input Size    Min time (s)    Max time (s)    Avg time (s)
------------  --------------  --------------  --------------
         105         0.02088         0.02713         0.02423
         210         0.06311         0.07347         0.06674
         420         0.24092         0.30932         0.27205
         840         0.73054         0.91064         0.84737
        1680         3.13634         3.67502         3.42626
```

#### InsertionSort output from running the `listsorting` program

`poetry run listsorting --starting-size 105 --number-doubles 5 --approach insertion`

```
✨ Conducting and experiment to measure the performance of list sorting!
The chosen sorting algorithm: insertion
Starting size of the data container: 105
Number of doubles to execute: 5

✨ Here are the results from running the experiment!
  Input Size    Min time (s)    Max time (s)    Avg time (s)
------------  --------------  --------------  --------------
         105         0.00873         0.01622         0.0125
         210         0.03044         0.04024         0.03381
         420         0.11008         0.12328         0.11786
         840         0.3215          0.48557         0.41888
        1680         1.29325         1.65495         1.49031
```

#### MergeSort output from running the `listsorting` program

`poetry run listsorting --starting-size 105 --number-doubles 5 --approach merge`

```
✨ Conducting and experiment to measure the performance of list sorting!
The chosen sorting algorithm: merge
Starting size of the data container: 105
Number of doubles to execute: 5

✨ Here are the results from running the experiment!
  Input Size    Min time (s)    Max time (s)    Avg time (s)
------------  --------------  --------------  --------------
         105         0.0062          0.00943         0.00766
         210         0.01496         0.01775         0.01611
         420         0.02973         0.03157         0.03075
         840         0.03651         0.0502          0.04108
        1680         0.1234          0.14508         0.13437
```

#### QuickSort output from running the `listsorting` program

`poetry run listsorting --starting-size 105 --number-doubles 5 --approach quick`

```
✨ Conducting and experiment to measure the performance of list sorting!
The chosen sorting algorithm: quick
Starting size of the data container: 105
Number of doubles to execute: 5

✨ Here are the results from running the experiment!
  Input Size    Min time (s)    Max time (s)    Avg time (s)
------------  --------------  --------------  --------------
         105         0.0045          0.00579         0.00534
         210         0.01058         0.01307         0.01197
         420         0.01726         0.01956         0.01834
         840         0.03824         0.04641         0.04123
        1680         0.07607         0.08558         0.08098
```

#### TimSort Output from running the `listsorting` program

`poetry run listsorting --starting-size 105 --number-doubles 5 --approach tim`

```
✨ Conducting and experiment to measure the performance of list sorting!
The chosen sorting algorithm: tim
Starting size of the data container: 105
Number of doubles to execute: 5

✨ Here are the results from running the experiment!
  Input Size    Min time (s)    Max time (s)    Avg time (s)
------------  --------------  --------------  --------------
         105         0.00743         0.00948         0.00868
         210         0.02253         0.03134         0.02597
         420         0.04844         0.06396         0.05609
         840         0.04692         0.0526          0.04896
        1680         0.11214         0.1436          0.12688
```

## Experiment Design

TODO: Explain the setup for your experiment that you ran to characterize the performance of the different configurations of containment checking algorithms. For instance, you should consider the following parameters as a part of your
experiment:

- The specific sorting algorithm
- The starting size of the data container: small values (e.g., 1024 numbers) to big
  values (e.g., 1,048,576 numbers)
- The total number of doubles conducted during the experiment (e.g., 5 or 10)

TODO: You may need to design a custom experiment for certain sorting algorithms due the fact that there may be some algorithms that are inefficient!

TODO: You must justify every part of your experiment design and then furnish output examples to demonstrate that your program generates correct data!

## Research Questions

// TODO: Make sure that the totality of your research questions cover all of the sorting algorithms provided by the `listsorting` program.

* RQ 1. With the starting container size of 105 and doubling 5 times, which approach has the fastest average time?

* RQ 2. With the starting container size of 105 and doubling 5 times, which approaches have a consitent worsening performance ratio as container size increases?

* RQ 3. With the starting container size of 105 and doubling 5 times, which approaches have a changing performance ratio as container size increases? 

## Performance Analysis

### Empirical Evaluation

TODO: The output data tables provided above of the ones that you should reference when you are reporting on your empirical evaluation.

TODO: Provide at least three paragraphs that explain which containment checking
algorithm is fastest, by how much it is faster, and how you knew that it was
faster, referencing the data in the aforementioned command outputs and the data
tables to support your response. You should make sure that you answer each of
the at least three research questions that you posed in a previous section.

TODO: Make sure that your responses explain WHY certain configurations are faster!
TODO: It is not sufficient to ONLY explain WHICH configuration is faster!

### Analytical Evaluation

TODO: Using the provided source code for the different containment check algorithms, your textbook, your experimental results, and any relevant online resources that you cite in this reflection, define the worst-case time complexity, using the big-O notation, for the five sorting algorithms. Please note that you do not need to prove the worst-case time complexity; rather you
may reference existing sources that tell you the worst-case time complexity and then confirm that they are correct by using your empirical results.

## Professional Development

### What is challenging about designing an experiment to evaluate sorting algorithm's performance?

For this lab, the most challenging about designing an experiment to evaluate sorting algorithm's performance was the process of creating research questions. I personally struggled to determine 

### Overall, what is the fastest sorting algorithm based on your empirical results?

TODO: Provide a one-paragraph response that answers this question in your own words.

### How do the empirical results suggest that you don't yet know the entire story about the performance of sorting algorithms?

TODO: Provide a one-paragraph response that answers this question in your own words.
