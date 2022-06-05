clc
clear all
% close all

%%% select data for plotting
movement_number = 1;
% movement_type = 2;
patient_number = 4;

%%% use function for data calculation
name = fn_data_name(movement_number); %%% movement number

[data_excel1, data_ave1, data_std1, data_std_up1, data_std_lo1] = ...
    fn_data_raw(movement_number,1); %%% movement number, movement type

[data_excel2, data_ave2, data_std2, data_std_up2, data_std_lo2] = ...
    fn_data_raw(movement_number,2); %%% movement number, movement type

[data_excel3, data_ave3, data_std3, data_std_up3, data_std_lo3] = ...
    fn_data_raw(movement_number,3); %%% movement number, movement type

%%% plot data

figure('Name','Average Data','NumberTitle','off');

subplot(2,2,1);
x = 1:1:101;
% plot(data_ave,'b--')
hold on
plot(data_std_up1,'k')
hold on
plot(data_std_lo1,'k')
patch([x fliplr(x)],[data_std_lo1 fliplr(data_std_up1)],'r')
% hold on
plot(data_excel1.data((100*(movement_number-1))+movement_number: ...
    (movement_number*101),(patient_number*3)-(3-1)), ...
    'g-.','LineWidth',3) %%% patient number
hold off
title(name + '   (X-axis)')
xlim([1 101])
ylim([-30 30])
legend('Upper SD','Lower SD','Fill','Raw Data')

subplot(2,2,2);
x = 1:1:101;
% plot(data_ave,'b--')
hold on
plot(data_std_up2,'k')
hold on
plot(data_std_lo2,'k')
patch([x fliplr(x)],[data_std_lo2 fliplr(data_std_up2)],'r')
% hold on
plot(data_excel2.data((100*(movement_number-1))+movement_number: ...
    (movement_number*101),(patient_number*3)-(3-2)), ...
    'g-.','LineWidth',3) %%% patient number
hold off
title(name + '   (Y-axis)')
xlim([1 101])
ylim([-30 30])
legend('Upper SD','Lower SD','Fill','Raw Data')

subplot(2,2,3);
x = 1:1:101;
% plot(data_ave,'b--')
hold on
plot(data_std_up3,'k')
hold on
plot(data_std_lo3,'k')
patch([x fliplr(x)],[data_std_lo3 fliplr(data_std_up3)],'r')
% hold on
plot(data_excel3.data((100*(movement_number-1))+movement_number: ...
    (movement_number*101),(patient_number*3)-(3-3)), ...
    'g-.','LineWidth',3) %%% patient number
hold off
title(name + '   (Z-axis)')
xlim([1 101])
ylim([-30 30])
legend('Upper SD','Lower SD','Fill','Raw Data')