%% get c3d file
clc
clear
close all

data_c3d = c3dserver;
methods(data_c3d);
invoke(data_c3d);
% methodsview(data_c3d)
openc3d(data_c3d)

%% get data
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

%% plot c3d and get angle
elbow = zeros(count,1); %% c7-r.head
knee = zeros(count,1); %% c7-r.head

elbowr = zeros(count,1); %% c7-r.head
elbowl = zeros(count,1); %% c7-r.head

for i = 1:count       
%     data_xyz = [data_x(i,1), data_y(i,1), data_z(i,1); ...
%             data_x(i,2), data_y(i,2), data_z(i,2); ...
%             data_x(i,3), data_y(i,3), data_z(i,3); ...
%             data_x(i,4), data_y(i,4), data_z(i,4); ...
%             data_x(i,5), data_y(i,5), data_z(i,5); ...
%             data_x(i,6), data_y(i,6), data_z(i,6); ...
%             data_x(i,7), data_y(i,7), data_z(i,7); ...
%             data_x(i,8), data_y(i,8), data_z(i,8)
%             ];
        
%     elbow_P1 = [data_x(i,1), data_y(i,1), data_z(i,1)];
%     elbow_P2 = [data_x(i,3), data_y(i,3), data_z(i,3)];
%     elbow_P3 = [data_x(i,4), data_y(i,4), data_z(i,4)];
% %     elbow_P4 = [data_x(i,3), data_y(i,3), data_z(i,3)];
%     knee_P1 = [data_x(i,1), data_y(i,1), data_z(i,1)];
%     knee_P2 = [data_x(i,3), data_y(i,3), data_z(i,3)];
%     knee_P3 = [data_x(i,4), data_y(i,4), data_z(i,4)];
% %     knee_P4 = [data_x(i,2), data_y(i,2), data_z(i,2)];
%     
%     elbow(i) = ra_angle_degree3p(elbow_P1, elbow_P2, elbow_P3, elbow_P2);
%     knee(i) = ra_angle_degree3p(knee_P2, knee_P1, knee_P2, knee_P3);
    
%     elbow_P1 = [data_x(i,2), data_y(i,2), data_z(i,2)];
%     elbow_P2 = [data_x(i,1), data_y(i,1), data_z(i,1)];
%     elbow_P3 = [data_x(i,3), data_y(i,3), data_z(i,3)];
%     elbow_P4 = [data_x(i,4), data_y(i,4), data_z(i,4)];
%     knee_P1 = [data_x(i,7), data_y(i,7), data_z(i,7)];
%     knee_P2 = [data_x(i,8), data_y(i,8), data_z(i,8)];
%     knee_P3 = [data_x(i,6), data_y(i,6), data_z(i,6)];
%     knee_P4 = [data_x(i,5), data_y(i,5), data_z(i,5)];
%     
%     elbow(i) = ra_angle_degree3p(elbow_P1, elbow_P2, elbow_P3, elbow_P4);
%     knee(i) = ra_angle_degree3p(knee_P1, knee_P2, knee_P3, knee_P4);
    
    elbow_P1 = [data_x(i,2), data_y(i,2), data_z(i,2)];
    elbow_P2 = [data_x(i,3), data_y(i,3), data_z(i,3)];
    elbow_P3 = [data_x(i,4), data_y(i,4), data_z(i,4)];
    elbow_P4 = [data_x(i,3), data_y(i,3), data_z(i,3)];
    knee_P1 = [data_x(i,5), data_y(i,5), data_z(i,5)];
    knee_P2 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    knee_P3 = [data_x(i,7), data_y(i,7), data_z(i,7)];
    knee_P4 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    
    elbowr(i) = ra_angle_degree3p(elbow_P1, elbow_P2, elbow_P3, elbow_P4);
    elbowl(i) = ra_angle_degree3p(knee_P1, knee_P2, knee_P3, knee_P4);
end

% elbow_min = min(elbow);
% elbow_max = max(elbow);
% knee_min = min(knee);
% knee_max = max(knee);

elbowr_min = min(elbowr);
elbowr_max = max(elbowr);
elbowl_min = min(elbowl);
elbowl_max = max(elbowl);

%% read file name
filePattern = fullfile('./', '*.c3d');
files = dir(filePattern);

for i=1:length(files)
    filesname(i) = files(i);
%     filesname.name
    %stlread(filename); %you can try this out by uncommenting
end

%% save output data
filerun = filesname(3).name;
% filename = 'neck_test_Nong P 0 degree 19-20 min test05.xlsx';
filename =  convertStringsToChars(convertCharsToStrings(erase(filerun, ".c3d")) + '.xlsx');
sheetname = erase(filerun, ".c3d");
sheetname = erase(sheetname, "bending");

% writematrix('Elbow Raw', filename, 'Sheet', sheetname, 'Range', 'A1')
% writematrix('Knee Raw', filename, 'Sheet', sheetname, 'Range', 'B1')
% writematrix(elbow, filename, 'Sheet', sheetname, 'Range', 'A2')
% writematrix(knee, filename, 'Sheet', sheetname, 'Range', 'B2')

writematrix('Elb/R Raw', filename, 'Sheet', sheetname, 'Range', 'A1')
writematrix('Elb/L Raw', filename, 'Sheet', sheetname, 'Range', 'B1')
writematrix(elbowr, filename, 'Sheet', sheetname, 'Range', 'A2')
writematrix(elbowl, filename, 'Sheet', sheetname, 'Range', 'B2')

% writematrix('Max Elbow', filename, 'Sheet', sheetname, 'Range', 'E1')
% writematrix('Max Knee', filename, 'Sheet', sheetname, 'Range', 'F1')
% writematrix(elbow_max, filename, 'Sheet', sheetname, 'Range', 'E2')
% writematrix(knee_max, filename, 'Sheet', sheetname, 'Range', 'F2')

writematrix('Max Elb/R', filename, 'Sheet', sheetname, 'Range', 'E1')
writematrix('Max Elb/L', filename, 'Sheet', sheetname, 'Range', 'F1')
writematrix(elbowr_max, filename, 'Sheet', sheetname, 'Range', 'E2')
writematrix(elbowl_max, filename, 'Sheet', sheetname, 'Range', 'F2')

% writematrix('Min Elbow', filename, 'Sheet', sheetname, 'Range', 'E4')
% writematrix('Min Knee', filename, 'Sheet', sheetname, 'Range', 'F4')
% writematrix(elbow_min, filename, 'Sheet', sheetname, 'Range', 'E5')
% writematrix(knee_min, filename, 'Sheet', sheetname, 'Range', 'F5')

writematrix('Min Elb/R', filename, 'Sheet', sheetname, 'Range', 'E4')
writematrix('Min Elb/L', filename, 'Sheet', sheetname, 'Range', 'F4')
writematrix(elbowr_min, filename, 'Sheet', sheetname, 'Range', 'E5')
writematrix(elbowl_min, filename, 'Sheet', sheetname, 'Range', 'F5')