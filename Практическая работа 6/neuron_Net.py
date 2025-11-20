import numpy as np

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
        y = 1 / (1 + np.exp(-x))
        
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
        y = 1 / (1 + np.exp(-x))
        # Возвращаем полученные вероятности
        return y