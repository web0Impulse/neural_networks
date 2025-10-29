% задание размера матрицы 128x127
matr_rows = 128;
matr_cols = 127;
% интервал генерации случайных чисел от 10 до 200
matr_start_interval = 10;
matr_end_interval = 200;
% генерация матрицы
dif = matr_end_interval - matr_start_interval;
result_matr = dif * rand(matr_rows, matr_cols) + matr_start_interval;
% создание вектора с первым числом 10, шагом 2 и длиной 127
last_number = (127-1)*2+10; % поиск последнего элемента
vect1 = 10:2:last_number;
% замены строки 35 на первый вектор
result_matr(35,:) = vect1;
% создание вектора с первым числом 10, шагом 2 и длиной 128
last_number = (128-1)*2+10; % поиск последнего элемента
vect2 = (10:2:last_number)';
% вставка второго вектора в 10 столбец
result_matr = [result_matr(:,1:3),vect2,result_matr(:,4:end)];
% разбиение матрицы по строкам на две равные части
matr1 = result_matr(1:matr_rows/2,:);
matr2 = result_matr(matr_rows/2 + 1:matr_rows,:);
% перемножение матриц
result_matr = matr1 * matr2';
% вывод куска матрицы размера 16x16
disp(result_matr(1:16,1:16));