##########################
##### import librery #####
##########################
import c3d
import pandas as pd
import numpy as np
import numpy.linalg as LA
import math
# import xlsxwriter

###########################
##### file management #####
###########################
# path_select = input('File name: ')
# path = 'D:/Document/Mahidol University/OrthoRama/Python/' + path_select + '.c3d'
# path = 'D:\Document\Mahidol University\OrthoRama\Python\sample01\\Neck P khaew right rotate1.c3d'
# reader = c3d.Reader(open(path, 'rb'))

# save_file = 'saved_merge1.xlsx'
# save_file = path.replace('D:\Document\Mahidol University\OrthoRama\Python\sample01\\', '').replace('.c3d', '') + '.xlsx'
# save = path.replace('D:\Document\Mahidol University\OrthoRama\Python\sample01\\', '')
# save_file = save.replace('.c3d', '') + '.xlsx'

file_name = 'Trimmed_KK test2 neck rt.rotation2A'
file_open = 'D:\\Document\\Mahidol University\\OrthoRama\\Python\\sample01'
file_save = 'D:\\Document\\Mahidol University\\OrthoRama\\Python'

file_c3d = file_name + '.c3d'
path_open = file_open + '\\' + file_c3d
path_save = file_save + '\\' + file_c3d.replace('.c3d', '') + '.xlsx'
reader = c3d.Reader(open(path_open, 'rb'))

#########################
##### function part #####
#########################
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

    if xyz == 'x': # flexion/extension
        b = np.array([1, 0, 0])
    elif xyz == 'y': # rotation
        b = np.array([0, 1, 0])
    elif xyz == 'z': # right/left
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

        if xyz == 'x': # flexion/extension
            deg = deg
        elif xyz == 'y': # rotation
            deg = deg
        elif xyz == 'z': # right/left
            deg = deg
        else:
            # pass
            print("Hello World")

    return deg

def angle_of_two_unit_vectors(u1, u2, u3, v1, v2, v3, xyz):
    a = np.array([u1 - v1, u2 - v2, u3 - v3])

    if xyz == 'x': # flexion/extension # deg = 90 - deg
        b = np.array([1, 0, 0])
    elif xyz == 'y': # rotation # deg = deg - 90
        b = np.array([0, 1, 0])
    elif xyz == 'z': # right/left # deg = deg
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

        if xyz == 'x': # flexion/extension # deg = 90 - deg
            deg = 90 - deg
        elif xyz == 'y': # rotation # deg = deg - 90
            deg = deg - 90
        elif xyz == 'z': # right/left # deg = deg
            deg = deg
        else:
            # pass
            print("Hello World")

    return deg

############################
##### calculation part #####
############################
df_labels = pd.DataFrame()
df_deg_xyz = pd.DataFrame()
df_time = pd.DataFrame()
df_value = pd.DataFrame()
df_value_xyz = pd.DataFrame()

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

for i in range(reader.point_labels.size):
    # print('frame {}: point {}, analog {}'.format(i, reader.point_labels[i], reader.point_labels[1]))
    df_labels_loop = pd.DataFrame([reader.point_labels[i]], index = [i + 1], columns = ['Point Labels'])
    df_labels = df_labels.append(df_labels_loop)

for i, points, analog in reader.read_frames():
    time = ((i/120)*1)-(1/120)
    two_unit_x = angle_of_two_unit_vectors(points[4,0], points[4,1], points[4,2], points[3,0], points[3,1], points[3,2], 'x')
    two_unit_y = angle_of_two_unit_vectors(points[2,0], points[2,1], points[2,2], points[1,0], points[1,1], points[1,2], 'y')
    two_unit_z = angle_of_two_unit_vectors(points[0,0], points[0,1], points[0,2], points[4,0], points[4,1], points[4,2], 'y')
    df_deg = pd.DataFrame([[two_unit_x, two_unit_y, two_unit_z, time]], index = [i], columns = ['xX FL/EXT', 'yY ROT', 'zZ L/R', 'Time'])
    df_deg_xyz = df_deg_xyz.append(df_deg)
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
        else:
            # pass
            print("Hello World")
            break

df_value_xyz = df_deg_xyz[df_deg_xyz != 0]
df_value = df_value_xyz[['xX FL/EXT', 'yY ROT', 'zZ L/R']].agg(['min','max'])

# print(df_labels.iat[0,0])
# print(unit_x)
# print(type(unit_x))

###########################
##### saved data part #####
###########################
# with pd.ExcelWriter('D:\\Document\\Mahidol University\\OrthoRama\\Python\\sample01\\Neck P khaew right rotate1.xlsx') as writer1:
with pd.ExcelWriter(path_save, engine='xlsxwriter') as writer1:
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

    df_deg_xyz.to_excel(writer1, sheet_name = 'XYZ', index = True)
    df_value.to_excel(writer1, sheet_name = 'XYZ', index = True, startcol= 6)

    df_labels.to_excel(writer1, sheet_name = 'Point Labels', index = True)

    # workbook  = writer1.book
    # worksheet = writer1.sheets['Point Labels']
    # workbook.set_column(0, 1, 50)
    writer1.sheets['XYZ'].set_column(1, 3, 15)
    writer1.sheets['Point Labels'].set_column(1, 1, 15)

    workbook  = writer1.book
    worksheet = writer1.sheets['XYZ']
    (max_row, max_col) = df_deg_xyz.shape

    chart_x = workbook.add_chart({'type': 'line'})
    chart_x.add_series({'categories': ['XYZ', 1, 4, i, 4], 'values': ['XYZ', 1, 1, max_row, 1], 'line': {'color': '#0000FF', 'width': 1.2}})
    chart_x.set_title({'name': 'Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
    chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
    chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
    chart_x.set_legend({'position': 'none'})
    chart_x.set_size({'width': 360, 'height': 216})
    chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
    worksheet.insert_chart('G2', chart_x) # , {'x_scale': 1.5, 'y_scale': 1.5}

    chart_y = workbook.add_chart({'type': 'line'})
    chart_y.add_series({'values': ['XYZ', 1, 2, max_row, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
    chart_y.set_title({'name': 'Rotation', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
    chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'visible': False})
    chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
    chart_y.set_legend({'position': 'none'})
    chart_y.set_size({'width': 360, 'height': 216})
    chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.8}})
    worksheet.insert_chart('G14', chart_y)

    chart_z = workbook.add_chart({'type': 'line'})
    chart_z.add_series({'values': ['XYZ', 1, 3, max_row, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
    chart_z.set_title({'name': 'Left/Right', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
    chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'visible': False})
    chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
    chart_z.set_legend({'position': 'none'})
    chart_z.set_size({'width': 360, 'height': 216})
    chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.8}})
    worksheet.insert_chart('M2', chart_z)

# writer1.save()
# writer1.close()