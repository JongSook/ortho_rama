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
        data_x(i,j+1) = data_c3d.GetPointData(j, 0, i, '1');
        data_y(i,j+1) = data_c3d.GetPointData(j, 1, i, '1');
        data_z(i,j+1) = data_c3d.GetPointData(j, 2, i, '1');
    end
end

%% plot c3d and get angle
right = zeros(count,1);
left = zeros(count,1);

for i = 1:count
    P0 = [data_x(i,3), data_y(i,3), data_z(i,3)];
    P1 = [data_x(i,4), data_y(i,4), data_z(i,4)];
    P2 = [data_x(i,2), data_y(i,2), data_z(i,2)];

    A0 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    A1 = [data_x(i,7), data_y(i,7), data_z(i,7)];
    A2 = [data_x(i,5), data_y(i,5), data_z(i,5)];

    right(i) = ra_angle_degree3p(P2,P1,P0);
    left(i) = ra_angle_degree3p(A2,A1,A0);
    angle_right = num2str(right(i));
    angle_left = num2str(left(i));
end

%% pop-up output data
right_min = num2str(min(right));
right_max = num2str(max(right));
left_min = num2str(min(left));
left_max = num2str(max(left));

str_minr = append('Minimum Right Degree : ', right_min);
str_maxr = append('Maximun Right Degree : ', right_max);
str_minl = append('Minimum Left Degree : ', left_min);
str_maxl = append('Maximun Left Degree : ', left_max);

data_popup = msgbox({str_maxr; str_minr; str_maxl; str_minl}, 'Angle in Degree');

%% save output data
% saveas(gcf,'Left Pelvic Tlit.pdf'); %% Get current figure handle get(0,'CurrentFigure')
% savefig('Left Pelvic Tlit.fig')
% writematrix(x,'M_tab.txt')
% writematrix(x,'M.xls')
filename = 'saveData.xlsx';
writematrix(right,filename,'Sheet','Angle')