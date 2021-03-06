function ang_deg = ra_angleangle_degree3p(point1, point2, point_innitial)

    AB = point1 - point_innitial;
    CD = point2 - point_innitial;
    ABCDdot = AB(1)*CD(1) + AB(2)*CD(2) + AB(3)*CD(3);
    ABabs = abs(sqrt(AB(1)*AB(1) + AB(2)*AB(2) + AB(3)*AB(3)));
    CDabs = abs(sqrt(CD(1)*CD(1) + CD(2)*CD(2) + CD(3)*CD(3)));
    ABCDfnv = ABCDdot / (ABabs * CDabs);
    ang_deg = acosd(ABCDfnv);
    
end

