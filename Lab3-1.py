from sklearn.datasets import(load_iris)

iris = load_iris()
data = iris['data']
iris.keys()

import pandas as pd

df = pd.DataFrame.from_records(data, columns = iris['feature_names'])
df['c'] = iris['target']

import matplotlib.pyplot as plt
plt.scatter(df['sepal width (cm)'], df['petal length (cm)'], c = df['c'],cmap = 'Pastel2')

plt.scatter(df['sepal width (cm)'], range(len(df)))