function [data_excel_norm, data_ave_norm, data_std_norm, data_std_up_norm, data_std_lo_norm] = fn_data_norm(movement, type)

data_excel_norm = importdata('Normal Data.xlsx');
count = (size(data_excel_norm.data,1))/50;
data_ave_norm = zeros(1,count);
data_std_norm = zeros(1,count);
data_std_up_norm = zeros(1,count);
data_std_up_norm = zeros(1,count);

count_data = count * movement;

for i = (count_data-count+1) : count_data
%     A = [data_excel.data(i,type + 33)];
%     A = [data_excel.data(i,type + (3*0)) data_excel.data(i,type + (3*1)) ...
%                     data_excel.data(i,type + (3*2)) data_excel.data(i,type + (3*3)) ... 
%                     data_excel.data(i,type + (3*4))];
%     data_x(i) = (data_raw.data(i,1)+data_raw.data(i,4)+data_raw.data(i,7)+...
%                     data_raw.data(i,10)+data_raw.data(i,13))/5;
%     data_ave_norm(i - ((movement-1)*count)) = mean(A);
%     data_std_norm(i - ((movement-1)*count)) = std(A);
    data_ave_norm(i - ((movement-1)*count)) = data_excel_norm.data(i,type + 33);
    data_std_norm(i - ((movement-1)*count)) = data_excel_norm.data(i,type + 36);
end

data_std_up_norm = data_ave_norm + data_std_norm;
data_std_lo_norm = data_ave_norm - data_std_norm;

end