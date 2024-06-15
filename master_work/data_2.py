import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Загрузка данных
data_path = 'C:\\Users\\Артем\\Desktop\\University\\master_work_data.csv'
data = pd.read_csv(data_path)

data['Date'] = pd.to_datetime(data['Date'])
data = data.dropna()

# Нормализация данных
scaler = MinMaxScaler()
data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])
data = data.drop(columns=['Volume'])

window_size = 14

# Создание последовательностей
input_sequences = []
output_sequences = []
dates = []

for i in range(len(data) - window_size):
    input_seq = data[['Open', 'High', 'Low', 'Close', 'Adj Close']].iloc[i:i+window_size].values
    output_seq = data['Close'].iloc[i+window_size]
    date = data['Date'].iloc[i+window_size]

    input_sequences.append(input_seq)
    output_sequences.append(output_seq)
    dates.append(date)

X = np.array(input_sequences)
y = np.array(output_sequences)

numeric_features = ['Open', 'High', 'Low', 'Close', 'Adj Close']

# Функции для аугментации данных
def time_shift(data, shift):
    return np.roll(data, shift, axis=0)

def add_noise(data, noise_factor):
    noise = np.random.randn(*data.shape) * noise_factor
    return data + noise

def augment_time_series(data, shift_range=5, noise_factor=0.09):
    augmented_data = []

    # Оригинальные данные
    augmented_data.append(data)

    # Сдвиг по времени
    for shift in range(1, shift_range + 1):
        augmented_data.append(time_shift(data, shift))
        augmented_data.append(time_shift(data, -shift))

    # Добавление шума
    augmented_data.append(add_noise(data, noise_factor))

    return np.concatenate(augmented_data, axis=0)

# Пример использования
X_train = augment_time_series(X)
y_train = np.tile(y, (X_train.shape[0] // X.shape[0], 1)).flatten()