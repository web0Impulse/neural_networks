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
% D = A + B * C по максиминному методу
j = 1;
for i = 0:0.01:20
    % M_B_C = B * C
    M_B_C(j) = min(M_B(j), M_C(j));
    % D
    M_D(j) = max(M_A(j), M_B_C(j));
    j = j + 1
end

% Вывод графиков функций принадлежности A, C, B, D
subplot(2, 4, 1)
plot(t, M_A, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A(x)');

subplot(2, 4, 2)
plot(t, M_B, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B(x)');

subplot(2, 4, 3)
plot(t, M_C, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_C(x)');

subplot(2, 4, 4)
plot(t, M_D, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_D(x)');

% Расчет no A, no B, no C, no D
j = 1;
for i = 0:0.01:20
    % M_nA = no A
    M_nA(j) = 1 - M_A(j);
    % M_nB = no B
    M_nB(j) = 1 - M_B(j);
    % M_nC = no C
    M_nC(j) = 1 - M_C(j);
    % M_nD = no D
    M_nD(j) = 1 - M_D(j);
    j = j + 1;
end
% Вывод графиков функций принадлежности no A, no B, no C, no D
subplot(2, 4, 5)
plot(t, M_nA, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_nA(x)');

subplot(2, 4, 6)
plot(t, M_nB, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_nB(x)');

subplot(2, 4, 7)
plot(t, M_nC, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_nC(x)');

subplot(2, 4, 8)
plot(t, M_nD, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_nD(x)');