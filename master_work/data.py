import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


data_path = 'C:\\Users\\Артем\\Desktop\\University\\master_work_data.csv'

data = pd.read_csv(data_path)

data['Date'] = pd.to_datetime(data['Date'])
data = data.dropna()

scaler = MinMaxScaler()
data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']] = scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])
data = data.drop(columns=['Volume'])

window_size = 14

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
