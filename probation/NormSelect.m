%% insert data
clc
clear all
close all


prompt_num = {'Enter Movement Number:', 'Enter Movement Type Number:', ...
    'Enter Patient Number:', 'Enter X-Axis:', 'Enter Y-Axis:'};
dlgtitle_num = 'Insert Required Number';
dims_num = [1 43];
definput_num = {'0', '0', '0', '0', '0'};
input_num_cell = inputdlg(prompt_num, dlgtitle_num, dims_num, definput_num);

prompt_str = {'Enter Figure Name:', 'Enter Label Name:'};
dlgtitle_str = 'Insert Required Name';
dims_str = [1 43];
definput_str = {'0', '0'};
input_str_cell = inputdlg(prompt_str, dlgtitle_str, dims_str, definput_str);

input_num = cellfun(@str2num,input_num_cell);
input_str = string(input_str_cell);

% movement_number = 11;
% movement_type = 2;
% patient_number = 4;       
% 
% xy = -10;
% yy = 50;
% yl = 'Pos - Ant';
% movement = 'Right Foot Progression';
% movement = 'Right Foot Dors/Plantarflexion';
% movement = 'Right Foot Rotation';
% movement = 'Right Knee Flex/Extension';
% movement = 'Right Hip Ab/Adduction';
% movement = 'Right Pelvic Obliquity';
% movement = 'Right Pelvic Tlit';
% movement = 'Right Knee Varus/Valgus';
% movement = 'Left Foot Progression';
% movement = 'Left Foot Dors/Plantarflexion';
% movement = 'Left Foot Rotation';
% movement = 'Left Knee Flex/Extension';
% movement = 'Left Hip Ab/Adduction';
% movement = 'Left Pelvic Obliquity';
% movement = 'Left Pelvic Tlit';
% movement = 'Left Knee Varus/Valgus';

% if movement_type == 1
%     xyz = '   (X-axis)';
% elseif movement_type == 2
%     xyz = '   (Y-axis)';
% elseif movement_type == 3
%     xyz = '   (Z-axis)';
% else
%     xyz = '';
% end

%% plot data
name = data_name(input_num(1)); %%% movement number

[data_excel, data_ave, data_std, data_std_up, data_std_lo] = ...
    data_raw(input_num(1), input_num(2)); %%% movement number, movement type

[data_excel_norm, data_ave_norm, data_std_norm, data_std_up_norm, data_std_lo_norm] = ...
    data_norm(input_num(1), input_num(2));

% name = data_name(movement_number) %%% movement number
% 
% [data_excel, data_ave, data_std, data_std_up, data_std_lo] = ...
%     data_raw(movement_number, movement_type) %%% movement number, movement type
% 
% [data_excel_norm, data_ave_norm, data_std_norm, data_std_up_norm, data_std_lo_norm] = ...
%     data_norm(movement_number, movement_type)

% str = '#0072BD';
% color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;

figure('Name','Average Normal Data 5N','NumberTitle','off');

x = 1:1:101;
zero_line = zeros(1,101);

% plot(data_ave,'b--')
hold on
plot(data_std_up_norm, 'k')
hold on
plot(data_std_lo_norm, 'k')
hold on
plot(data_std_up, 'k')
hold on
plot(data_std_lo, 'k')
l(1) = patch([x fliplr(x)],[data_std_lo_norm fliplr(data_std_up_norm)], [1.0000 0.8431 0.8431], ...
    'EdgeColor', [1.0000 0.8431 0.8431]);
% hold on
l(2) = patch([x fliplr(x)],[data_std_lo fliplr(data_std_up)], [0.8431 1.0000 0.8431], ...
    'EdgeColor', [0.8431 1.0000 0.8431]);
% hold on
% l(3) = plot(data_excel.data((100*(movement_number-1))+movement_number: ...
%     (movement_number*101),(patient_number*3)-(3-movement_type)), ...
%     'r-.','LineWidth',1.5) %%% patient number
hold on
ylabel(input_str(2))
yline(0);
xline(1, '-', {'RHS'}, 'LabelHorizontalAlignment', 'center', 'LabelVerticalAlignment', 'bottom');
xline(12, '-', {'LTO'}, 'LabelHorizontalAlignment', 'center', 'LabelVerticalAlignment', 'bottom');
xline(51, '-', {'LHS'}, 'LabelHorizontalAlignment', 'center', 'LabelVerticalAlignment', 'bottom');
xline(61, '-', {'RTO'}, 'LabelHorizontalAlignment', 'center', 'LabelVerticalAlignment', 'bottom');
xline(101, '-', {'RHS'}, 'LabelHorizontalAlignment', 'center', 'LabelVerticalAlignment', 'bottom');
hold off
title(input_str(1))
xlim([1 101])
ylim([input_num(4) input_num(5)])
legend(l, 'Device', 'Rama')

%% save data figure
saveas(gcf,input_str(1) + '.pdf'); %% Get current figure handle get(0,'CurrentFigure')
% saveas(gcf,input_str(1) + '.jpg');
% savefig(input_str(1))
% writematrix(x,'M_tab.txt')
% writematrix(x,'M.xls')