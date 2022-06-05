%% get c3d file
clc
clear all
close all

data_c3d = c3dserver;
methods(data_c3d);
invoke(data_c3d);
methodsview(data_c3d)
openc3d(data_c3d)

tic

%% get data

count = data_c3d.GetVideoFrame(1);
number_3dpoint = data_c3d.GetNumber3DPoints;
% number_point = 3;
% data_xyz = zeros(count,3);
data_x = zeros(count,number_3dpoint);
data_y = zeros(count,number_3dpoint);
data_z = zeros(count,number_3dpoint);

for i = 1:count
    for j = 0:number_3dpoint-1
%    data_name = zeros(50,1);
%    data_xyz(i,1) = data_c3d.GetPointData(0, 0, i, '1');
%    data_xyz(i,2) = data_c3d.GetPointData(0, 1, i, '1');
%    data_xyz(i,3) = data_c3d.GetPointData(0, 2, i, '1');
        data_x(i,j+1) = data_c3d.GetPointData(j, 0, i, '1');
        data_y(i,j+1) = data_c3d.GetPointData(j, 1, i, '1');
        data_z(i,j+1) = data_c3d.GetPointData(j, 2, i, '1');
    end
end

data_time = toc;

%% plot c3d and get angle
tic

right = zeros(count,1);
left = zeros(count,1);

myVideo = VideoWriter('myMovementVideoTest'); %open video file
myVideo.FrameRate = 10;  %can adjust this, 5 - 10 works well for me
open(myVideo)

for i = 1:count
    data_xyz = [data_x(i,4), data_y(i,4), data_z(i,4); ...
        data_x(i,3), data_y(i,3), data_z(i,3); ...
        data_x(i,2), data_y(i,2), data_z(i,2); ...
        data_x(i,1), data_y(i,1), data_z(i,1); ...
        data_x(i,5), data_y(i,5), data_z(i,5); ...
        data_x(i,6), data_y(i,6), data_z(i,6); ...
        data_x(i,7), data_y(i,7), data_z(i,7)];
    
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
%     angle_right = num2str(angle_degree(P2,P1,P0));
%     angle_left = num2str(angle_degree(A2,A1,A0));
%     text(1000,1000,1000, angle_move,'HorizontalAlignment','left','FontSize',22)
    
    p = plot3(data_xyz(:,1),data_xyz(:,2),data_xyz(:,3),'-o','Color','r',...
        'MarkerSize',10,'MarkerFaceColor','#D9FFFF');
    axis([-1500  1500 -1500  1500 -1500  1500])
    text(1000, 500, 800, angle_left, ...
        'HorizontalAlignment', 'center', 'FontSize', 18)
    text(1000, 500, 1200, angle_right, ...
        'HorizontalAlignment', 'center', 'FontSize', 12)
    view(45, 45)
    
    hold off;
    pause(0.0001); %Pause and grab frame
    frame = getframe(gcf); %get frame
    writeVideo(myVideo, frame);
%     delete(p)
end

close(myVideo)
plot_time = toc;

%% pop-up output data
right_min = num2str(min(right));
right_max = num2str(max(right));
left_min = num2str(min(left));
left_max = num2str(max(left));

str_minr = append('Minimum Right Degree : ', right_min);
str_maxr = append('Maximun Right Degree : ', right_max);
str_minl = append('Minimum Left Degree : ', left_min);
str_maxl = append('Maximun Left Degree : ', left_max);
% f = msgbox('Invalid Value', 'Error','error');
% f = msgbox('Operation Completed','Success');
% f = msgbox({'Operation';'Completed'});
% data_popup = msgbox({'Maximun Degree : ' + right_max; 'Minimum Degree :' + right_min}, ...
%     'Angle in Degree');
data_popup = msgbox({str_maxr; str_minr; str_maxl; str_minl}, 'Angle in Degree');

%% save output data
% saveas(gcf,'Left Pelvic Tlit.pdf'); %% Get current figure handle get(0,'CurrentFigure')
% savefig('Left Pelvic Tlit.fig')
% writematrix(x,'M_tab.txt')
% writematrix(x,'M.xls')
filename = 'saveData.xlsx';
writematrix(right,filename,'Sheet','Angle')