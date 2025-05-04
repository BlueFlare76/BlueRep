
import matplotlib.pyplot as plt

from statsmodels.datasets import nile


data = nile.load_pandas().data


data.set_index('year', inplace=True)

plt.figure(figsize=(10, 6))

plt.plot(data['volume'], label='Годовой расход воды в реке Нил')

plt.title('Годовой расход воды в реке Нил (1871-1970)')

plt.xlabel('Год')

plt.ylabel('Годовой расход воды (кубические гектометры)')

plt.legend()

plt.grid(True)

plt.show()