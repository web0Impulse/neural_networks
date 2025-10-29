import matplotlib.pyplot as plt
from common_lib import read_float_from_console, read_YN_from_console
import random
# код запускался не под Anaconda, а через консоль Windows так что эта команда была не нужна
#%matplotlib inline

w1 = 0.4 # коэф. крутизны наклона A - первый вход нейрона
w2 = random.uniform(-4, 4) # параметр B - второй вход нейрона
w1_vis = w1 #сохраняем изначальное значение w1
w2_vis = w2 # сохраняем изначальное значение w2
lr = 0.001 #скорость обучения
epochs = 3000 #эпохи
print(f'Начальная прямая: {w1}*X+{w2}')

# обучающая выборка
arr_x1 = [1.0, 2.0, 3.0, 3.5, 4.0, 6.0, 7.5, 8.5, 9.0]
x2 = 1
arr_y = [4.3, 7, 8.0, 10.1, 11.3, 14.2, 18.5, 19.3, 21.4]

# прогон по выборке
for i in range(epochs):
    for j in range(len(arr_x1)):
        x1 = arr_x1[j] # получить x координату
        y = w1 * x1 + w2 # расчет y
        target_Y = arr_y[j] # получить целувую y
        E = -(target_Y - y) # ошибка E
        w1 -= lr*E*x1 # изменение веса w1 с учетом ошибки
        w2 -= lr*E # изменение веса w2 с учетом ошибки
print(f'Готовая прямая y = {w1} * X + {w2}')

# поле x_data не используется??
# def func_data(x_data):
def func_data():
    # если эта функция возвращает новый массив копирующий arr_y то можно сократить
    #return [arr_y[i] for i in range(len(arr_y))]
    return arr_y.copy()

def func_begin(x_begin):
    return [w1_vis*i+w2_vis for i in x_begin]

def func(x):
    return [w1*i+w2 for i in x]

x_data = arr_x1
x_begin = [i for i in range(0,11)]
x = [i for i in range(0,11)]
#y_data = func_data(x_data) #зачем x_data??
y_data = func_data()
y_begin = func_begin(x_begin)
y = func(x)
plt.title("Neuron")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y,label='Входные данные',color='g')
plt.plot(x,y,label='Готовая прямая',color='r')
plt.plot(x,y,label='Начальная прямая',color='b')
plt.legend(loc=2)
plt.scatter(x_data, y_data, color='g',s=10)
plt.plot(x_begin, y_begin, 'b')
plt.plot(x, y, 'r')
plt.grid(True, linestyle='-', color='0.75')
plt.show(block=False)

# цикл добавлен чтобы для проверки значений не требовалось перезапускать программу
while True:
    ''' функции read_float_from_console и read_YN_from_console добавлены
    из моей библиотеки common_lib они не вернут управление пока не будут
    введены корректные данные'''
    user_x = read_float_from_console("Введите значение ширины X: ")
    user_T = read_float_from_console("Введите значение высоты Y: ")
    user_y = w1 * user_x + w2
    if user_T > user_y:
        print("Это жираф!")
    else:
        print("Это крокодил!")
    ttb = not read_YN_from_console("Проверить еще?(Y/N): ")
    # если пользователь не хочет продолжать прерываем цикл
    if ttb:
        break
