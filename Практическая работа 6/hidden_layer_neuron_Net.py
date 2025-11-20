import numpy as np

def sigmoid(x):
    # Для больших отрицательных x возвращает 0 без вызова exp
    out = np.empty_like(x)
    mask = x >= 0
    out[mask] = 1 / (1 + np.exp(-x[mask]))
    exp_x = np.exp(x[~mask])
    out[~mask] = exp_x / (1 + exp_x)
    return out

class neuron_Net:
    '''
        @param input_num - Кол-во входов
        @param neuron_num - Кол-во нейронов
        @param output_num - Кол-во выходов
        @param learningrate - Скорость обучения
    '''
    def __init__(self, input_num, neuron_num, output_num,learningrate):
        # Инициализируем веса
        self.weights = (np.random.rand(neuron_num, input_num))
        self.weights_out = (np.random.rand(output_num, neuron_num))
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
        x1 = np.dot(self.weights, inputs_x)
        # Вычисляем значение сигмоидальной функции для каждого значения матрицы x
        y1 = 1 / (1 + np.exp(-x1))
        
        x2 = np.dot(self.weights_out, y1)

        # Ошибка
        E = -(targets_Y - x2)
        E_hidden = np.dot(self.weights_out.T, E)
        # Обновляем веса
        self.weights_out -= self.lr * np.dot((E * x2), np.transpose(y1))
        self.weights -= self.lr * np.dot((E_hidden * y1 * (1.0 - y1)), np.transpose(inputs_x))

    '''
        @param inputs_list - Входной список данных
    '''
    def query(self, inputs_list):
        # Преобразуем входной список данных в вертикальную матр.
        inputs_x = np.array(inputs_list, ndmin=2).T
        # Перемножаем матрицу весов и матрицу входных данных
        x1 = np.dot(self.weights, inputs_x)
        # Вычисляем значение сигмоидальной функции для каждого значения матрицы x
        y1 = 1 / (1 + np.exp(-x1))

        x2 = np.dot(self.weights_out, y1)
        # Возвращаем полученные вероятности
        return x2