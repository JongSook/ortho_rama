function ang_deg = ra_angle_plane3d(point1, point2, plane)

    if plane == 1
        AB = point2 - point1;
        CD = [1 0 0];
    elseif plane == 2
        AB = point2 - point1;
        CD = [0 1 0];
    elseif plane == 3
        AB = point2 - point1;
        CD = [0 0 1];
    else
        AB = point2 - point1;
        CD = point1 - point2;
    end
    
    if  plane == 1 || plane == 2  
        ABCDdot = AB(1)*CD(1) + AB(2)*CD(2) + AB(3)*CD(3);
        ABabs = abs(sqrt(AB(1)*AB(1) + AB(2)*AB(2) + AB(3)*AB(3)));
        CDabs = abs(sqrt(CD(1)*CD(1) + CD(2)*CD(2) + CD(3)*CD(3)));
        ABCDfnv = ABCDdot / (ABabs * CDabs);
        ang_deg = 90 - acosd(ABCDfnv);
	elseif plane == 3 
        ABCDdot = AB(1)*CD(1) + AB(2)*CD(2) + AB(3)*CD(3);
        ABabs = abs(sqrt(AB(1)*AB(1) + AB(2)*AB(2) + AB(3)*AB(3)));
        CDabs = abs(sqrt(CD(1)*CD(1) + CD(2)*CD(2) + CD(3)*CD(3)));
        ABCDfnv = ABCDdot / (ABabs * CDabs);
        ang_deg = 180 - acosd(ABCDfnv);
%         ang_deg = acosd(ABCDfnv);
    else
        ABCDdot = AB(1)*CD(1) + AB(2)*CD(2) + AB(3)*CD(3);
        ABabs = abs(sqrt(AB(1)*AB(1) + AB(2)*AB(2) + AB(3)*AB(3)));
        CDabs = abs(sqrt(CD(1)*CD(1) + CD(2)*CD(2) + CD(3)*CD(3)));
        ABCDfnv = ABCDdot / (ABabs * CDabs);
        ang_deg = acosd(ABCDfnv);
    end
    
end