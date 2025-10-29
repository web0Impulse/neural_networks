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
subplot(3, 4, 1)
plot(t, M_A, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A(x)');

subplot(3, 4, 2)
plot(t, M_B, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B(x)');

subplot(3, 4, 3)
plot(t, M_C, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_C(x)');

% Расчет A - B, A - C, C - B, C - A, B - C, B - A
j = 1;
for i = 0:0.01:20
    % M_AmB = A - B = A * noB
    M_AmB(j) = min(M_A(j), 1 - M_B(j));
    % M_AmC = A - C = A * noC
    M_AmC(j) = min(M_A(j), 1 - M_C(j));
    % M_CmB = C - B = C * noB
    M_CmB(j) = min(M_C(j), 1 - M_B(j));
    % M_CmA = C - A = C * noA
    M_CmA(j) = min(M_C(j), 1 - M_A(j));
    % M_BmC = B - C = B * noC
    M_BmC(j) = min(M_B(j), 1 - M_C(j));
    % M_BmA = B - A = B * noA
    M_BmA(j) = min(M_B(j), 1 - M_A(j));
    j = j + 1;
end
% Вывод графиков функций принадлежности A - B, A - C, C - B, C - A, B - C, B - A
subplot(3, 4, 4)
plot(t, M_AmB, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A_-_B(x)');

subplot(3, 4, 5)
plot(t, M_AmC, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A_-_C(x)');

subplot(3, 4, 6)
plot(t, M_CmA, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_C_-_A(x)');

subplot(3, 4, 7)
plot(t, M_CmB, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_C_-_B(x)');

subplot(3, 4, 8)
plot(t, M_BmA, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B_-_A(x)');

subplot(3, 4, 9)
plot(t, M_BmC, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B_-_C(x)');