%% get c3d file
tic

clc
clear
close all

data_c3d = c3dserver;
methods(data_c3d);
invoke(data_c3d);
% methodsview(data_c3d)
openc3d(data_c3d)

% open_time = toc;
%% get data
% tic

count = data_c3d.GetVideoFrame(1);
number_3dpoint = data_c3d.GetNumber3DPoints;
data_x = zeros(count,number_3dpoint);
data_y = zeros(count,number_3dpoint);
data_z = zeros(count,number_3dpoint);

for i = 1:count
    for j = 0:number_3dpoint-1
%    data_name = zeros(50,1);
        data_x(i,j+1) = data_c3d.GetPointData(j, 0, i, '1');
        data_y(i,j+1) = data_c3d.GetPointData(j, 1, i, '1');
        data_z(i,j+1) = data_c3d.GetPointData(j, 2, i, '1');
    end
end

% data_time = toc;
%% plot c3d and get angle
% tic

right_left = zeros(count,1); %% c7-r.head
flexion_extension = zeros(count,1); %% c7-r.head
rotation = zeros(count,1); %% t.head-f.head

for i = 1:count       
%     data_xyz = [data_x(i,1), data_y(i,1), data_z(i,1); ...
%             data_x(i,2), data_y(i,2), data_z(i,2); ...
%             data_x(i,3), data_y(i,3), data_z(i,3); ...
%             data_x(i,4), data_y(i,4), data_z(i,4); ...
%             data_x(i,5), data_y(i,5), data_z(i,5); ...
%             data_x(i,6), data_y(i,6), data_z(i,6); ...
%             data_x(i,7), data_y(i,7), data_z(i,7); ...
%             data_x(i,8), data_y(i,8), data_z(i,8); ...
%             data_x(i,9), data_y(i,9), data_z(i,9); ...
%             data_x(i,10), data_y(i,10), data_z(i,10); ...
%             data_x(i,11), data_y(i,11), data_z(i,11); ...
%             data_x(i,12), data_y(i,12), data_z(i,12); ...
%             data_x(i,13), data_y(i,13), data_z(i,13); ...
%             data_x(i,14), data_y(i,14), data_z(i,14); ...
%             data_x(i,15), data_y(i,15), data_z(i,15); ...
%             data_x(i,16), data_y(i,16), data_z(i,16)
%             ];
        
    rl_P1 = [data_x(i,1), data_y(i,1), data_z(i,1)];
    rl_P2 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    fe_P1 = [data_x(i,1), data_y(i,1), data_z(i,1)];
    fe_P2 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    rt_P1 = [data_x(i,3), data_y(i,3), data_z(i,3)];
    rt_P2 = [data_x(i,2), data_y(i,2), data_z(i,2)];
    
    right_left(i) = ra_angle_plane3d(rl_P1, rl_P2, 3);
    flexion_extension(i) = ra_angle_plane3d(fe_P1, fe_P2, 1);
    rotation(i) = ra_angle_plane3d(rt_P1, rt_P2, 2);
end

rl_min = min(right_left);
rl_max = max(right_left);
fe_min = min(flexion_extension);
fe_max = max(flexion_extension);
rotation_min = min(rotation);
rotation_max = max(rotation);

% plot_time = toc;
%% read file name
% tic

filePattern = fullfile('./', '*.c3d');
files = dir(filePattern);

for i=1:length(files)
    filesname(i) = files(i);
%     filesname.name
    %stlread(filename); %you can try this out by uncommenting
end

% read_time = toc;
%% save output data
% tic

filerun = filesname(4).name;
% filename = 'neck_test_Nong P 0 degree 19-20 min test05.xlsx';
filename =  convertStringsToChars(convertCharsToStrings(erase(filerun, ".c3d")) + '.xlsx');
sheetname = erase(filerun, ".c3d");
sheetname = erase(sheetname, "bending");
writematrix('L/R Raw', filename, 'Sheet', sheetname, 'Range', 'A1')
writematrix('FL/EXT Raw', filename, 'Sheet', sheetname, 'Range', 'B1')
writematrix('ROT Raw', filename, 'Sheet', sheetname, 'Range', 'C1')
writematrix(right_left, filename, 'Sheet', sheetname, 'Range', 'A2')
writematrix(flexion_extension, filename, 'Sheet', sheetname, 'Range', 'B2')
writematrix(rotation, filename, 'Sheet', sheetname, 'Range', 'C2')

writematrix('Max L/R', filename, 'Sheet', sheetname, 'Range', 'E1')
writematrix('Max FL/EXT', filename, 'Sheet', sheetname, 'Range', 'F1')
writematrix('Max ROT', filename, 'Sheet', sheetname, 'Range', 'G1')
writematrix(rl_max, filename, 'Sheet', sheetname, 'Range', 'E2')
writematrix(fe_max, filename, 'Sheet', sheetname, 'Range', 'F2')
writematrix(rotation_max, filename, 'Sheet', sheetname, 'Range', 'G2')

writematrix('Min L/R', filename, 'Sheet', sheetname, 'Range', 'E4')
writematrix('Min FL/EXT', filename, 'Sheet', sheetname, 'Range', 'F4')
writematrix('Min ROT', filename, 'Sheet', sheetname, 'Range', 'G4')
writematrix(rl_min, filename, 'Sheet', sheetname, 'Range', 'E5')
writematrix(fe_min, filename, 'Sheet', sheetname, 'Range', 'F5')
writematrix(rotation_min, filename, 'Sheet', sheetname, 'Range', 'G5')

% writetable(table(Time, Data), 'Result.xlsx', 'WriteVariableNames', true)
% xlswritefig(gcf, 'Result.xlsx', 'Sheet1', 'D2')
figure('position', [200 200 750 500])
subplot(221)
plot(right_left)
title('Left/Right')
xlabel('Motion Points (Samples)', 'FontSize', 8, 'FontWeight', 'bold')
ylabel('Angles in Degrees (°)', 'FontSize', 8, 'FontWeight', 'bold')
subplot(222)
plot(flexion_extension)
title('Flexion/Extension')
xlabel('Motion Points (Samples)', 'FontSize', 8, 'FontWeight', 'bold')
ylabel('Angles in Degrees (°)', 'FontSize', 8, 'FontWeight', 'bold')
subplot(223)
plot(rotation)
title('Rotation')
xlabel('Motion Points (Samples)', 'FontSize', 8, 'FontWeight', 'bold')
ylabel('Angles in Degrees (°)', 'FontSize', 8, 'FontWeight', 'bold')
subplot(224)
x = categorical({'L/R' 'FL/EXT' 'ROT'});
vals = [rl_min fe_min rotation_min; rl_max fe_max rotation_max];
b = bar(x, vals);
title('Maximun/Minimum')
ylabel('Angles in Degrees (°)', 'FontSize', 8, 'FontWeight', 'bold')
xtips1 = b(1).XEndPoints;
ytips1 = b(1).YEndPoints;
labels1 = string(b(1).YData);
text(xtips1, ytips1/2, labels1, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom', 'FontSize', 3)
xtips2 = b(2).XEndPoints;
ytips2 = b(2).YEndPoints;
labels2 = string(b(2).YData);
text(xtips2, ytips2/2, labels2, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom', 'FontSize', 3)
xlswritefig(gcf, filename, sheetname, 'E8')

operate_time = toc;