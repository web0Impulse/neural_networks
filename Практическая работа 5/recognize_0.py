import numpy as np

# Вспомогательная функция вычисления стандартного отклонения
def bco(arr):
    average = np.mean(arr)
    sum = 0
    for i in arr:
        sum += (i - average)**2
    bco = np.sqrt(sum) / np.sqrt(len(arr) - 1)
    return bco

# Вспомогательная функция вычисления значения сигмоидальной функции
def sigm(x):
    return 1 / (1 + np.exp(-x))

# Загружаем тренировочные данные
training_data = open('./numbers.csv', 'r')
training_data_list = training_data.readlines()
training_data.close()
# Загружаем тестовые данные
test_data = open('./test_numbers_0.csv', 'r')
test_data_list = test_data.readlines()
test_data.close()

weights = np.zeros(15) # Инициализация весов
epochs = 50000 # Эпохи
lr = 0.1 # Скорость обучения

# Обучение
for i in range(epochs):
    for j in training_data_list:
        all_values = j.split(',')
        inputs_x = np.asarray(all_values[1:], dtype=float)
        target_Y = int(all_values[0])
        if target_Y == 0:
            target_Y = 1
        else:
            target_Y = 0

        # Взвешенная сумма
        x = np.sum(weights * inputs_x)
        # Сигм. функция 
        y = sigm(x)
        E = -(target_Y - y)
        # Смена весов по сигмоидальной функц. акт.
        weights -= lr * E * y * (1.0 - y) * inputs_x

print(f'Весовые коэффициенты: \n{weights}')

# Проход по обучающей выборке
for i in training_data_list:
    all_values = i.split(',')
    inputs_x = np.asarray(all_values[1:], dtype=float)
    # Взвешенная сумма
    x = np.sum(weights * inputs_x)
    # Вывод по сигм.
    print(f'{i[0]} Вероятность, что это 0: ', sigm(x))

# Проход по тестовой выборке
t = 0 # Счетчик
my_results = np.array([]) # Массив для записи вероятностей
for i in test_data_list:
    all_values = i.split(',')
    inputs_x = np.asarray(all_values[1:], dtype=float)
    t += 1
    # Взвешенная сумма
    x = np.sum(weights * inputs_x)
    my_results = np.append(my_results, sigm(x))
    print(f'{t}. Вероятность, что узнал 0 - ', sigm(x))

# Узнаем стандартное отклонение моих весов
print(f'Стандартное отклонение моих весов: {bco(weights)}')
# Узнаем стандартное отклонение весов в примере
test_weights_array = np.array([
    0.44879589, -0.18430999, -0.02023563, 2.0697523, -0.07193334,
    0.17307025, -2.1606589, -5.35195696, -1.45815401, 3.73096992,
    -1.31490847, 0.26365056, 0.52117981, 0.94419683, -4.20017402
    ])
print(f'Стандартное отклонение тестовых весов: {bco(test_weights_array)}')

# Узнаем стандартное отклонение узнавания 0 у моей модели
print(f'Узнаем стандартное отклонение узнавания 0 у моей модели: {bco(my_results)}')
# Узнаем стандартное отлонение узнавания 0 у тестовой модели
test_results = np.array([
    0.964467249281,
    0.98802530455,
    0.614232538622,
    0.905331401561,
    0.81811184231,
    0.74017734823
])
print(f'Узнаем стандартное отклонение узнавания 0 у тестовой модели: {bco(test_results)}')