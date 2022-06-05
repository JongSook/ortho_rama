%% get c3d file
tic

clc
clear all
close all

data_c3d = c3dserver;
methods(data_c3d);
invoke(data_c3d);
methodsview(data_c3d)
openc3d(data_c3d)

open_time = toc;

%% get data
tic

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

% right = zeros(count,1); %% r.shoulder-c7-t.head
% left = zeros(count,1); %% l.shoulder-c7-t.head
% flexion = zeros(count,1); %% sternum-c7-t.head	%% front
% extension = zeros(count,1); %% t2-c7-t.head	%% back
% flexion1 = zeros(count,1); %% sternum-c7-occiput	%% front
% extension1 = zeros(count,1); %% t2-c7-occiput	%% back

right_left = zeros(count,1); %% c7-r.head
flexion_extension = zeros(count,1); %% c7-r.head
rotation = zeros(count,1); %% t.head-f.head

% myVideo = VideoWriter('myMovementVideoNeck'); %open video file
% myVideo.FrameRate = 10;  %can adjust this, 5 - 10 works well for me
% open(myVideo)

for i = 1:count
    data_xyz = [data_x(i,1), data_y(i,1), data_z(i,1); ...
            data_x(i,2), data_y(i,2), data_z(i,2); ...
            data_x(i,3), data_y(i,3), data_z(i,3); ...
            data_x(i,4), data_y(i,4), data_z(i,4); ...
            data_x(i,5), data_y(i,5), data_z(i,5); ...
            data_x(i,6), data_y(i,6), data_z(i,6); ...
            data_x(i,7), data_y(i,7), data_z(i,7); ...
            data_x(i,8), data_y(i,8), data_z(i,8); ...
            data_x(i,9), data_y(i,9), data_z(i,9); ...
            data_x(i,10), data_y(i,10), data_z(i,10)
            ];
        
    rl_P1 = [data_x(i,3), data_y(i,3), data_z(i,3)];
    rl_P2 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    
    fe_P1 = [data_x(i,4), data_y(i,4), data_z(i,4)];
    fe_P2 = [data_x(i,5), data_y(i,5), data_z(i,5)];
    
    rt_P1 = [data_x(i,3), data_y(i,3), data_z(i,3)];
    rt_P2 = [data_x(i,2), data_y(i,2), data_z(i,2)];
    
    right_left(i) = ra_angle_plane3d(rl_P1, rl_P2, 3);
    flexion_extension(i) = ra_angle_plane3d(fe_P1, fe_P2, 1);
    rotation(i) = ra_angle_plane3d(rt_P1, rt_P2, 2);

%     right(i) = ra_angle_degree3p(right_P2, right_P1, right_P0);
%     left(i) = ra_angle_degree3p(left_P2, left_P1, left_P0);
%     flexion(i) = ra_angle_degree3p(flexion_P2, flexion_P1, flexion_P0);
%     extension(i) = ra_angle_degree3p(extension_P2, extension_P1, extension_P0);
%     flexion1(i) = ra_angle_degree3p(flexion_P21, flexion_P11, flexion_P01);
%     extension1(i) = ra_angle_degree3p(extension_P21, extension_P11, extension_P01);  
%     
%     p = plot3(data_xyz(:,1),data_xyz(:,2),data_xyz(:,3),'-o','Color','r',...
%         'MarkerSize',10,'MarkerFaceColor','#D9FFFF');
%     axis([-600  0 -100  500  700  1300])
% 
%     a = cellstr( num2str( [1:10]'));
%     dx = 0.1; dy = 0.1; dz = 0.1;
%     text(data_xyz(:,1)+dx, data_xyz(:,2)+dy, data_xyz(:,3)+dz, a);
%     
%     hold off;
%     pause(0.0001); %Pause and grab frame
%     frame = getframe(gcf); %get frame
%     writeVideo(myVideo, frame);
end

% close(myVideo)
plot_time = toc;

%% save output data
% filename = 'saveData2.xlsx';
% writematrix(right,filename,'Sheet','Angle')
% writematrix(right,filename,'Sheet','right','Range','A1')
% writematrix(left,filena me,'Sheet','right','Range','B1')
filename = 'neck_test__ love you rak ter na ka _left.xlsx';
% writematrix(right,filename,'Sheet','right(r.shoulder-c7-t.head)')
% writematrix(left,filename,'Sheet','left(l.shoulder-c7-t.head)')
% writematrix(flexion,filename,'Sheet','flexion(sternum-c7-t.head)')
% writematrix(extension,filename,'Sheet','extension(t2-c7-t.head)')
% writematrix(flexion1,filename,'Sheet','flexion(sternum-c7-occiput)')
% writematrix(extension1,filename,'Sheet','extension(t2-c7-occiput)')
writematrix(right_left,filename,'Sheet','right_left')
writematrix(flexion_extension,filename,'Sheet','flexion_extension')
writematrix(rotation,filename,'Sheet','rotation')