import numpy as np
from machine_learning.utils.features.prepare_for_training import prepare_for_training


class LinearRegression:
    def __init__(self, data, labels, polynomial_degree = 0, sinusoid_degree = 0, normalize_data = True):
        """
        1. standardize the raw data
        2. initiate the theta
        """
        (self.data,
         self.features_mean,
         self.features_deviation) = prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data)

        self.labels = labels
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data
        self.theta = np.zeros((self.data.shape[1],1))

    @staticmethod
    def hypothesis(data, theta):
        """
        calculate the predicted value
        """
        return np.dot(data, theta)

    def gradient_step(self, alpha):
        """
        update the one-step theta value based on the formula
        """
        num_examples = self.data.shape[0]
        prediction = LinearRegression.hypothesis(self.data, self.theta)
        delta = prediction - self.labels
        theta = self.theta
        theta = theta - alpha * (1/num_examples) * (np.dot(delta.T, self.data)).T
        self.theta = theta

    def cost_function(self, data, labels):
        """
        formula to calculate the cost function
        """
        num_examples = data.shape[0]
        delta = LinearRegression.hypothesis(data, self.theta) - labels
        cost = (1/2)*np.dot(delta.T, delta)/num_examples
        return cost[0][0]

    def gradient_descent(self,alpha,num_iterations):
        """
        execute the gradient descent processes and store the costs along the iterations
        """
        cost_history = []
        for _ in range(num_iterations):
            self.gradient_step(alpha)
            cost_history.append(self.cost_function(self.data, self.labels))
        return cost_history

    def train(self,alpha,num_iterations = 500):
        cost_history = self.gradient_descent(alpha, num_iterations)
        return self.theta, cost_history

    def get_cost(self, data, labels):
        """
        get cost for testing data
        """
        data_processed = prepare_for_training(
            data,
            self.polynomial_degree,
            self.sinusoid_degree,
            self.normalize_data
        )[0]
        return self.cost_function(data_processed,labels)

    def predict(self, data):
        """
        get predicted value for test data
        """
        data_processed = prepare_for_training(
            data,
            self.polynomial_degree,
            self.sinusoid_degree,
            self.normalize_data
        )[0]
        return LinearRegression.hypothesis(data_processed,self.theta)




