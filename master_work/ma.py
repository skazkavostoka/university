import matplotlib.pyplot as plt

from data import data


data['MA100'] = data['Close'].rolling(window=100).mean()
data['MA250'] = data['Close'].rolling(window=250).mean()

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], color='blue', label='Цены закрытия', linewidth=1)
plt.plot(data['Date'], data['MA100'], color='red', label='MA100', linewidth=2)
plt.plot(data['Date'], data['MA250'], color='yellow', label='MA250', linewidth=1)

plt.title('График цены закрытия (Close) и скользящая средняя (MA)')
plt.xlabel('Дата (Date)')
plt.ylabel('Цена закрытия (Close)')
plt.legend()

# Показываем график
plt.show()