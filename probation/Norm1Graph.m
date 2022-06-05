clc
clear all
close all

%%% select data for plotting
movement_number = 1;
movement_type = 2;
patient_number = 4;

if movement_type == 1
    xyz = '   (X-axis)';
elseif movement_type == 2
    xyz = '   (Y-axis)';
elseif movement_type == 3
    xyz = '   (Z-axis)';
else
    xyz = '';
end

%%% use function for data calculation
name = fn_data_name(movement_number); %%% movement number

[data_excel, data_ave, data_std, data_std_up, data_std_lo] = ...
    fn_data_raw(movement_number,movement_type); %%% movement number, movement type

%%% plot data
x = 1:1:101;
% plot(data_ave,'b--')
hold on
plot(data_std_up,'k')
hold on
plot(data_std_lo,'k')
patch([x fliplr(x)],[data_std_lo fliplr(data_std_up)],'r')
% hold on
plot(data_excel.data((100*(movement_number-1))+movement_number: ...
    (movement_number*101),(patient_number*3)-(3-movement_type)), ...
    'g-.','LineWidth',3) %%% patient number
hold off
title(name + xyz)
xlim([1 101])
ylim([-30 30])
legend('Upper SD','Lower SD','Fill','Raw Data')