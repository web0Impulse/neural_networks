import matplotlib.pyplot as plt
from common_lib import read_float_from_console, read_YN_from_console
# код запускался не под Anaconda, а через консоль Windows так что эта команда была не нужна
#%matplotlib inline

A = 0.4 #коэф. крутизны наклона
A_vis = A #сохраняем изначальное значение A
lr = 0.001 #скорость обучения
epochs = 3000 #эпохи

# обучающая выборка
arr_x = [1.0, 2.0, 3.0, 3.5, 4.0, 6.0, 7.5, 8.5, 9.0]
arr_y = [2.4, 4.5, 5.5, 6.4, 8.5, 11.7, 16.1, 16.5, 18.3]

# прогон по выборке
for i in range(epochs):
    for i_x in range(len(arr_x)):
        x = arr_x[i_x]
        y = A * x
        target_Y = arr_y[i_x]
        E = target_Y - y
        A += lr*(E / x)
print(f'Готовая прямая y = {A} * X')

# поле x_data не используется??
def func_data(x_data):
    # если эта функция возвращает новый массив копирующий arr_y то можно сократить
    #return [arr_y[i] for i in range(len(arr_y))]
    return arr_y.copy()

def func_begin(x_begin):
    return [A_vis*i for i in x_begin]

def func(x):
    return [A*i for i in x]

x_data = arr_x
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
#plt.show()
#это нужно чтобы управление не блокировалось графиком
plt.show(block=False)

# цикл добавлен чтобы для проверки значений не требовалось перезапускать программу
while True:
    ''' функции read_float_from_console и read_YN_from_console добавлены
    из моей библиотеки common_lib они не вернут управление пока не будут
    введены корректные данные'''
    user_x = read_float_from_console("Введите значение ширины X: ")
    user_T = read_float_from_console("Введите значение длины Y: ")
    user_y = A * user_T
    if user_T > user_y:
        print("Это жираф!")
    else:
        print("Это крокодил!")
    ttb = not read_YN_from_console("Проверить еще?(Y/N): ")
    # если пользователь не хочет продолжать прерываем цикл
    if ttb:
        break
