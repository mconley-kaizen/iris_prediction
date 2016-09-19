import pickle
import numpy as np

from sklearn import svm
from sklearn import datasets

from ..model import MODEL_PATH, persistent_model

def fit():
    """Simple method to fit model and dump pickle"""
    clf = svm.SVC()
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    clf.fit(X, y) 
    pickle.dump(clf, open(MODEL_PATH, 'wb'))


def predict(sepal_length=None, sepal_width=None, 
         petal_length=None, petal_width=None):
    """Main entry point to model

    Parameters
    ----------
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

    Returns
    -------
    name : str
        Expected name of flower as predicted by model
    """
    iris = datasets.load_iris()
    
    X = np.array([[sepal_length, sepal_width, 
                  petal_length, petal_width]])
    
    clf2 = persistent_model
    result = clf2.predict(X)
    name = iris.target_names[result][0]
    return name
