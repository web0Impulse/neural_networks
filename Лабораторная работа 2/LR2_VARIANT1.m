t = 0:0.01:20; % определяем число значений по оси абсцисс
a = 3; b = 5; % параметры функции принадлежности M_A
a1 = 0; b1 = 3; c1 = 5; % параметры функции принадлежности M_B
a2 = 0; b2 = 5; % параметры функции принадлежности M_C
j = 1;
% расчет графиков A, C, B
for i = 0:0.01:20
    if (i <= a)
        M_A(j) = 0;
    elseif (i > a) & (i <= b)
        M_A(j) = (i - a)/(b - a);
    else
        M_A(j) = 1;
    end

    if i <= a1
        M_B(j) = 0;
    elseif (i > a1) & (i <= b1)
        M_B(j) = (i - a1)/(b1 - a1);
    elseif (i > b1) & (i <= c1)
        M_B(j) = (c1 - i)/(c1 - b1);
    else M_B(j) = 0;
    end

    if i <= a2
        M_C(j) = 1;
    elseif (i > a2) & (i <= b2)
        M_C(j) = (b2 - i)/(b2 - a2);
    else M_C(j) = 0;
    end

    j = j + 1
end
% Вывод графиков функций принадлежности A, C, B
subplot(2, 3, 1)
plot(t, M_A, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A(x)');

subplot(2, 3, 2)
plot(t, M_B, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B(x)');

subplot(2, 3, 3)
plot(t, M_C, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_C(x)');

% D = A + B * C по максиминному методу
j = 1;
for i = 0:0.01:20
    % M_B_C = B * C
    M_B_C(j) = min(M_B(j), M_C(j));
    % D
    M_D(j) = max(M_A(j), M_B_C(j));
    j = j + 1
end
% Вывод графиков функций принадлежности B*C, D = A+B*C
subplot(2, 3, 4)
plot(t, M_B_C, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B_C(x)');

subplot(2, 3, 5)
plot(t, M_D, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_D(x)');

% НМ D лежит в диапазоне [0, бесконечность/(или 20 если учесть, что универсум ограничен 20)]
% Ядро НМ D лежит в диапазоне [5, бесконечность/(или 20 если учесть, что универсум ограничен 20)]
% Анализ максиминным способом точки X = 3
point = 3
j = round((point - t(1))/0.01); % найти точку в которой X = 3
m_A = M_A(j); % степень принадлежности НМ A в точке X = 3 
m_B = M_B(j); % степень принадлежности НМ B в точке X = 3
m_C = M_C(j); % степень принадлежности НМ C в точке X = 3
m_B_C = min(m_B, m_C); % B * C по максиминному способу
m_D = max(m_A, m_B_C); % D = A + BC по максиминному способу
disp(['Степень принадлежности значения 3 = ', num2str(M_D(j))]);