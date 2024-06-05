import matplotlib.pyplot as plt
import seaborn as sns
from data import data


feature1 = 'Open'
feature2 = 'Close'

plt.figure(figsize=(8, 6))
sns.scatterplot(x=data[feature1], y=data[feature2])
plt.title('Диаграмма рассеяния между признаками {} и {}'.format(feature1, feature2))
plt.xlabel(feature1)
plt.ylabel(feature2)
plt.grid(True)
plt.show()