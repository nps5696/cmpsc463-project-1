# Introsort Algorithm, CMPSC-463 Project 1
![pylint](https://img.shields.io/badge/pylint-8.91-yellow?logo=python&logoColor=white)

---

## Implementing hybrid sorting algorithms

 For this project, I am going to implement the Introsort algorithm. The algorithm relies on Quicksort and Heapsort. The goal of this project is to research the difference in implementation and complexity of the hybrid Introsort algorithms and Quicksort, Heapsort Algorithms.

## These are the key points for the project:

- Explore Introsort algorithm structure and logic
- Introsort Implementation
- Performance Analysis
- Introspective hybrid sorting performance compared to Quicksort and Heapsort
- Add Unit Tests

### Explore Introsort algorithm structure and logic

#### The structure of Introsort comprises three main parts: 

- Introsort logic to choose either Quicksort or Heapsort algorithms
- Quicksort algorithm implementation
- Heapsort algorithms implementation

The algorithm tries to use Quicksort initially and falls back to Heapsort when inefficiency in Quicksort is detected. The inefficiency of Quicksort comes from a high level of recursion which usually indicates the pivot was not selected in the best possible way. When the pivot is constantly selected as the most right or most left element we do not have a good separation of sub-arrays passed to the next recursion call, and we end up with O(n^2) complexity. When such a condition is detected we switch to the Heapsort algorithm which can sort in O(n log n) time. 

### Introsort Implementation

The Introsort is implemented with Quicksort, Heapsort, and Routing functions (routes sorting to either heapsort or quicksort). I measure its performance with start/end timestamps. Since we already have the implementation of Quicksort within the Introsort, external implementation is not necessary and instead, I pass an extra parameter to the routing function to forcefully use Quicksort for the times when I compare algorithm performances.

### Performance Analysis

#### Quicksort and Introspective Sort Performance Comparison

Quicksort has a big disadvantage for the cases where it is picking the left-most or right-most element, increasing its complexity to O(n^2). The introspective sorting algorithm utilizes heapsort for cases such as this. Let's look at the sorting time performance graph:

![introsort vs quicksort run time](https://github.com/nps5696/cmpsc463-fp/blob/develop/img/intospective_vs_quicksort.png)

On the graph you can see real-world performance on test data, the performance was generated from running Introsort and Quicksort Algorithms with a list length of 1000 of unsorted integers. The complexity is clearly visible, **as we increase the size of our array the Quicksort algorithm trend shows quadratic growth, while Introsort shows logarithm based growth function.**

### Introspective hybrid sorting performance compared to Quicksort and Heapsort

Why not use Quicksort alone? Quicksort has worst-case complexity O(n^2) for the poorly selected pivot, therefore we rely on Heapsort to avoid such worst cases.

Why not use Heapsort alone? Heapsort tends to perform worse compared to Quicksort for smaller arrays because it utilizes local cache, and parallelization better, Quicksort also has a simpler data structure to work with - arrays vs max heap in Heapsort. Heapsort has to work with a more complex structure - heap which adds overhead to its run time. 

Overall we get the best from both algorithms when exploiting their strengths. We get faster sorting for smaller arrays using Quicksort, which gives us the complexity of O(n log n). And for the larger arrays we switch to Heapsort to avoid O(n^2) complexity from Quicksort, the switch to Heapsort keeps the complexity for larger arrays at O(n log n) time. Therefore, we have the complexity of O(n log n) for any case.

### For my test case with 100 arrays varying length of 10 to 1000 items, I recieved thise performance results:

```
Average performance for 100 runs printout: 
Average running time of Introsort for 100 sets: 0.0009717774391174316
Average running time of Quicksort for 100 sets: 0.006901700496673584


Performance gain for our test case: 
Average performance gain of Introsort vs Quicksort for 100 tests: 7.102141106446873
```

The performance is heavily dependent on test cases, and will change in accordance with complexities of the Introsort and Quicksort I mentioned in this document above.