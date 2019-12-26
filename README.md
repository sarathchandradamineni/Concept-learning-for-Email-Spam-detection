# Concept-learning-for-Email-Spam-detection
Concept Learning for Email spam detection dataset
 
I.	IMPORTING DATA 
As a first step data set was imported using pandas library of python, then data set was divided into training and test sets in 80, 20 ratios respectively using train_test_split of sklearn.model_selection.
II.	DISCUSSION
After importing the data using pandas library, data is discretized in to  parts using KbinsDiscretizer of sklearn.preprocessing. Hypothesis function is formed by taking 80% of the data into account and then developing the model from only positive classes. Then, testing is performed on 20% of the whole data, and statistics were analyzed. How the hypothesis function was developed, how the training of the model is done, and what are the results are described in the next sections elaborately.
III.	HYPOTHESIS FORMULATION
After importing and discretizing the data, I start with a most specific hypothesis i.e an empty hypothesis. Such that in the initial stage my hypothesis looks like 
hypothesis_function = [ ]
Then on wards my hypothesis starts leraning by reading each row of training set and start being generalized from specific this process will be done in the following way.
While formulating the hypothesis, in the first step hypothesis will be initialized with the first instance that has 1 in the last column (first spam instance)
While formulating the hypothesis, for every new spam instance, the hypothesis formed up to then is compared with the new instance. If the value in the hypothesis is same as that of the value in the instance for each and every attribute then that value remains as it is in the hypothesis function, otherwise the value for that attribute  in the hypothesis is replaced by the ‘?’. Which states, that attribute in hypoothesis can take any value while testing. Like this the common values for the attributes of spam intances were collected to form hypotheis function.
Assume, data after the discretizing is like
1	0	2	0	4	…….57 values…....	1
1	0	0	0	3	…….57 values…....	1
0	1	0	1	5	…….57 values…....	0
1	0	0	0	4	…….57 values…....	0
1	0	0	0	4	…….57 values…....	1
5	0	2	3	4	…….57 values…....	0
1	0	2	0	3	…….57 values…....	1

Step 1: hypothesis function initializes as first spam instance.
Hypothesis_function = [[1],[0],[2],[0],[4],…57values….]
Step 2: hypothesis function updates from reading second spam instance as 
 Hypothesis_function = [[1],[0],[‘?’],[0],[‘?’],..57values]
Step 3:As 3 and 4 instances are not spam instances, I won’t consider these instaces for formulating the hypothesis so I will consider 5th instace now
Hypotheis_function = [[1],[0],[‘?’],[0],[‘?’],…57values]
Step 4: As 6th instace is not spam I will consider 7th instance for formulating hypothesis so hypothesis_function updates as
Hypothesis_function = [[1],[0],[‘?’],[0],[‘?’]…57values]
Like this by using algorithm 4.1 and 4.3 hypotheis_function will updates [1]. Finally, a hypothesis_function will be formed with 57 inner lists will be formed.
Each attribute can take 5 values, so hypothesis space is 5^57. Possible conjugate concepts are 6^57.
IV.	MODEL TRAINING
Model training was done using only positive class such that hypothesis list contains a list, which contains 57 sub lists. After the training the model every instance is compared with hypothesis lists and check whether the instace contain the values for attributes as hypothesis contains.
V.	TESTING HYPOTHESIS
As we previously divided the training and test data, now we apply hypothesis function over testing data in this way: For every column of each instance, I will compare the attribute of instance with attribute of hypothesis function. If hypothesis function contains ‘?’ for that attribute I will move to next attribute. If hypothesis contains value other than ‘?’ then I will compare the hypothesis with instance, if both hypothesis and instance has same value for that attribute then I will move to next attribute, otherwise I will assign 0 as result for that instance and move to nnext instnace. In this way I will check all the attributes of instances. If instance contains same values for the all the attributes that are present in the hypothesis function then I will assign 1 as result.
VI.	CALCULATING ACCURACY
Hypothesis results and test data results are compared to form a confusion matrix and finally accuracy is calculated using formula ((tp+tn)/(tn + tp + fn + fp) * 100). 
Finally, the statistics are as follows:
Accuracy from the confusion  is  between 85% to 90%, for example, for a particular point of time I got the accuracy 62.391%
and the values are
tp:363, tn:211, fp:6, fn:340

REFERENCES
[1]	P. Flach, “Machine Learning,” p. 416.


 

