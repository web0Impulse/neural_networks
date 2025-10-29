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

% Расчет A + B, A + C, C + B, A + C + B
j = 1;
for i = 0:0.01:20
    % M_AB = A + B
    M_AB(j) = max(M_A(j), M_B(j));
    % M_AC = A + C
    M_AC(j) = max(M_A(j), M_C(j));
    % M_BC = B + C
    M_BC(j) = max(M_B(j), M_C(j));
    % M_ABC = A + B + C
    M_ABC(j) = max(M_AB(j), M_C(j));
    j = j + 1;
end
% Вывод графиков функций принадлежности A + B, A + C, C + B, A + C + B
subplot(2, 4, 5)
plot(t, M_AB, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A_+_B(x)');

subplot(2, 4, 6)
plot(t, M_AC, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A_+_C(x)');

subplot(2, 4, 7)
plot(t, M_BC, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_B_+_C(x)');

subplot(2, 4, 8)
plot(t, M_ABC, 'LineWidth', 2);
grid on;
xlabel('X');
ylabel('M_A_+_B_+_C(x)');