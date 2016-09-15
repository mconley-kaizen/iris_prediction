# iris_prediction
Small repo to demonstrate value of repo interfaces for model deployment

## Installation

`pip install git+https://github.com/mconley-kaizen/iris_prediction.git#egg=iris_prediction`

## Usage
```python
from sklearn import datasets
import iris_prediction as mymodel

iris = datasets.load_iris()
features = iris.data[0:1]
args = features[0].tolist()

result = mymodel.main(*args)
print result
'setosa'
```
