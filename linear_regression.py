import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics



#	Given a data set of the form
#	((original photo, original age, target age), target photo)
#	We take some part of the data set and use it to train a linear model
#	We reserve some of the data to test it afterwards


#	photos should be npy
#	input = lists of the data (should all be the same size and flattened)
#	output = linear regression interpolator
#	note that data can come from multiple people, the more data, the more accurate
def findInterpolator(start_photos, start_ages, target_ages, target_photos):

	X = []
	Y = []

	for i in range(len(start_photos)):
		X.append(np.array([start_photos[i], start_ages[i], target_ages[i]]))
		Y.append(target_photos[i])
	

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

	regressor = LinearRegression()  
	regressor.fit(X_train, Y_train)

	#print("accuracy = " + str(testModel(X_train, Y_train, regressor)))

	return regressor, X_test, Y_test

#	input = list of data to test on and regressor to test
#	output = accuracy in MSE
def testModel(X, Y, regressor):

	Y_pred = regressor.predict (X)

	MSE = metrics.mean_squared_error (Y, Y_pred)

	return MSE





# TESTING FROM HERE DOWN REMOVE THIS DURING USE #


data1 = []
data2 = []
data3 = []

results = []
for i in range(1000):
	data1.append(np.array(np.random.rand()))
	data2.append(np.array(np.random.rand()))
	data3.append(np.array(np.random.rand()))
	results.append(np.array([np.power(data1[i], 1),data2[i], data3[i]]))

print(np.around(data1, decimals=3))
print(np.around(data2, decimals=3))
print(np.around(data3, decimals=3))
print(np.around(results, decimals=3))

regressor, X_test, Y_test = findInterpolator(data1, data2, data3, results)

print (testModel(X_test, Y_test, regressor))


