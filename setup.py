from setuptools import setup, find_packages

setup(
      name='iris_prediction',
      version='0.1',
      description='Identify iris from sepal and petal information',
      url='https://github.com/mconley-kaizen/iris_prediction.git',
      packages=find_packages(),
      include_package_data=True,
      package_data={'': ['model.pkl']}
)
