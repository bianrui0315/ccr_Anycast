# classification using random forest algorithm
# input: datasets
# output: classification results


# Importing the required packages
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_fscore_support

# Function importing Dataset
def importdata():
	balance_data = pd.read_csv(
'datasets_prefix_N_P1_P2_MD_ML.txt',
	sep= ',', header = None)
	
	# Printing the dataswet shape
	print ("Dataset Lenght: ", len(balance_data))
	print ("Dataset Shape: ", balance_data.shape)
	
	# Printing the dataset obseravtions
	print ("Dataset: ",balance_data.head())
	return balance_data

# Function to split the dataset
def splitdataset(balance_data):

	# Seperating the target variable
	X = balance_data.values[:, 2:balance_data.shape[1]]
	Y = balance_data.values[:, 0]

	# Spliting the dataset into train and test
	X_train, X_test, y_train, y_test = train_test_split( 
	X, Y, test_size = 0.33, random_state = 100)
	
	return X, Y, X_train, X_test, y_train, y_test
	
# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):

	# Creating the classifier object
	clf_gini = RandomForestClassifier(criterion = "gini",
			random_state = 90,max_depth=18, min_samples_leaf=1 , class_weight={"A":4, "U":1})

	# Performing training
	clf_gini.fit(X_train, y_train)
	return clf_gini
	
# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):

	# Decision tree with entropy
	clf_entropy = RandomForestClassifier(
			criterion = "entropy", random_state = 90,
			max_depth = 18, min_samples_leaf = 1 , class_weight={"A":4, "U":1})

	# Performing training
	clf_entropy.fit(X_train, y_train)
	return clf_entropy


# Function to make predictions
def prediction(X_test, clf_object):

	# Predicton on test with giniIndex
	y_pred = clf_object.predict(X_test)
	print("Predicted values:")
	print(y_pred)
	return y_pred
	
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
	
	print("Confusion Matrix: ",
		confusion_matrix(y_test, y_pred))
	
	print ("Accuracy : ",
	accuracy_score(y_test,y_pred)*100)
	
	print("Report : ",
	classification_report(y_test, y_pred))
	print(precision_recall_fscore_support(y_test, y_pred)[0][0],precision_recall_fscore_support(y_test, y_pred)[1][0], precision_recall_fscore_support(y_test, y_pred)[2][0])
	print(precision_recall_fscore_support(y_test, y_pred)[0][1],precision_recall_fscore_support(y_test, y_pred)[1][1], precision_recall_fscore_support(y_test, y_pred)[2][1])
	

def get_importance(X_train, clf_object):
	importances=clf_object.feature_importances_
	#std = np.std([tree.feature_importances_ for tree in clf_object.estimators_],
             #axis=0)
	indices = np.argsort(importances)[::-1]
	print("Feature ranking:")
	for f in range(X_train.shape[1]):
		print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
		
	plt.figure()
	plt.title("Feature importances")
	plt.bar(range(X_train.shape[1]), importances[indices],
			color="r")
	plt.xticks(range(X_train.shape[1]), indices)
	plt.xlim([-1, X_train.shape[1]])
	plt.xlabel('feature')
	plt.ylabel('importance')
	plt.show()
	
# Driver code
def main():
	
	# Building Phase
	data = importdata()
	X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
	clf_gini = train_using_gini(X_train, X_test, y_train)
	clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
	prefix=data.values[:,1]
	# Operational Phase
	print("Results Using Gini Index:")
	
	# Prediction using gini
	y_pred_gini = prediction(X_test, clf_gini)
	cal_accuracy(y_test, y_pred_gini)
	
	print("Results Using Entropy:")
	# Prediction using entropy
	y_pred_entropy = prediction(X_test, clf_entropy)
	cal_accuracy(y_test, y_pred_entropy)
	'''
	print("gini")
	get_importance(X_train,clf_gini)
	print("entropy")
	get_importance(X_train,clf_entropy)
'''
	y_pred_gini_all = prediction(X, clf_gini)
	cal_accuracy(Y, y_pred_gini_all)
	y_pred_entropy_all = prediction(X, clf_entropy)
	cal_accuracy(Y, y_pred_entropy_all)
	results_entropy=np.column_stack([prefix,Y,y_pred_entropy_all])
	df_entropy=pd.DataFrame(results_entropy)
	df_entropy.to_csv("RF_gini_true_predicts_en_5.csv")
	df_entropy.to_csv("RF_gini_true_preficts_en_5.txt",sep='\t')
	results_gini=np.column_stack([prefix,Y,y_pred_gini_all])
	df_gini=pd.DataFrame(results_gini)
	df_gini.to_csv("RF_gini_true_predicts_gi_5.csv")
	df_gini.to_csv("RF_gini_true_preficts_gi_5.txt",sep='\t')
	
# Calling main function
if __name__=="__main__":
	main()
