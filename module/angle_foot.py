import c3d
import pandas as pd
import numpy as np
import numpy.linalg as LA
import math
# import xlsxwriter

# path_select = input('File name: ')
# path = 'D:/Document/Mahidol University/OrthoRama/Python/' + path_select + '.c3d'
path = 'D:\Document\Mahidol University\OrthoRama\Angle\GaitModule\P Khaew test2 data\\KK test2 foot plantar flexion2A.c3d'
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

    if (u1 == 0 and u2 == 0) or (u1 == 0 and u3 == 0) or (u2 == 0 and u3 == 0) or (u1 == 0 and u2 == 0 and u3 == 0):
        deg = 'NA'
    else:
        inner = np.inner(a, b)
        norms = LA.norm(a) * LA.norm(b)

        cos = inner / norms
        rad = np.arccos(np.clip(cos, -1.0, 1.0))
        deg = np.rad2deg(np.clip(rad, -2.0 * math.pi, 2.0 * math.pi))

        if xyz == 'x':
            deg = deg
        elif xyz == 'y':
            deg = deg
        elif xyz == 'z':
            deg = deg
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

    if (u1 == 0 and u2 == 0) or (u1 == 0 and u3 == 0) or (u2 == 0 and u3 == 0) or (u1 == 0 and u2 == 0 and u3 == 0) or \
        (v1 == 0 and v2 == 0) or (v1 == 0 and v3 == 0) or (v2 == 0 and v3 == 0) or (v1 == 0 and v2 == 0 and v3 == 0):
        deg = 'NA'
    else:
        inner = np.inner(a, b)
        norms = LA.norm(a) * LA.norm(b)

        cos = inner / norms
        rad = np.arccos(np.clip(cos, -1.0, 1.0))
        deg = np.rad2deg(np.clip(rad, -2.0 * math.pi, 2.0 * math.pi))

        if xyz == 'x':
            deg = deg
        elif xyz == 'y':
            deg = deg
        elif xyz == 'z':
            deg = deg
        else:
            # pass
            print("Hello World")

    return deg

df_labels = pd.DataFrame()
df_deg_xyz = pd.DataFrame()

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
df_11 = pd.DataFrame()
df_12 = pd.DataFrame()
df_13 = pd.DataFrame()
df_14 = pd.DataFrame()
df_15 = pd.DataFrame()
df_16 = pd.DataFrame()
df_17 = pd.DataFrame()
df_18 = pd.DataFrame()
df_19 = pd.DataFrame()
df_20 = pd.DataFrame()
df_21 = pd.DataFrame()
df_22 = pd.DataFrame()

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
df_deg11 = pd.DataFrame()
df_deg12 = pd.DataFrame()
df_deg13 = pd.DataFrame()
df_deg14 = pd.DataFrame()
df_deg15 = pd.DataFrame()
df_deg16 = pd.DataFrame()
df_deg17 = pd.DataFrame()
df_deg18 = pd.DataFrame()
df_deg19 = pd.DataFrame()
df_deg20 = pd.DataFrame()
df_deg21 = pd.DataFrame()
df_deg22 = pd.DataFrame()

for i in range(reader.point_labels.size):
    # print('frame {}: point {}, analog {}'.format(i, reader.point_labels[i], reader.point_labels[1]))
    df_labels_loop = pd.DataFrame([reader.point_labels[i]], index = [i + 1], columns = ['Point Labels'])
    df_labels = df_labels.append(df_labels_loop)

