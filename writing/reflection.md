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

For all of my following research questions, I attempted to controll as many variables as possible. I chose to set my starting container size to 105. This because I wanted a very quick glance at all of the approaches. I then limited the total number of doubles to 5 so I could compare across the approaches and within. I chose to ignore the maxium value tag and allow it to just use the number coded as the default which is 10000. I choose to keep many of these small due to the known ineffeciency of the approaches. 

By only changing the approach, the independent variable, I can compare the outputs collected with each other easily. My dependent variable is time which is then collected and displayed in the charts that are already given in the outputs. With the format of my questions, I also only need to run each of the approaches once and then analyze.

Future experimentation could look at these with a larger total of number of doubles. Another option could be to vary the maximum number. These should be conducted with less time limit and adjusted due to the knowledge gained from answering my current questions. 

## Research Questions

* RQ 1. With the starting container size of 105 and doubling 5 times, which approach has the fastest average time?

* RQ 2. With the starting container size of 105 and doubling 5 times, which approaches have a consitent worsening performance ratio as container size increases?

* RQ 3. With the starting container size of 105 and doubling 5 times, which approaches have a changing performance ratio as container size increases? 

## Performance Analysis

### Empirical Evaluation

#### Table 1: Average Times of Approaches

| Bubble  | Insertion | Merge   | Quick   | Tim     |
| ------  | --------- | ------- | ------- | ------- |
| 0.02423 | 0.0125    | 0.00766 | 0.00534 | 0.00868 |
| 0.06674 | 0.03381   | 0.01611 | 0.01197 | 0.02597 |
| 0.27205 | 0.11786   | 0.03075 | 0.01834 | 0.05609 |
| 0.84737 | 0.41888   | 0.04108 | 0.04123 | 0.04896 |
| 3.42626 | 1.49031   | 0.13437 | 0.08098 | 0.12688 |

#### Table 2: Changes in Performance Between Doubles
| Approach  | 1 & 2  | 2 & 3  | 3 & 4   | 4 & 5  |
| --------- | ------ | ------ | ------- | ------ |
| Bubble    | 63.69% | 75.47% | 67.89%  | 75.27% |
| Insertion | 63.02% | 71.31% | 71.86%  | 71.89% |
| Merge     | 52.45% | 47.61% | 24.15%  | 68.43% |
| Quick     | 55.39% | 34.73% | 55.52%  | 49.09% |
| Tim       | 66.58% | 53.70% | -12.71% | 61.41% |

Above is an aggregated table of the average time columns of each of the respective approaches for ease of comparison. The second is using the performance arthimetic to decipher how much faster the smaller container was to the double.

With my first research question, I wanted to compare the average times of each of the approaches. Overall, the quick approach always had the faster time except for the 4 double where the merge approach was faster by 0.00015 seconds. The order was also consitent of the bubble sort always being slowest, with the insertion sort as second slowest. Merge, timsort, and quicksort all were reasonably close with each double. On the fifth double, quicksort was 97.64% faster than the bubblesort (the slowest) and 36.17% faster than timsort (the next fastest approach). 

With my second research question, I was looking at consistancy in the changes of speed as the container size increased. Though I was surprised with my results, I believe I can only say that insertion sorting had the most consitent percentage of worsening. It is important to note that this change is also worsening by around 70% every double.

With my third research question, I was looking at inconsistancy in the performance time changes. This could be applied to all of the approaches with the data that I gathered. At the moment, I have a hard time deciphering if there was any error that occured. The most notable of these potential errors (or findings) is between doubles 3 and 4 of the timsort. The larger container size from the fourth double in the sequence was actually faster than the third double. I would want to conduct this experiment again. I would start with the same starting number of 105 and increase the number of doubles to have more data to study before I would like to draw any conclusion to this question.


### Analytical Evaluation

These algorithms have varying worst-case time complexities. From my available resources, quick, merge, and timsort all have the O(nlogn). This is matches our empirical findings as these three were the fastest. The bubble and insertion sort run with a worst-case time complexity of O(n^2). This fits with the drastic increase of time for the larger size containers. I am not convinced that bubblesort and insertion have the same exact worst-case time complexity due to my empirical data.

## Professional Development

### What is challenging about designing an experiment to evaluate sorting algorithm's performance?

For this lab, the most challenging about designing an experiment to evaluate sorting algorithm's performance was the process of creating research questions. I personally struggled to determine what was worthy of testing. In the end, I determined that all research needs a starting point. Even though my current questions feel preliminary, I know that this is where I needed to start to develop my knowledge about sorting algorithms. After the completion of this lab, I would be prepared to design new tests for new questions.

### Overall, what is the fastest sorting algorithm based on your empirical results?

The fastest sorting algorithm based on my empirical results is the quick sort algorithm. Though it was similar to the timsort and merge approaches in the first runs, the larger container sizes showed that the quick sort truly was the fastest. This algorithm also decreased speed consistently with a loss of about 50% of their performance time with each double in container size.

### How do the empirical results suggest that you don't yet know the entire story about the performance of sorting algorithms?

The empirical results suggest that we don't yet know what the sort is being applied to. Not all data should use the same algorithms. The speed of the quicksort may not actually be useful in certain applications. Sometimes it is worth spending more time to do a better sorting method to then be able to do many calculations with the sorted data.
