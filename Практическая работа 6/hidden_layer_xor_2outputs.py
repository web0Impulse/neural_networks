import numpy as np
from hidden_layer_neuron_Net import neuron_Net
# from gpt_variant import neuron_Net
# Загружаем тренировочные данные
training_data = open('./train_data.csv', 'r')
training_data_list = training_data.readlines()
training_data.close()

data_input = 2 # Кол-во входов
data_neuron = 4 # Кол-во нейронов
data_output = 2 # Кол-во выходов
lr = 0.09 # Скорость обучения
n = neuron_Net(data_input, data_neuron, data_output, lr) # Объект нейронной сети
epochs = 80000

# Обучение
for e in range(epochs):
    for i in training_data_list:
        all_values = i.split(',')
        # Считываем значения x
        inputs_x = np.asarray(all_values[1:], dtype=int)
        # Инициализируем целевые выходные значения
        #target_Y = int(all_values[0])
        target_Y = np.zeros(data_output) + 0.01
        target_Y[int(all_values[0])] = 0.99
        n.train(inputs_x, target_Y)

# Вывод весовых коэффициентов
print(f'Весовые коэффициенты: \n{n.weights}')

# Проход по обучающей выборке
for i in training_data_list:
    all_values = i.split(',')
    inputs_x = np.asarray(all_values[1:], dtype=int)
    outputs = n.query(inputs_x)
    print(f'{all_values[1]} XOR {all_values[2]}', outputs)