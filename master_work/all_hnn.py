import tensorflow as tf
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import SimpleRNN, LSTM, Dense, Dropout, Input
import time
import psutil
import os
import pandas as pd
from data import X, y, window_size, dates, numeric_features


X_train, X_test, y_train, y_test, dates_train, dates_test = train_test_split(X, y, dates, test_size=0.2,
                                                                             random_state=42)


models = {
    "HNN_1": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=64, activation='relu', return_sequences=True),
        LSTM(units=32, activation='relu'),
        Dense(units=1)
    ]),
    "HNN_2": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=128, activation='relu', return_sequences=True),
        Dropout(0.2),
        LSTM(units=64, activation='relu'),
        Dense(units=1)
    ]),
    "HNN_3": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=64, activation='tanh', return_sequences=True),
        Dropout(0.2),
        LSTM(units=32, activation='tanh'),
        Dropout(0.2),
        Dense(units=1)
    ]),
    "HNN_4": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=128, activation='relu', return_sequences=True),
        Dropout(0.15),
        LSTM(units=64, activation='relu', return_sequences=True),
        Dropout(0.15),
        LSTM(units=32, activation='relu'),
        Dropout(0.15),
        Dense(units=1)
    ]),
    "HNN_5": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=64, activation='tanh', return_sequences=True),
        Dropout(0.15),
        LSTM(units=64, activation='tanh', return_sequences=True),
        Dropout(0.2),
        LSTM(units=32, activation='tanh'),
        Dropout(0.15),
        Dense(units=1)
    ])
}

for key, value in models.items():
    print(f'Обучение {key}')
    value.compile(optimizer='adam', loss='mean_squared_error')

    process = psutil.Process(os.getpid())
    memory_before = process.memory_info().rss
    cpu_usage_before = psutil.cpu_percent(interval=True)

    start_time = time.time()
    history = value.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    training_time = time.time()

    memory_after = process.memory_info().rss
    cpu_usage_after = psutil.cpu_percent(interval=None)
    execution_time = training_time - start_time

    loss = value.evaluate(X_test, y_test)
    predictions = value.predict(X_test)

    value.save(f'{key}.h5')

    plt.figure(figsize=(14, 7))
    plt.plot(dates_test[:100], y_test[:100], 'bo', label='Реальное значение', markersize=5)
    plt.plot(dates_test[:100], predictions[:100], 'ro', label=f'Результат прогнозирования {key}', markersize=5)
    plt.title(f'Реальные значения и результат прогноза (Первые 100 значений) - {key}')
    plt.xlabel('Год')
    plt.ylabel('Значение')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

    results = pd.DataFrame(
        {'Год': dates_test, 'Реальное значение': y_test, 'Результат прогнозирования': predictions.flatten()})
    results.to_csv(f'res_{key}.csv', index=False)

    print(f"Время выполнения: {execution_time} секунд")
    print(f"Потребление памяти: {(memory_after - memory_before) / 1024 ** 2} MB")
    print(f"Использование CPU: {cpu_usage_before-cpu_usage_after}%")

    print(f'Потери на тестовых данных ({key}): {loss}')










