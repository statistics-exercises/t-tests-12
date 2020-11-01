# Comparison of means II

Let's do the comparison of means for a small sample with some small modifications one further time in order to consolidate what we have learned.  This time we will set the null and alternative hypotheses as follows:

* __Null hypothesis__: The difference between the expectation of the distributions that were sampled to generate the points in the NumPy arrays called `data1` and `data2` is 10. 
* __Alternative hypothesis__: The difference between the expectation of the distributions that were sampled to generate the points in the NumPy arrays called `data1` and `data2` is less than 10. 

__As in the previous exercise, you need to complete the following functions to pass this final task__:

1. `testStatisti`c - this function takes two  NumPy arrays in input:  `data1` that contains the samples from the first distribution and `data2` contains the samples from the second distribution.  This function should return the test statistic that was introduced in the previous task.   
2. `pvalue` - this function takes two  NumPy arrays in input:  `data1` that contains the samples from the first distribution and `data2` contains the samples from the second distribution.   To complete the task you must use the value of the `testStatistic` to calculate the __p-value__.  The p-value should then be returned.
