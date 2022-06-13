function [data_c3d] = get_c3d()

test = c3dserver
methods(test);
invoke(test);
methodsview(test)
openc3d(test)

end