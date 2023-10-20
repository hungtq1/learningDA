import pandas
from sklearn import linear_model
# sơ ché phân loại dữ liệu
cars = pandas.read_csv("data2.csv")
ohe_cars = pandas.get_dummies(cars['Car'].explode())

X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
print(X)
y = cars['CO2']
print(y)
regr = linear_model.LinearRegression()
regr.fit(X,y)
print(regr.coef_)

##predict the CO2 emission of a Volvo where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
print(predictedCO2)