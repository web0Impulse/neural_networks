start_interval = 63;
end_interval = 82;
dif = end_interval - start_interval;
result = dif * rand(4, 1) + start_interval;
disp(result);