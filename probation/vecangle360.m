function a = vecangle360(v1,v2,n)
%     x = cross(v1,v2);
%     c = sign(dot(x,n)) * norm(x);
%     a = atan2d(c,dot(v1,v2));
    
%     t1 = [1 4 3];
%     g1 = [2 4 3];
%     % normal associated with g1
%     n = [-1 0 0]; %<-- does this have to be normalized??
%     % get vector from g1 to t1:
%     v1 = g1-t1;
%     angle = atan2(norm(cross(v1,n)),dot(v1,n)).*(180/pi)
%     ang = v1-v2;
%     a = atan2(norm(cross(ang,n)),dot(ang,n)).*(180/pi)
    
%     v = [1 4 3];
%     n = [-1 0 0];
%     angle1 = atan2(norm(cross(v,n)), dot(v,n)).*(180/pi)
%     n = [-1000 0 0];
%     angle2 = atan2(norm(cross(v,n)), dot(v,n)).*(180/pi)
%     ang = v1-v2;
%     n1 = [-1000 0 0];
%     a = atan2(norm(cross(ang,n1)), dot(ang,n1)).*(180/pi);

%     P01 = n - v1;
%     P02 = v2 - n;
%     pd = (P01(1)*P02(1))+(P01(2)*P02(2))+(P01(3)*P02(3));
%     pc = abs((P01(1)^2)+(P01(2)^2)+(P01(3)^2))*...
%         abs((P02(1)^2)+(P02(2)^2)+(P02(3)^2));
%     pr = pd/pc;
%     a=acosd(pr);

    AB = v2 - n;
    CD = v1 - n;
    ABCDdot = AB(1)*CD(1) + AB(2)*CD(2) + AB(3)*CD(3);
    ABabs = abs(sqrt(AB(1)*AB(1) + AB(2)*AB(2) + AB(3)*AB(3)));
    CDabs = abs(sqrt(CD(1)*CD(1) + CD(2)*CD(2) + CD(3)*CD(3)));
    ABCDfnv = ABCDdot / (ABabs * CDabs);
    a = acosd(ABCDfnv);
end

