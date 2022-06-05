function [data_excel, data_ave, data_std, data_std_up, data_std_lo] = fn_data_raw(movement, type)

data_excel = importdata('Normal Data.xlsx');
count = (size(data_excel.data,1))/50;
data_ave = zeros(1,count);
data_std = zeros(1,count);

count_data = count * movement;

for i = (count_data-count+1) : count_data
    A = [data_excel.data(i,type + (3*0)) data_excel.data(i,type + (3*1)) ...
                    data_excel.data(i,type + (3*2)) data_excel.data(i,type + (3*3)) ... 
                    data_excel.data(i,type + (3*4))];
%     data_x(i) = (data_raw.data(i,1)+data_raw.data(i,4)+data_raw.data(i,7)+...
%                     data_raw.data(i,10)+data_raw.data(i,13))/5;
    data_ave(i - ((movement-1)*count)) = mean(A);
    data_std(i - ((movement-1)*count)) = std(A);
end

% data_std_up = data_ave+data_std;
data_std_up = data_ave + data_std;
data_std_lo = data_ave - data_std;

end