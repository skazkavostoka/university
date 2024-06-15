import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

data = yf.download('BTC-USD', start='2022-10-10', end='2024-05-05', interval='1h')
data.to_csv('nasdaq_data.csv')
data = pd.read_csv('nasdaq_data.csv')

print(data)
print(data.describe())

data['Datetime'] = pd.to_datetime(data['Datetime'])

data = data.dropna()
data = data.rename(columns={'Open': 'Open', 'High': 'High', 'Low': 'Low',
                                          'Close': 'Close', 'Adj Close': 'Adj Close', 'Volume': 'Volume'})

data = data.drop(columns=['Volume'])

# scaler = MinMaxScaler()
# data[['Open', 'High', 'Low', 'Close', 'Adj Close']] =\
#     scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Adj Close']])
#
# window_size = 14
#
# input_sequences = []
# output_sequences = []
# dates = []
#
# for i in range(len(data) - window_size):
#     input_seq = data[['Open', 'High', 'Low', 'Close', 'Adj Close']].iloc[i:i + window_size].values
#     output_seq = data['Close'].iloc[i + window_size]
#     date = data['Datetime'].iloc[i + window_size]  # Сохранение соответствующей даты
#
#     input_sequences.append(input_seq)
#     output_sequences.append(output_seq)
#     dates.append(date)
#
# X = np.array(input_sequences)
# y = data['Close'][window_size:].values

numeric_features = ['Open', 'High', 'Low', 'Close', 'Adj Close']