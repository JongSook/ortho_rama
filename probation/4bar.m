for th=0:0.1:8*pi;
    a=5; c=6;
    d=7; b=8;
    AC=sqrt(a^2+d^2-2*a*d*cos(th));
    th1=acos((d^2+(AC^2)-a^2)/(2*d*AC));
    th2=acos(((AC^2)+b^2-c^2)/(2*AC*b));
    th3=(th2-th1);
    plot([0 a*cos(th)], [0 a*sin(th)],'ro-');hold on;
    plot([a*cos(th) a*cos(th)+b*cos(th3)], [a*sin(th) a*sin(th)+b*sin(th3)], 'ro-'); hold on;
    plot([0 d], [0 0], 'ro-'); hold on;
    plot([d a*cos(th)+b*cos(th3)], [0 a*sin(th)+b*sin(th3)], 'ro-');hold off;
    axis([-10 20 -10 10]);
    pause(0.1);
 
end
 
v_1 = [data_x(i,4), data_y(i,4), data_z(i,4)] - [data_x(i,3), data_y(i,3), data_z(i,3)];
v_2 = [data_x(i,2), data_y(i,2), data_z(i,2)] - [data_x(i,3), data_y(i,3), data_z(i,3)];
Theta = atan2(norm(cross(v_1, v_2)), dot(v_1, v_2));

a = atan2(norm(cross(P1,P2)),dot(P1,P2));