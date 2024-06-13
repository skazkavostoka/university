from matplotlib import pyplot as plt

from data_3 import data, numeric_features


Q1 = data[numeric_features].quantile(0.25)
Q3 = data[numeric_features].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR #нижняя граница
upper_bound = Q3 + 1.5 * IQR #верхняя граница

anomalies = {}
transliter = {'Open': '"Цена открытия (Open)"', 'High': '"Максимум цены (High)"',
              'Low': '"Минимум цены (Low)"',
              'Close': '"Цена закрытия (Close)"', 'Adj Close': '"Скорр. цена закрытия (Adj close)"'}
for feature in numeric_features:
    anomalies[feature] = data[(data[feature] < lower_bound[feature]) | (data[feature] > upper_bound[feature])]

# Выведем аномалии для каждого признака
for feature, anomaly_data in anomalies.items():
    print(f"Аномалии для признака {transliter[feature]}:")
    print(anomaly_data)


