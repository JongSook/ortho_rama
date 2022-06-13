tic

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
%     n1 = (P2 - P0) / norm(P2 - P0);  % Normalized vectors
%     n2 = (P1 - P0) / norm(P1 - P0);
%     angle1 = acos(dot(n1, n2));                        % Instable at (anti-)parallel n1 and n2
%     angle2 = asin(nor m(cropss(n1, n2));                % Instable at perpendiculare n1 and n2
%     angle3 = atan2(norm(cross(n1, n2)), dot(n1, n2));  % Stable
%     angle3 = atan2(norm(det([n2; n1])), dot(n1, n2));
    A0 = [data_x(i,6), data_y(i,6), data_z(i,6)];
    A1 = [data_x(i,7), data_y(i,7), data_z(i,7)];
    A2 = [data_x(i,5), data_y(i,5), data_z(i,5)];

%     angle_move = num2str(vecangle360(P2,P1,P0));
    angle_right = num2str(ra_angle_degree(P2,P1,P0));
    angle_left = num2str(ra_angle_degree(A2,A1,A0));
%     text(1000,1000,1000, angle_move,'HorizontalAlignment','left','FontSize',22)
    
    p = plot3(data_xyz(:,1),data_xyz(:,2),data_xyz(:,3),'-o','Color','r',...
        'MarkerSize',10,'MarkerFaceColor','#D9FFFF');
    axis([-1500  1500 -1500  1500 -1500  1500])
    text(1000, -500, 1000, angle_left, ...
        'HorizontalAlignment', 'center', 'FontSize', 12)
    text(-1000, 500, 1000, angle_right, ...
        'HorizontalAlignment', 'center', 'FontSize', 18)
    
%     v_1 = [data_x(i,2), data_y(i,2), data_z(i,2)] - [data_x(i,3), data_y(i,3), data_z(i,3)];
%     v_2 = [data_x(i,4), data_y(i,4), data_z(i,4)] - [data_x(i,3), data_y(i,3), data_z(i,3)];
%     Theta = num2str(mod(atan2(det([v_1, v_2])), dot(v_1, v_2)), 2*pi );
    
    hold off;
    pause(0.01);
%     delete(p)
end

plot_time = toc;