import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN, Dense, Input, Dropout, LeakyReLU
import matplotlib.pyplot as plt
import time

from data import X, y, window_size, dates


X_train, X_test, y_train, y_test, dates_train, dates_test = train_test_split(X, y, dates, test_size=0.2,
                                                                             random_state=42)

models = {
    "RNN_1": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=64, activation='relu'),
        Dense(units=1)
    ]),
    "RNN_2": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=128, activation='relu', return_sequences=True),
        SimpleRNN(units=64, activation='relu'),
        Dense(units=1)
    ]),
    "RNN_3(tanh)": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=128, activation='relu', return_sequences=True),
        Dropout(0.2),
        SimpleRNN(units=64, activation='relu'),
        Dropout(0.2),
        Dense(units=32, activation='relu'),
        Dense(units=1)
    ]),
    "RNN_4(sigmoid)": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=128, activation='sigmoid', return_sequences=True),
        SimpleRNN(units=64, activation='sigmoid'),
        Dense(units=1)
    ]),
    "RNN_5(LeakyReLU)": tf.keras.Sequential([
        Input(shape=(window_size, X.shape[2])),
        SimpleRNN(units=128, return_sequences=True),
        LeakyReLU(alpha=0.01),
        SimpleRNN(units=64),
        LeakyReLU(alpha=0.01),
        Dense(units=1)
    ])
}

for key, value in models.items():
    print(f"Обучение {key}...")

    value.compile(optimizer='adam', loss='mean_squared_error')

    start_time = time.time()
    history = value.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    training_time = time.time() - start_time

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

    # Сохранение результатов в CSV-файл
    results = pd.DataFrame({'Год': dates_test, 'Реальное значение': y_test, 'Результат прогнозирования': predictions.flatten()})
    results.to_csv(f'res_{key}.csv', index=False)

    print(f'Потери на тестовых данных ({key}): {loss}')
    print(f'Время обучения ({key}): {training_time} с.')
    print(f"Результаты сохранены в файл 'res_{key}.csv'\n")