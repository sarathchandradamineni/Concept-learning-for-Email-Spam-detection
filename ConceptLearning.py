import pandas as pd

dataset = pd.read_csv('spambase.data')

from sklearn.model_selection import train_test_split
training_data, testing_data = train_test_split(dataset,test_size=0.2)

testing_data_input = testing_data.iloc[:,:-1].values
testing_data_output = testing_data.iloc[:,-1].values
training_data_input = training_data.iloc[:,:-1].values
training_data_output = training_data.iloc[:,-1].values
training_data_list = training_data.values.tolist()
testing_data_list = testing_data.values.tolist()
training_data_input_list = training_data_input.tolist()
training_data_output_list = training_data_output.tolist()
testing_data_input_list = testing_data_input.tolist()
testing_data_output_list = testing_data_output.tolist()

#Discretizing the data  
from sklearn.preprocessing import KBinsDiscretizer
est = KBinsDiscretizer(n_bins = 5, encode='ordinal', strategy='uniform')
est.fit(training_data_input_list)
training_data_discretized = est.transform(training_data_input_list)
est2 = KBinsDiscretizer(n_bins= 5, encode='ordinal', strategy='uniform')
est2.fit(testing_data_input_list)
testing_data_input_discretized = est2.transform(testing_data_input_list)

testing_data_input_discretized_list = testing_data_input_discretized.tolist()


#print(training_data.info())
hypothesis = []
for i in range(57):
    hypothesis.append([])

#function to check whether the element present in the list or not
def checkElementInList(val,list_hypo):
    for each_val in list_hypo:
        if val == each_val:
            return True
    return False

#Preparing the hypothesis function
for i in range(len(training_data_list)):
    if training_data_list[i][-1] == 1:
        for j in range(57):
            if not checkElementInList(training_data_discretized[i][j],hypothesis[j]):
                if len(hypothesis[j]) != 0:
                    hypothesis[j].pop()
                    hypothesis[j].append('?')
                else:
                    hypothesis[j].append(training_data_discretized[i][j])
num = 0                
for i in range(57):
    if hypothesis[i][0] != '?':
        num += 1

print('number of unique values')
print(num)

results = []

for i in range(len(testing_data_list)):
    for j in range(57):
        if hypothesis[j][0] != '?':
            if hypothesis[j][0] != testing_data_input_discretized_list[i][j]:
                results.append(0)
                break
        if j == 56:
            results.append(1)

#out put statistics
from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(results,testing_data_output_list).ravel()
print('From confusion matrix accuracy percentage is')
print((tp+tn)/(tn + tp + fn + fp) * 100)
            
                
