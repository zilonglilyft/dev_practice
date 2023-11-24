import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from linear_regression import LinearRegression

data = pd.read_csv('../data/world-happiness-report-2017.csv')
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

x_name = 'Economy..GDP.per.Capita.'
y_name = 'Happiness.Score'
x_train = train_data[[x_name]].values
y_train = train_data[[y_name]].values
x_test = test_data[[x_name]].values
y_test = test_data[[y_name]].values

# Data Viz
plt.figure(figsize = (6,4))
plt.scatter(x_train, y_train, label = 'train data')
plt.scatter(x_test, y_test, label='test data')
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.title('Happiness VS GDP')
plt.legend()
plt.show()

# run linear regression to get theta and cost curve
ulr = LinearRegression(x_train, y_train)
theta, cost_history = ulr.train(alpha = 0.01)
print('loss at the beginning is %f, and the loss at the end is %f' %(cost_history[0], cost_history[-1]))

# plot cost curve
plt.figure(figsize = (6,4))
plt.plot(range(len(cost_history)), cost_history)
plt.xlabel('iterations')
plt.ylabel('costs')
plt.title('Cost curves')
plt.show()

# plot predicted value
samples = 100
x_samples = np.linspace(x_train.min(), x_train.max(),100).reshape(samples,1)
y_preds = ulr.predict(x_samples)
plt.figure(figsize = (6,4))
plt.scatter(x_train, y_train, label = 'train data')
plt.scatter(x_test, y_test, label='test data')
plt.plot(x_samples,y_preds, color = 'g', label='predicted values')
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.title('Happiness VS GDP')
plt.legend()
plt.show()