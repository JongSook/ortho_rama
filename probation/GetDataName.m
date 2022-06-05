tic

data_raw = importdata('Normal Data.xlsx');
data_all_name = string(data_raw.textdata(:,1));
count = (size(data_all_name,1)-2)/101;
data_name = string(zeros(count,1));


for i = 1:count
%    data_name = zeros(50,1);
   data_name(i) = data_all_name(3+(101*(i-1)),1);
end

toc