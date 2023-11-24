import numpy as np
from machine_learning.utils.features.normalize import normalize
from machine_learning.utils.features.generate_sinusoids import generate_sinusoids
from machine_learning.utils.features.generate_polynomials import generate_polynomials

def prepare_for_training(data,polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
    num_examples = data.shape[0]
    data_processed = np.copy(data)

    # normalize
    features_mean = 0
    features_deviation = 0
    data_normalized = data_processed
    if normalize_data:
        (
            data_normalized,
            features_mean,
            features_deviation
        ) = normalize(data_processed)

        data_processed = data_normalized

    # generate sinusoid transformed features
    if sinusoid_degree > 0:
        sinusoids = generate_sinusoids(data_normalized, sinusoid_degree)
        data_processed = np.concatenate((data_processed, sinusoids), axis=1)

    # generate polynomial transformed features
    if polynomial_degree > 0:
        polynomials = generate_polynomials(data_normalized, polynomial_degree, normalize_data)
        data_processed = np.concatenate((data_processed, polynomials), axis=1)

    # add one row for intercept.
    data_processed = np.hstack((np.ones((num_examples, 1)), data_processed))
    return data_processed, features_mean, features_deviation

    """
    np.concatenate((a,b), axis) => axis = 0, concat on rows; 1 concat on columns
    np.hstack((a,b)): concat on columns.
    np.vstack((a,b)): concat on rows.
    """