for i, points, analog in reader.read_frames():
    for f in range(reader.point_labels.size):
        # print('frame {}: point {}, analog {}'.format(points[f,0], points[f,1], points[f,2]))
        # print('frame {}: point {}, analog {}'.format(i, points.shape, analog.shape))
        # print('frame {}: point {}'.format(i, points.all))
        # print(reader.point_labels[f])
        df_labels_loop = pd.DataFrame([[points[f,0], points[f,1], points[f,2]]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
        if f == 0:
            df_1 = df_1.append(df_labels_loop)
            # test = angle_of_two_vectors(points[f,0], points[f,1], points[f,2], points[f+1,0], points[f+1,1], points[f+1,2])
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
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
        elif f == 10:
            df_11 = df_11.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg11 = df_deg11.append(df_deg)
        elif f == 11:
            df_12 = df_12.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg12 = df_deg12.append(df_deg)
        elif f == 12:
            df_13 = df_13.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg13 = df_deg13.append(df_deg)
        elif f == 13:
            df_14 = df_14.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg14 = df_deg14.append(df_deg)
        elif f == 14:
            df_15 = df_15.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg15 = df_deg15.append(df_deg)
        elif f == 15:
            df_16 = df_16.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg16 = df_deg16.append(df_deg)
        elif f == 16:
            df_17 = df_17.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg17 = df_deg17.append(df_deg)
        elif f == 17:
            df_18 = df_18.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg18 = df_deg18.append(df_deg)
        elif f == 18:
            df_19 = df_19.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg19 = df_deg19.append(df_deg)
        elif f == 19:
            df_20 = df_20.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg20 = df_deg20.append(df_deg)
        elif f == 20:
            df_21 = df_21.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg21 = df_deg21.append(df_deg)
        elif f == 21:
            df_22 = df_22.append(df_labels_loop)
            unit_x = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'x')
            unit_y = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'y')
            unit_z = angle_of_unit_vectors(points[f,0], points[f,1], points[f,2], 'z')
            df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index = [i], columns = ['X ' + df_labels.iat[f,0], 'Y ' + df_labels.iat[f,0], 'Z ' + df_labels.iat[f,0]])
            df_deg22 = df_deg22.append(df_deg)
        else:
            # pass
            print("Hello World")
            break

# print(df_labels.iat[0,0])
# print(unit_x)
# print(type(unit_x))

with pd.ExcelWriter('saved_merge3.xlsx', engine='xlsxwriter') as writer1:
    df_1.to_excel(writer1, sheet_name = 'Raw Data', index = True)
    df_2.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 5)
    df_3.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 9)
    df_4.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 13)
    df_5.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 17)
    df_6.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 21)
    df_7.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 25)
    df_8.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 29)
    df_9.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 33)
    df_10.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 37)
    df_11.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 41)
    df_12.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 45)
    df_13.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 49)
    df_14.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 53)
    df_15.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 57)
    df_16.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 61)
    df_17.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 65)
    df_18.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 69)
    df_19.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 73)
    df_20.to_excel(writer1, sheet_name = 'Raw Data', index = False, startcol = 77)
    df_21.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 81)
    df_22.to_excel(writer1, sheet_name = 'Raw Data', index = None, startcol = 85)
    
    df_deg1.to_excel(writer1, sheet_name = 'Unit Angle', index = True, header = True)
    df_deg2.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 5)
    df_deg3.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 9)
    df_deg4.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 13)
    df_deg5.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 17)
    df_deg6.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 21)
    df_deg7.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 25)
    df_deg8.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 29)
    df_deg9.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 33)
    df_deg10.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 37)
    df_deg11.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol = 41)
    df_deg12.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 45)
    df_deg13.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 49)
    df_deg14.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 53)
    df_deg15.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 57)
    df_deg16.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 61)
    df_deg17.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 65)
    df_deg18.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 69)
    df_deg19.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 73)
    df_deg20.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol= 77)
    df_deg21.to_excel(writer1, sheet_name = 'Unit Angle', index = None, startcol = 81)
    df_deg22.to_excel(writer1, sheet_name = 'Unit Angle', index = False, startcol= 85)

    df_labels.to_excel(writer1, sheet_name = 'Point Labels', index = True)

    # workbook  = writer1.book
    # worksheet = writer1.sheets['Point Labels']
    # workbook.set_column(0, 1, 50)
    writer1.sheets['Point Labels'].set_column(2, 3, 15)

# writer1.save()
# writer1.close()