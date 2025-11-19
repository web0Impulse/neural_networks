import numpy as np

# Вспомогательная функция вывода сигмоидальной функции
def sigm(x):
    return 1 / (1 + np.exp(-x))

class neuron_Net:
    '''
        @param input_num - Кол-во входов
        @param neron_num - Кол-во нейронов
        @param learningrate - Скорость обучения
    '''
    def __init__(self, input_num, neuron_num, learningrate):
        # Задаем матрицу весов размером Кол-во нейронов x Кол-во входов
        # Инициализируем их от -0.5 до 0.5
        self.weights = (np.random.rand(neuron_num, input_num) - 0.5)
        self.lr = learningrate # Скорость обучения
    
    '''
        @param inputs_list - Входной список данных
        @param targets_list - Ответы
    '''
    def train(self, inputs_list, targets_list):
        # Преобразуем входной список данных и ответов в вертикальные матр.
        inputs_x = np.array(inputs_list, ndmin=2).T
        targets_Y = np.array(targets_list, ndmin=2).T

        # Перемножаем матрицу весов и матрицу входных данных
        x = np.dot(self.weights, inputs_x)
        # Вычисляем значение сигмоидальной функции для каждого значения матрицы x
        y = sigm(x)
        
        # Ошибка
        E = -(targets_Y - y)
        # Обновляем веса
        self.weights -= self.lr * np.dot((E * y * (1.0 - y)), np.transpose(inputs_x))

    '''
        @param inputs_list - Входной список данных
    '''
    def query(self, inputs_list):
        # Преобразуем входной список данных в вертикальную матр.
        inputs_x = np.array(inputs_list, ndmin=2).T
        # Перемножаем матрицу весов и матрицу входных данных
        x = np.dot(self.weights, inputs_x)
        # Вычисляем значение сигмоидальной функции для каждого значения матрицы x
        y = sigm(x)
        # Возвращаем полученные вероятности
        return y

# Загружаем тренировочные данные
training_data = open('./numbers.csv', 'r')
training_data_list = training_data.readlines()
training_data.close()

# Загружаем тестовые данные
test_data = open('./test_numbers_0_1.csv', 'r')
test_data_list = test_data.readlines()
test_data.close()

data_input = 15 # Кол-во входов
data_neuron = 2 # Кол-во нейронов
lr = 0.1 # Скорость обучения
n = neuron_Net(data_input, data_neuron, lr) # Объект нейронной сети
epochs = 40000

# Обучение
for e in range(epochs):
    for i in training_data_list:
        all_values = i.split(',')
        # Считываем значения x
        inputs_x = np.asarray(all_values[1:], dtype=float)
        # Инициализируем целевые выходные значения
        target_Y = np.zeros(data_neuron) + 0.01
        if int(all_values[0]) <= 1:
            target_Y[int(all_values[0])] = 0.99

        n.train(inputs_x, target_Y)

# Вывод весовых коэффициентов
print(f'Весовые коэффициенты: \n{n.weights}')

# Проход по обучающей выборке
for i in training_data_list:
    all_values = i.split(',')
    inputs_x = np.asarray(all_values[1:], dtype=float)
    outputs = n.query(inputs_x)
    print(i[0], 'Вероятность:\n', outputs)

# Получаем более читаемый результат
for i in training_data_list:
    all_values = i.split(',')
    inputs_x = np.asarray(all_values[1:], dtype=float)
    outputs = n.query(inputs_x)

    label = np.argmax(outputs)
    if outputs[label] > 0.5 and int(all_values[0]) == label:
        print(i[0], 'Узнал? : Да!')
    else:
        print(i[0], 'Узнал? : Нет!')

# Проход по тестовой выборке
t = 0 # Счетчик номера нуля тестовой выборки
t1 = 0 # Счетчик номера единицы тестовой выборки
for i in test_data_list:
    all_values = i.split(',') # split(',') - раздел строку на символы где запятая "," символ разделения
    inputs_x = np.asarray(all_values[1:], dtype=float)
    t += 1
    outputs = n.query(inputs_x)
    label = np.argmax(outputs)
    if t <= 6:
        print('Вероятность что узнал 0 -',t, '?', outputs[label])
    else:
        t1 += 1
        print('Вероятность что узнал 1 -',t1, '?', outputs[label])

t = 0 # Счетчик номера нуля тестовой выборки
t1 = 0 # Счетчик номера единицы тестовой выборки
for i in test_data_list:
    all_values = i.split(',') # split(',') - раздел строку на символы где запятая "," символ разделения
    inputs_x = np.asarray(all_values[1:], dtype=float)
    # Прогон по сети
    outputs = n.query(inputs_x)
    # индекс самого высокого значения соответствует метке
    label = np.argmax(outputs)
    t += 1
    if outputs[label]>0.5 and int(all_values[0]) == label:
        print(i[0], 'Узнал?:',t, 'Да!')
    else:
        t1 += 1
        print(i[0], 'Узнал?:',t1, 'Нет!')
