import matplotlib.pyplot as plt
from common_lib import read_float_from_console, read_YN_from_console
import random
import numpy as np
# код запускался не под Anaconda, а через консоль Windows так что эта команда была не нужна
#%matplotlib inline

def log_and_neuron_test():
    print('Логическое И')
    w1 = random.uniform(-4, 4) # коэф. крутизны наклона A - первый вход нейрона
    w2 = random.uniform(-4, 4) # параметр B - второй вход нейрона
    w3 = random.uniform(-4, 4) # свободный параметр w3
    # добавил еще два свобоных параметра просто проверял что можно добавить сколько угодно и они ни на, что не повлияют
    w4 = random.uniform(-4, 4)
    w5 = random.uniform(-4, 4)
    w1_vis = w1 #сохраняем изначальное значение w1
    w2_vis = w2 # сохраняем изначальное значение w2
    w3_vis = w3 # сохраняем изначальное значение w3
    w4_vis = w4
    w5_vis = w5
    print(f'Начальные весовые коэффициенты: \n\t{w1}, \n\t{w2}, \n\t{w3}, \n\t{w4}, \n\t{w5}')
    lr = 0.001 #скорость обучения
    epochs = 5000 #эпохи
    bias = 3 # порог единичной функции активации

    # массив данных логического И
    log_and = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ])

    # прогон по выборке
    for i in range(epochs):
        for j in range(len(log_and)):
            x1 = log_and[j, 0] # получить x1
            x2 = log_and[j, 1] # получить x2
            y = w1 * x1 + w2 * x2 + w3 + w4 + w5 # взвешенная сумма
            target_Y = log_and[j, 2] # целевая Y
            if y >= bias:
                y = 1
                E = -(target_Y - y) # ошибка E
                w1 -= lr*E*x1
                w2 -= lr*E*x2
                w3 -= lr*E
                w4 -= lr*E
                w5 -= lr*E
            else:
                y = 0
                E = -(target_Y - y) # ошибка E
                w1 -= lr*E*x1
                w2 -= lr*E*x2
                w3 -= lr*E
                w4 -= lr*E
                w5 -= lr*E
    print(f'Обученные весовые коэффициенты: \n\t{w1}, \n\t{w2}, \n\t{w3}, \n\t{w4}, \n\t{w5}')

    print('Проверка логической функции (И):')
    print('\t0, 0,', int(0*w1 + 0*w2 + w3 + w4 + w5>=3))
    print('\t1, 0,', int(1*w1 + 0*w2 + w3 + w4 + w5>=3))
    print('\t0, 1,', int(0*w1 + 1*w2 + w3 + w4 + w5>=3))
    print('\t1, 1,', int(1*w1 + 1*w2 + w3 + w4 + w5>=3))

def log_or_neuron_test():
    print('Логическое ИЛИ')
    w1 = random.uniform(-4, 4) # коэф. крутизны наклона A - первый вход нейрона
    w2 = random.uniform(-4, 4) # параметр B - второй вход нейрона
    w1_vis = w1 #сохраняем изначальное значение w1
    w2_vis = w2 # сохраняем изначальное значение w2
    print(f'Начальные весовые коэффициенты: \n\t{w1}, \n\t{w2}')
    lr = 0.001 #скорость обучения
    epochs = 5000 #эпохи
    bias = 3 # порог единичной функции активации

    # массив данных логического И
    log_or = np.array([
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ])

    # прогон по выборке
    for i in range(epochs):
        for j in range(len(log_or)):
            x1 = log_or[j, 0] # получить x1
            x2 = log_or[j, 1] # получить x2
            y = w1 * x1 + w2 * x2 # взвешенная сумма
            target_Y = log_or[j, 2] # целевая Y
            if y >= bias:
                y = 1
                E = -(target_Y - y) # ошибка E
                w1 -= lr*E*x1
                w2 -= lr*E*x2
            else:
                y = 0
                E = -(target_Y - y) # ошибка E
                w1 -= lr*E*x1
                w2 -= lr*E*x2
    print(f'Обученные весовые коэффициенты: \n\t{w1}, \n\t{w2}')

    print('Проверка логической функции (ИЛИ):')
    print('\t0, 0,', int(0*w1 + 0*w2>=bias))
    print('\t1, 0,', int(1*w1 + 0*w2>=bias))
    print('\t0, 1,', int(0*w1 + 1*w2>=bias))
    print('\t1, 1,', int(1*w1 + 1*w2>=bias))

def numbers_recognize_test():
    training_data = open('./numbers.csv', 'r')
    training_data_list = training_data.readlines()
    training_data.close()
    test_data = open('./test_numbers.csv', 'r')
    test_data_list = test_data.readlines()
    test_data.close()


    weights = np.zeros(15) # инициализация весов
    epochs = 1000 # эпохи
    bias = 3
    lr = 1

    for i in range(epochs):
        for j in training_data_list:
            all_values = j.split(',')
            inputs_x = np.asarray(all_values[1:], dtype=int)
            target_Y = int(all_values[0])
            if target_Y == 0:
                target_Y = 1
            else:
                target_Y = 0
            y = np.sum(weights * inputs_x)
            if y >= bias:
                y = 1
                E = -(target_Y - y)
                weights -= lr * E * inputs_x
            else:
                y = 0
                E = -(target_Y - y)
                weights -= lr * E * inputs_x

    print(f'Весовые коэффициенты: \n{weights}')
    for i in training_data_list:
        all_values = i.split(',')
        inputs_x = np.asarray(all_values[1:], dtype=int)
        print(f'{i[0]} это 0? ', np.sum(weights * inputs_x) >= bias)

    # Проход по тестовой выборке
    t = 0 # Счетчик
    for i in test_data_list:
        all_values = i.split(',')
        inputs_x = np.asarray(all_values[1:], dtype=int)
        t += 1
        print(f'Узнал 0 – {t} ? ', np.sum(weights * inputs_x) >= bias)

log_and_neuron_test()
log_or_neuron_test()
numbers_recognize_test()
