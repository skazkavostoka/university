import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

from data_2 import X_train, y_train, scaler, window_size


model_names = ["RNN_1", "RNN_2", "RNN_3(tanh)",
               "HNN_1", "HNN_2", "HNN_3"]
losses = {}

predictions = {}

for model_name in model_names:
    model = tf.keras.models.load_model(f'{model_name}.h5')
    result = model.predict(X_train).flatten()
    predictions[model_name] = result
    loss = mean_squared_error(y_train, result)
    losses[model_name] = loss

predictions_df = pd.DataFrame(predictions)
print(predictions_df)

# denormalized_predictions = {}
# for model_name in model_names:
#     denormalized_predictions[model_name] = scaler.inverse_transform(
#         np.concatenate((X_train[:, -1, :-1], predictions_df[[model_name]].values), axis=1)
#     )[:, -1]
#
# denormalized_real_close = scaler.inverse_transform(
#     np.concatenate((X_train[:, -1, :-1], y_train.reshape(-1, 1)), axis=1)
# )[:, -1]

for model_name, loss in losses.items():
    print(f'Потери на новых данных для {model_name}: {loss}')

metrics = {}

for model_name in model_names:
    model = tf.keras.models.load_model(f'{model_name}.h5')
    pred = model.predict(X_train).flatten()
    # mse = mean_squared_error(denormalized_real_close, denormalized_predictions[model_name])
    # mae = mean_absolute_error(denormalized_real_close, denormalized_predictions[model_name])
    # mape = mean_absolute_percentage_error(denormalized_real_close, denormalized_predictions[model_name])
    # metrics[model_name] = {'MSE': mse, 'MAE': mae, 'MAPE': mape}

# for model_name, metric in metrics.items():
#     print(f'Метрики для {model_name}: MSE: {metric["MSE"]}, MAE: {metric["MAE"]}, MAPE: {metric["MAPE"]}')

# denormalized_df = pd.DataFrame(denormalized_predictions)
# denormalized_df['Real_Close'] = denormalized_real_close
# denormalized_df.to_csv('denormalized_predictions.csv', index=False)