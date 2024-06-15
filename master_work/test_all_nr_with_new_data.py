import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split

from data_3 import X, y, window_size, btc_data, dates

model_names = ["RNN_1", "RNN_2", "RNN_3(tanh)",
               "HNN_1", "HNN_2", "HNN_3"]
losses = {}

predictions = {}

for model_name in model_names:
    model = tf.keras.models.load_model(f'{model_name}.h5')
    result = model.predict(X).flatten()
    predictions[model_name] = result
    loss = mean_squared_error(y, result)
    losses[model_name] = loss

# Преобразование результатов в DataFrame для удобства анализа
predictions_df = pd.DataFrame(predictions)
predictions_df['Datetime'] = btc_data['Datetime'][window_size:].values
predictions_df['Real_Close'] = btc_data['Close'][window_size:].values

# Вывод результатов
print(predictions_df)

for model_name, loss in losses.items():
    print(f'Потери на новых данных для {model_name}: {loss}')

predictions_df.to_csv('nasdaq_predictions.csv', index=False)

metrics = {}

for model_name in model_names:
    model = tf.keras.models.load_model(f'{model_name}.h5')
    pred = model.predict(X).flatten()
    mse = mean_squared_error(y, pred)
    mae = mean_absolute_error(y, pred)
    mape = mean_absolute_percentage_error(y, pred)
    metrics[model_name] = {'MSE': mse, 'MAE': mae, 'MAPE': mape}

# Вывод метрик
for model_name, metric in metrics.items():
    print(f'Метрики для {model_name}: MSE: {metric["MSE"]}, MAE: {metric["MAE"]}, MAPE: {metric["MAPE"]}')