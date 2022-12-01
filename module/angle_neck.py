import c3d
import pandas as pd
import numpy as np
import numpy.linalg as LA
import math
# import xlsxwriter

# path_select = input('File name: ')
# path = 'D:/Document/Mahidol University/OrthoRama/Python/' + path_select + '.c3d'
path = 'D:\Document\Mahidol University\OrthoRama\Python\sample01\\Neck P khaew flexion1.c3d'
reader = c3d.Reader(open(path, 'rb'))

def angle_of_two_vectors(u1, u2, u3, v1, v2, v3):
    a = np.array([u1, u2, u3])  # ([1, 2])
    b = np.array([v1, v2, v3])  # [-5, 4]

    inner = np.inner(a, b)
    norms = LA.norm(a) * LA.norm(b)

    cos = inner / norms
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    deg = np.rad2deg(np.clip(rad, -2.0 * math.pi, 2.0 * math.pi))

    return deg

def angle_of_unit_vectors(u1, u2, u3, xyz):
    a = np.array([u1, u2, u3])

    if xyz == 'x':
        b = np.array([1, 0, 0])
    elif xyz == 'y':
        b = np.array([0, 1, 0])
    elif xyz == 'z':
        b = np.array([0, 0, 1])
    else:
        # pass
        print("Hello World")
        
    inner = np.inner(a, b)
    norms = LA.norm(a) * LA.norm(b)

    cos = inner / norms
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    deg = np.rad2deg(np.clip(rad, -2.0 * math.pi, 2.0 * math.pi))

    if xyz == 'x':
        deg = 90 - deg
    elif xyz == 'y':
        deg = 90 - deg
    elif xyz == 'z':
        deg = 180 - deg
    else:
        # pass
        print("Hello World")

    return deg

def angle_of_two_unit_vectors(u1, u2, u3, v1, v2, v3, xyz):
    a = np.array([u1 - v1, u2 - v2, u3 - v3])

    if xyz == 'x':
        b = np.array([1, 0, 0])
    elif xyz == 'y':
        b = np.array([0, 1, 0])
    elif xyz == 'z':
        b = np.array([0, 0, 1])
    else:
        # pass
        print("Hello World")

    inner = np.inner(a, b)
    norms = LA.norm(a) * LA.norm(b)

    cos = inner / norms
    rad = np.arccos(np.clip(cos, -1.0, 1.0))
    deg = np.rad2deg(np.clip(rad, -2.0 * math.pi, 2.0 * math.pi))

    if xyz == 'x':
        deg = 90 - deg
    elif xyz == 'y':
        deg = 90 - deg
    elif xyz == 'z':
        deg = 180 - deg
    else:
        # pass
        print("Hello World")

    return deg

df_labels = pd.DataFrame()
df_1 = pd.DataFrame()
df_2 = pd.DataFrame()
df_3 = pd.DataFrame()
df_4 = pd.DataFrame()
df_5 = pd.DataFrame()
df_6 = pd.DataFrame()
df_7 = pd.DataFrame()
df_8 = pd.DataFrame()
df_9 = pd.DataFrame()
df_10 = pd.DataFrame()

df_deg1 = pd.DataFrame()
df_deg2 = pd.DataFrame()
df_deg3 = pd.DataFrame()
df_deg4 = pd.DataFrame()
df_deg5 = pd.DataFrame()
df_deg6 = pd.DataFrame()
df_deg7 = pd.DataFrame()
df_deg8 = pd.DataFrame()
df_deg9 = pd.DataFrame()
df_deg10 = pd.DataFrame()

for i in range(10):
    # print('frame {}: point {}, analog {}'.format(i, reader.point_labels[i], reader.point_labels[1]))
    df_labels_loop = pd.DataFrame([reader.point_labels[i]], index = [i], columns = ['Point Labels'])
    df_labels = df_labels.append(df_labels_loop)

for i, points, analog in reader.read_frames():
    for f in range(10):
        # print('frame {}: point {}, analog {}'.format(points[f,0], points[f,1], points[f,2]))
        # print('frame {}: point {}, analog {}'.format(i, points.shape, analog.shape))
        # print('frame {}: point {}'.format(i, points.all))
        # print(reader.point_labels[f])
        df_labels_loop = pd.DataFrame([[points[f,0], points[f,1], points[f,2]]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
        if f == 0:
            df_1 = df_1.append(df_labels_loop)
            # test = angle_of_two_vectors(points[f,0], points[f,1], points[f,2], points[f+1,0], points[f+1,1], points[f+1,2])
            # unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            # unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            # unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            # df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            two_unit_x = angle_of_two_unit_vectors(points[3,0], points[3,1], points[3,2], points[4,0], points[4,1], points[4,2], 'x')
            two_unit_y = angle_of_two_unit_vectors(points[3,0], points[3,1], points[3,2], points[4,0], points[4,1], points[4,2], 'y')
            two_unit_z = angle_of_two_unit_vectors(points[3,0], points[3,1], points[3,2], points[4,0], points[4,1], points[4,2], 'z')
            df_deg = pd.DataFrame([[two_unit_x, two_unit_y, two_unit_z]], index = [i], columns = ['xX ' + df_labels.iat[f,0], 'yY ' + df_labels.iat[f,0], 'zZ ' + df_labels.iat[f,0]])
            df_deg1 = df_deg1.append(df_deg)
        elif f == 1:
            df_2 = df_2.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg2 = df_deg2.append(df_deg)
        elif f == 2:
            df_3 = df_3.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg3 = df_deg3.append(df_deg)
        elif f == 3:
            df_4 = df_4.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg4 = df_deg4.append(df_deg)
        elif f == 4:
            df_5 = df_5.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg5 = df_deg5.append(df_deg)
        elif f == 5:
            df_6 = df_6.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg6 = df_deg6.append(df_deg)
        elif f == 6:
            df_7 = df_7.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg7 = df_deg7.append(df_deg)
        elif f == 7:
            df_8 = df_8.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg8 = df_deg8.append(df_deg)
        elif f == 8:
            df_9 = df_9.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg9 = df_deg9.append(df_deg)
        elif f == 9:
            df_10 = df_10.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg10 = df_deg10.append(df_deg)
        else:
            # pass
            print("Hello World")
            break

# print(df_labels.iat[0,0])
# print(unit_x)
# print(type(unit_x))

with pd.ExcelWriter('saved_merge.xlsx') as writer1:
    df_1.to_excel(writer1, sheet_name = 'Raw Data', index = True)
    df_2.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 5)
    df_3.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 9)
    df_4.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 13)
    df_5.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 17)
    df_6.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 21)
    df_7.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 25)
    df_8.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 29)
    df_9.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 33)
    df_10.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol= 37)
    
    df_deg1.to_excel(writer1, sheet_name = 'Unit Angle', index = True, header = True)
    df_deg2.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 5)
    df_deg3.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 9)
    df_deg4.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 13)
    df_deg5.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 17)
    df_deg6.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 21)
    df_deg7.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 25)
    df_deg8.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 29)
    df_deg9.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 33)
    df_deg10.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 37)

    df_labels.to_excel(writer1, sheet_name = 'Point Labels', index = True)

    # workbook  = writer1.book
    # worksheet = writer1.sheets['Point Labels']
    # workbook.set_column(0, 1, 50)
    writer1.sheets['Point Labels'].set_column(2, 3, 15)

# writer1.save()
# writer1.close()