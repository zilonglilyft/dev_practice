import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from linear_regression import LinearRegression

data = pd.read_csv('../data/non-linear-regression-x-y.csv')

x = data['x'].values.reshape((data.shape[0], 1))
y = data['y'].values.reshape((data.shape[0], 1))

plt.plot(x,y)
plt.show()

nlr = LinearRegression(x, y, polynomial_degree=15, sinusoid_degree=15, normalize_data=True)

(theta, cost_history) = nlr.train(alpha=0.02, num_iterations= 5000)

print("Beginning cost: {:.2f}".format(cost_history[0]))
print("Ending cost: {:.2f}".format(cost_history[-1]))

plt.plot(range(5000), cost_history)
plt.xlabel('Interations')
plt.ylabel('Cost')
plt.title('Gradient Descent Progress')
plt.show()

x_predictions = np.linspace(x.min(),x.max(),1000).reshape(1000,1)
y_predictions = nlr.predict(x_predictions)

plt.scatter(x,y,label = 'Training Dataset')
plt.plot(x_predictions,y_predictions,'r',label = 'Prediction')
plt.show()

