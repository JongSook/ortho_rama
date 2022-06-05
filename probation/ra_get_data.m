clc
clear all
close all

data_c3d = c3dserver
methods(data_c3d);
invoke(data_c3d);
methodsview(data_c3d)
openc3d(data_c3d)

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

% plot3(data_x,data_y,data_z)
% legend('R.Off', 'R.Sh', 'R.El', 'R.Wir', 'L.Sh', 'L.El', 'L.wir')

% for i = 1:count
%     data_xyz = [data_x(i,4), data_y(i,4), data_z(i,4); ...
%         data_x(i,3), data_y(i,3), data_z(i,3); ...
%         data_x(i,2), data_y(i,2), data_z(i,2); ...
%         data_x(i,1), data_y(i,1), data_z(i,1); ...
%         data_x(i,5), data_y(i,5), data_z(i,5); ...
%         data_x(i,6), data_y(i,6), data_z(i,6); ...
%         data_x(i,7), data_y(i,7), data_z(i,7)];
%     p = plot3(data_xyz(:,1),data_xyz(:,2),data_xyz(:,3),'-o','Color','r',...
%         'MarkerSize',10,'MarkerFaceColor','#D9FFFF')
%     axis([-1500  1500 -1500  1500 -1500  1500])
%     
% %     v_1 = [data_x(i,2), data_y(i,2), data_z(i,2)] - [data_x(i,3), data_y(i,3), data_z(i,3)];
% %     v_2 = [data_x(i,4), data_y(i,4), data_z(i,4)] - [data_x(i,3), data_y(i,3), data_z(i,3)];
% %     Theta = num2str(mod(atan2(det([v_1, v_2])), dot(v_1, v_2)), 2*pi );
% 
%     P0 = [data_x(i,3), data_y(i,3), data_z(i,3)];
%     P1 = [data_x(i,2), data_y(i,2), data_z(i,2)];
%     P2 = [data_x(i,4), data_y(i,4), data_z(i,4)];
% %     n1 = (P2 - P0) / norm(P2 - P0);  % Normalized vectors
% %     n2 = (P1 - P0) / norm(P1 - P0);
% %     angle1 = acos(dot(n1, n2));                        % Instable at (anti-)parallel n1 and n2
% %     angle2 = asin(nor m(cropss(n1, n2));                % Instable at perpendiculare n1 and n2
% %     angle3 = atan2(norm(cross(n1, n2)), dot(n1, n2));  % Stable
% %     angle3 = atan2(norm(det([n2; n1])), dot(n1, n2));
% 
% %     angle_move = num2str(vecangle360(P2,P1,P0));
%     angle_move = num2str(vecangle360(P2,P1,P0));
%     text(1000,1000,1000, angle_move,'HorizontalAlignment','left','FontSize',22)
%     
%     hold off;
%     pause(0.01);
% %     delete(p)
% end