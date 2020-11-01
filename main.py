import numpy as np
import scipy.stats 

def testStatistic( data1, data2 ) :
  # This function should calcualte and return the test statistic T that is 
  # described in the panel on the right.  Notice that you will need to compute 
  # estimates of the two sample variances and the combined variance 
  # in order to complete this function.
  

def pvalue( data1, data2 ) : 
  # You need to write code to determine the pvalue here.  This code will need to
  # include a call to test statistic
  
  
data1 = np.array([-4.62, -5.24, -4.91, -5.07, -5.32, -6.63, -5.63])
data2 = np.array([4.19, 2.73, 5.93, 4.79, 5.88])
print("Null hypothesis: the expectations for the two sampled distributions are the same")
print("Alternative hypothesis: the expectations for for the two sampled distributions are different")
print("The p-value for this hypothsis test is", pvalue( data1, data2 ) )
