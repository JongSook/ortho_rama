tic

clc
clear all
close all

% data_raw = readtable('Normal Data.xlsx');
% average
% standard derivertive
% plot

data_raw = importdata('Normal Data.xlsx');
count_all = (size(data_raw.data,1))/50;
data_ave = zeros(1,count_all);
data_std = zeros(1,count_all);

for i = 1 : count_all
    A = [data_raw.data(i,3) data_raw.data(i,6) ...
                    data_raw.data(i,9) data_raw.data(i,12) ... 
                    data_raw.data(i,15)];
%     data_x(i) = (data_raw.data(i,1)+data_raw.data(i,4)+data_raw.data(i,7)+...
%                     data_raw.data(i,10)+data_raw.data(i,13))/5;
    data_ave(i) = mean(A);
    data_std(i) = std(A);
end

data_std_up = data_ave+data_std;
data_std_lo = data_ave-data_std;

x = 1:1:101;
% plot(data_ave,'b--')
% hold on
plot(data_std_up,'k')
hold on
plot(data_std_lo,'k')
patch([x fliplr(x)],[data_std_lo fliplr(data_std_up)],'r')
% hold on
% plot(data_raw.data(1:101,1),'g-.','LineWidth',3)
hold off
xlim([1 101])
ylim([-20 20])
% legend('Upper SD','Lower SD','fill','ave')
legend('Upper SD','Lower SD','fill')

% x=0:0.1:10;
% y1=exp(-x/2);
% y2=exp(-x/3);
% figure
% hold all
% plot(x,y1)
% plot(x,y2)
% patch([x fliplr(x)], [y1 fliplr(y2)], 'g')
% hold off

% plot(data_raw.data(1:101,13))
% title(data_name(1))
% xlim([1 101])
% ylim([-15 15])

toc