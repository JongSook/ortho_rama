from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog as fd
import c3d
import pandas as pd
import numpy as np
import numpy.linalg as LA
import math

screen = tk.Tk() # create root window
screen.title("Motion Module")
screen.config(bg="white")
screen.geometry("700x250+0+0")

# ---------------------------------- Function ---------------------------------------- #
def exitProgram():
    confirm = tkinter.messagebox.askquestion("Warning!", "Do you want to exit?")
    if confirm == 'yes':
        screen.destroy()
        print('exit')

def aboutProgram():
    tkinter.messagebox.showinfo("About", "Designed by JongSook \n\nProblem with this program please contact: \njongsook.san@gmail.com")

def angleUnitVector_1pt(u1, u2, u3, xyz):
    a = np.array([u1, u2, u3])

    if xyz == 'x':
        b = np.array([1,0,0])
    elif xyz == 'y':
        b = np.array([0,1,0])
    elif xyz == 'z':
        b = np.array([0,0,1])
    else:
        print("Hello World") # pass
        
    if (u1==0 and u2==0) or (u1==0 and u3==0) or (u2==0 and u3==0) or (u1==0 and u2==0 and u3==0):
        deg = 'NA'
    else:
        inner = np.inner(a, b)
        norms = LA.norm(a) * LA.norm(b)
        cos = inner / norms
        rad = np.arccos(np.clip(cos, -1.0, 1.0))
        deg = np.rad2deg(np.clip(rad, -2.0*math.pi, 2.0*math.pi))

        if xyz == 'x':
            deg = deg
        elif xyz == 'y':
            deg = deg
        elif xyz == 'z':
            deg = deg
        else:
            print("Hello World") # pass

    return deg

def angleUnitVector_2pt(u1, u2, u3, v1, v2, v3, xyz):
    a = np.array([u1-v1, u2-v2, u3-v3])

    if xyz == 'x': # flexion/extension # deg = 90 - deg
        b = np.array([1,0,0])
    elif xyz == 'y' or xyz == 'yy': # rotation # deg = deg - 90
        b = np.array([0,1,0])
    elif xyz == 'z' or xyz == 'zz': # right/left # deg = deg
        b = np.array([0,0,1])
    else:
        print("Hello World") # pass

    if (u1==0 and u2==0) or (u1==0 and u3==0) or (u2==0 and u3==0) or (u1==0 and u2==0 and u3==0) or \
        (v1==0 and v2==0) or (v1==0 and v3==0) or (v2==0 and v3==0) or (v1==0 and v2==0 and v3==0):
        deg = 0
    else:
        inner = np.inner(a, b)
        norms = LA.norm(a) * LA.norm(b)
        cos = inner / norms
        rad = np.arccos(np.clip(cos, -1.0, 1.0))
        deg = np.rad2deg(np.clip(rad, -2.0*math.pi, 2.0*math.pi))

        if moduleVar.get() == 1:
            if xyz == 'x': # flexion/extension
                deg = deg - 90
            elif xyz == 'y': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = deg - 90
            elif xyz == 'z': # internal/external rotation sagittal
                deg = deg - 90
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 2:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # pronation/supination
                deg = deg - 90
            elif xyz == 'z': # flexion/extension
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 3:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # radial/ulnar transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'z': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 4:
            if xyz == 'x': # flexion/extension
                deg = (deg - 90) * (-1)
            elif xyz == 'y': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'z': # internal/external rotation sagittal
                deg = (deg - 90) * (-1)
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 5:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # pronation/supination
                deg = (deg -90) * (-1)
            elif xyz == 'z': # flexion/extension
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 6:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # radial/ulnar transverse
                deg = deg - 90
            elif xyz == 'z': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            else:
                print("Hello World") # pass
        else:
            print('Hello World')

    return deg

def selectFile():
    # show the open file dialog
    fileType = (('C3D File', '*.c3d'),('All files', '*.*'))
    print(fileType)
    fileName = fd.askopenfilename(filetypes=fileType)
    textString.set(fileName)
    moduleVar.set(1)

    global reader
    pathOpen = fileName
    reader = c3d.Reader(open(pathOpen, 'rb'))
    print(reader)
     
    #disable&enable
    fileBTN.config(state=DISABLED)
    clearBTN.config(state=NORMAL)
    runBTN.config(state=NORMAL)
    saveBTN.config(state=DISABLED)

    module_1.config(state=NORMAL)
    module_2.config(state=NORMAL)
    module_3.config(state=NORMAL)
    module_4.config(state=NORMAL)
    module_5.config(state=NORMAL)
    module_6.config(state=NORMAL)

    statusString.set("Open File")
    print('file')

def runFile():
    checkModule()
    labelData()
    xyzData()

    #disable&enable
    fileBTN.config(state=DISABLED)
    clearBTN.config(state=NORMAL)
    runBTN.config(state=DISABLED)
    saveBTN.config(state=NORMAL)

    module_1.config(state=DISABLED)
    module_2.config(state=DISABLED)
    module_3.config(state=DISABLED)
    module_4.config(state=DISABLED)
    module_5.config(state=DISABLED)
    module_6.config(state=DISABLED)

    print('run')
    statusString.set("Completed Run")

def labelData():
    global df_label
    df_label = pd.DataFrame()

    for i in range(reader.point_labels.size):
        df_labelsLoop = pd.DataFrame([reader.point_labels[i]], index=[i+1], columns=['Point Labels'])
        df_label = df_label.append(df_labelsLoop)

    print('label...')

def xyzData():
    global df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15
    global df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24, df_25, df_26, df_27, df_28, df_29, df_30
    df_1 = pd.DataFrame(); df_2 = pd.DataFrame(); df_3 = pd.DataFrame(); df_4 = pd.DataFrame(); df_5 = pd.DataFrame()
    df_6 = pd.DataFrame(); df_7 = pd.DataFrame(); df_8 = pd.DataFrame(); df_9 = pd.DataFrame(); df_10 = pd.DataFrame()
    df_11 = pd.DataFrame(); df_12 = pd.DataFrame(); df_13 = pd.DataFrame(); df_14 = pd.DataFrame(); df_15 = pd.DataFrame()
    df_16 = pd.DataFrame(); df_17 = pd.DataFrame(); df_18 = pd.DataFrame(); df_19 = pd.DataFrame(); df_20 = pd.DataFrame()
    df_21 = pd.DataFrame(); df_22 = pd.DataFrame(); df_23 = pd.DataFrame(); df_24 = pd.DataFrame(); df_25 = pd.DataFrame()
    df_26 = pd.DataFrame(); df_27 = pd.DataFrame(); df_28 = pd.DataFrame(); df_29 = pd.DataFrame(); df_30 = pd.DataFrame()

    global df_deg1, df_deg2, df_deg3, df_deg4, df_deg5, df_deg6, df_deg7, df_deg8, df_deg9, df_deg10
    global df_deg11, df_deg12, df_deg13, df_deg14, df_deg15, df_deg16, df_deg17, df_deg18, df_deg19, df_deg20
    global df_deg21, df_deg22, df_deg23, df_deg24, df_deg25, df_deg26, df_deg27, df_deg28, df_deg29, df_deg30
    df_deg1 = pd.DataFrame(); df_deg2 = pd.DataFrame(); df_deg3 = pd.DataFrame(); df_deg4 = pd.DataFrame(); df_deg5 = pd.DataFrame()
    df_deg6 = pd.DataFrame(); df_deg7 = pd.DataFrame(); df_deg8 = pd.DataFrame(); df_deg9 = pd.DataFrame(); df_deg10 = pd.DataFrame()
    df_deg11 = pd.DataFrame(); df_deg12 = pd.DataFrame(); df_deg13 = pd.DataFrame(); df_deg14 = pd.DataFrame(); df_deg15 = pd.DataFrame()
    df_deg16 = pd.DataFrame(); df_deg17 = pd.DataFrame(); df_deg18 = pd.DataFrame(); df_deg19 = pd.DataFrame(); df_deg20 = pd.DataFrame()
    df_deg21 = pd.DataFrame(); df_deg22 = pd.DataFrame(); df_deg23 = pd.DataFrame(); df_deg24 = pd.DataFrame(); df_deg25 = pd.DataFrame()
    df_deg26 = pd.DataFrame(); df_deg27 = pd.DataFrame(); df_deg28 = pd.DataFrame(); df_deg29 = pd.DataFrame(); df_deg30 = pd.DataFrame()

    global df_degXYZ, df_value, df_valueXYZ
    df_degXYZ = pd.DataFrame()
    df_value = pd.DataFrame()
    df_valueXYZ = pd.DataFrame()

    for i, points, analog in reader.read_frames():
        for f in range(reader.point_labels.size):
            df_labelsLoop = pd.DataFrame([[points[f,0], points[f,1], points[f,2]]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
            if f == 0:
                df_1 = df_1.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg1 = df_deg1.append(df_deg)
            elif f == 1:
                df_2 = df_2.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg2 = df_deg2.append(df_deg)
            elif f == 2:
                df_3 = df_3.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg3 = df_deg3.append(df_deg)
            elif f == 3:
                df_4 = df_4.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg4 = df_deg4.append(df_deg)
            elif f == 4:
                df_5 = df_5.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg5 = df_deg5.append(df_deg)
            elif f == 5:
                df_6 = df_6.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg6 = df_deg6.append(df_deg)
            elif f == 6:
                df_7 = df_7.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg7 = df_deg7.append(df_deg)
            elif f == 7:
                df_8 = df_8.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg8 = df_deg8.append(df_deg)
            elif f == 8:
                df_9 = df_9.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg9 = df_deg9.append(df_deg)
            elif f == 9:
                df_10 = df_10.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg10 = df_deg10.append(df_deg)
            elif f == 10:
                df_11 = df_11.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg11 = df_deg11.append(df_deg)
            elif f == 11:
                df_12 = df_12.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg12 = df_deg12.append(df_deg)
            elif f == 12:
                df_13 = df_13.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg13 = df_deg13.append(df_deg)
            elif f == 13:
                df_14 = df_14.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg14 = df_deg14.append(df_deg)
            elif f == 14:
                df_15 = df_15.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg15 = df_deg15.append(df_deg)
            elif f == 15:
                df_16 = df_16.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg16 = df_deg16.append(df_deg)
            elif f == 16:
                df_17 = df_17.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg17 = df_deg17.append(df_deg)
            elif f == 17:
                df_18 = df_18.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg18 = df_deg18.append(df_deg)
            elif f == 18:
                df_19 = df_19.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg19 = df_deg19.append(df_deg)
            elif f == 19:
                df_20 = df_20.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg20 = df_deg20.append(df_deg)
            elif f == 20:
                df_21 = df_21.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg21 = df_deg21.append(df_deg)
            elif f == 21:
                df_22 = df_22.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg22 = df_deg22.append(df_deg)
            elif f == 22:
                df_23 = df_23.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg23 = df_deg23.append(df_deg)
            elif f == 23:
                df_24 = df_24.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg24 = df_deg24.append(df_deg)
            elif f == 24:
                df_25 = df_25.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg25 = df_deg25.append(df_deg)
            elif f == 25:
                df_26 = df_26.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg26 = df_deg26.append(df_deg)
            elif f == 26:
                df_27 = df_27.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg27 = df_deg27.append(df_deg)
            elif f == 27:
                df_28 = df_28.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg28 = df_deg28.append(df_deg)
            elif f == 28:
                df_29 = df_29.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg29 = df_deg29.append(df_deg)
            elif f == 29:
                df_30 = df_30.append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg30 = df_deg30.append(df_deg)
            else:
                print("Hello World") # pass
                break

    for i, points, analog in reader.read_frames():
        time = ((i/120)*1)-(1/120)        
        if moduleVar.get() == 1: # right shoulder
            # two_unit_x = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x') * (-1)
            # two_unit_xx = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x')
            # two_unit_y = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'y') * (-1)
            # two_unit_z = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'y') * (-1)
            # two_unit_0 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'y') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'y')) /2) * (-1)
            # two_unit_1 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'z')) /2) * (-1)
            two_unit_x = angleUnitVector_2pt(points[12,0], points[12,1], points[12,2], points[11,0], points[11,1], points[11,2], 'y') * (1) # 11 12
            two_unit_xx = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x')
            two_unit_y = angleUnitVector_2pt(points[11,0], points[11,1], points[11,2], points[12,0], points[12,1], points[12,2], 'y') * (1) # 11 12
            two_unit_z = angleUnitVector_2pt(points[11,0], points[11,1], points[11,2], points[12,0], points[12,1], points[12,2], 'z') * (1) # 11 12
            two_unit_0 = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[9,0], points[9,1], points[9,2], 'y') * (1) # 11 12
            two_unit_1 = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[9,0], points[9,1], points[9,2], 'z') * (1) # 11 12
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_xx, two_unit_y, two_unit_z, two_unit_0, two_unit_1]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-EXT', 'R-ADD/ABD', 'R-HOR ADD/ABD', 'R-INT/EXT Tran', 'R-INT/EXT Sag'])
            df_degXYZ = df_degXYZ.append(df_deg)
        elif moduleVar.get() == 2: # right elbow
            two_unit_rx = (angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'z')) /2            
            two_unit_ry = angleUnitVector_2pt(points[11,0], points[11,1], points[11,2], points[12,0], points[12,1], points[12,2], 'y') * (1) # 11 12
            df_deg = pd.DataFrame([[round(time,3), two_unit_rx, two_unit_ry]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-PRO/SUP'])
            df_degXYZ = df_degXYZ.append(df_deg)
        elif moduleVar.get() == 3: # right wrist
            two_unit_rx = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'z')) /2
            two_unit_ry = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'y') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'y')) /2
            two_unit_rz = ((angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'z')) /2) * (-1)
            df_deg = pd.DataFrame([[round(time,3), two_unit_rx, two_unit_ry, two_unit_rz]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-Radial/Ulnar Tran', 'R-Radial/Ulnar Sag'])
            df_degXYZ = df_degXYZ.append(df_deg)
        elif moduleVar.get() == 4: # left shoulder
            two_unit_a = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'x')
            two_unit_aa = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'x')
            two_unit_b = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'y') * (-1)
            two_unit_c = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'y') * (-1)
            two_unit_d = ((angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'y') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'y')) /2) * (-1)
            two_unit_e = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'z') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'z')) /2
            df_deg = pd.DataFrame([[round(time,3), two_unit_a, two_unit_aa, two_unit_b, two_unit_c, two_unit_d, two_unit_e]], index = [i], columns = ['Time (s)', 'L-FL/EXT', 'L-EXT', 'L-ADD/ABD', 'L-HOR ADD/ABD', 'L-INT/EXT Tran', 'L-INT/EXT Sag'])
            df_degXYZ = df_degXYZ.append(df_deg)
        elif moduleVar.get() == 5: # left elbow
            two_unit_lx = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'z') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'z')) /2
            two_unit_ly = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[14,0], points[14,1], points[14,2], 'y') * (1)) # 13 14
            df_deg = pd.DataFrame([[round(time,3), two_unit_lx, two_unit_ly]], index = [i], columns = ['Time (s)', 'L-FL/EXT', 'L-PRO/SUP'])
            df_degXYZ = df_degXYZ.append(df_deg)
        elif moduleVar.get() == 6: # left wrist            
            two_unit_lx = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'z') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'z')) /2 
            two_unit_ly = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'y') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'y')) /2 
            two_unit_lz = ((angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'z') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'z')) /2) * (-1)
            df_deg = pd.DataFrame([[round(time,3), two_unit_lx, two_unit_ly, two_unit_lz]], index = [i], columns = ['Time (s)', 'L-FL/EXT', 'L-Radial/Ulnar Tran', 'L-Radial/Ulnar Sag'])
            df_degXYZ = df_degXYZ.append(df_deg)
        else:
            print('Hello World')

    if moduleVar.get() == 1:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-EXT', 'R-ADD/ABD', 'R-HOR ADD/ABD', 'R-INT/EXT Tran', 'R-INT/EXT Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 2:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-PRO/SUP']].agg(['min', 'max'])
    elif moduleVar.get() == 3:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-Radial/Ulnar Tran', 'R-Radial/Ulnar Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 4:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['L-FL/EXT', 'L-EXT', 'L-ADD/ABD', 'L-HOR ADD/ABD', 'L-INT/EXT Tran', 'L-INT/EXT Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 5:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['L-FL/EXT', 'L-PRO/SUP']].agg(['min', 'max'])
    elif moduleVar.get() == 6:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['L-FL/EXT', 'L-Radial/Ulnar Tran', 'L-Radial/Ulnar Sag']].agg(['min', 'max'])
    else:
        print('Hello World')

    print('raw data...')

def savefile():
    pathSave = (fd.asksaveasfilename(filetypes=(('Microsoft Excel Workbook', '*.xlsx'),('All files', '*.*'))))
    saveName = pathSave + '.xlsx'
    textString.set(saveName)
    
    with pd.ExcelWriter(saveName, engine='xlsxwriter') as writer:
        df_label.to_excel(writer, sheet_name='Point Labels', index=True)
        writer.sheets['Point Labels'].set_column(1, 1, 15)

        df_1.to_excel(writer, sheet_name='Raw Data', index=True)
        df_2.to_excel(writer, sheet_name='Raw Data', index=None, startcol=5)
        df_3.to_excel(writer, sheet_name='Raw Data', index=None, startcol=9)
        df_4.to_excel(writer, sheet_name='Raw Data', index=None, startcol=13)
        df_5.to_excel(writer, sheet_name='Raw Data', index=None, startcol=17)
        df_6.to_excel(writer, sheet_name='Raw Data', index=None, startcol=21)
        df_7.to_excel(writer, sheet_name='Raw Data', index=None, startcol=25)
        df_8.to_excel(writer, sheet_name='Raw Data', index=None, startcol=29)
        df_9.to_excel(writer, sheet_name='Raw Data', index=None, startcol=33)
        df_10.to_excel(writer, sheet_name='Raw Data', index=None, startcol=37)
        df_11.to_excel(writer, sheet_name='Raw Data', index=None, startcol=41)
        df_12.to_excel(writer, sheet_name='Raw Data', index=None, startcol=45)
        df_13.to_excel(writer, sheet_name='Raw Data', index=None, startcol=49)
        df_14.to_excel(writer, sheet_name='Raw Data', index=None, startcol=53)
        df_15.to_excel(writer, sheet_name='Raw Data', index=None, startcol=57)
        df_16.to_excel(writer, sheet_name='Raw Data', index=None, startcol=61)
        df_17.to_excel(writer, sheet_name='Raw Data', index=None, startcol=65)
        df_18.to_excel(writer, sheet_name='Raw Data', index=None, startcol=69)
        df_19.to_excel(writer, sheet_name='Raw Data', index=None, startcol=73)
        df_20.to_excel(writer, sheet_name='Raw Data', index=None, startcol=77)
        df_21.to_excel(writer, sheet_name='Raw Data', index=None, startcol=81)
        df_22.to_excel(writer, sheet_name='Raw Data', index=None, startcol=85)
        df_23.to_excel(writer, sheet_name='Raw Data', index=None, startcol=89)
        df_24.to_excel(writer, sheet_name='Raw Data', index=None, startcol=93)
        df_25.to_excel(writer, sheet_name='Raw Data', index=None, startcol=97)
        df_26.to_excel(writer, sheet_name='Raw Data', index=None, startcol=101)
        df_27.to_excel(writer, sheet_name='Raw Data', index=None, startcol=105)
        df_28.to_excel(writer, sheet_name='Raw Data', index=None, startcol=109)
        df_29.to_excel(writer, sheet_name='Raw Data', index=None, startcol=113)
        df_30.to_excel(writer, sheet_name='Raw Data', index=None, startcol=117)

        df_deg1.to_excel(writer, sheet_name='Unit Angle', index=True, header=True)
        df_deg2.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=5)
        df_deg3.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=9)
        df_deg4.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=13)
        df_deg5.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=17)
        df_deg6.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=21)
        df_deg7.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=25)
        df_deg8.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=29)
        df_deg9.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=33)
        df_deg10.to_excel(writer, sheet_name='Unit Angle', index=False, startcol=37)
        df_deg11.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=41)
        df_deg12.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=45)
        df_deg13.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=49)
        df_deg14.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=53)
        df_deg15.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=57)
        df_deg16.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=61)
        df_deg17.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=65)
        df_deg18.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=69)
        df_deg19.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=73)
        df_deg20.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=77)
        df_deg21.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=81)
        df_deg22.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=85)
        df_deg23.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=89)
        df_deg24.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=93)
        df_deg25.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=97)
        df_deg26.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=101)
        df_deg27.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=105)
        df_deg28.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=109)
        df_deg29.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=113)
        df_deg30.to_excel(writer, sheet_name='Unit Angle', index=None, startcol=117)

        if moduleVar.get() == 1 or moduleVar.get() == 4:
            df_degXYZ.to_excel(writer, sheet_name='XYZ', index=True)
            df_value.to_excel(writer, sheet_name='XYZ', index=True, startcol=9)
            writer.sheets['XYZ'].set_column(2, 7, 15)
            writer.sheets['XYZ'].set_column(10, 15, 15)
        elif moduleVar.get() == 2 or moduleVar.get() == 5:
            df_degXYZ.to_excel(writer, sheet_name='XYZ', index=True)
            df_value.to_excel(writer, sheet_name='XYZ', index=True, startcol=5)
            writer.sheets['XYZ'].set_column(2, 3, 15)
            writer.sheets['XYZ'].set_column(6, 7, 15)
        elif moduleVar.get() == 3 or moduleVar.get() == 6:
            df_degXYZ.to_excel(writer, sheet_name='XYZ', index=True)
            df_value.to_excel(writer, sheet_name='XYZ', index=True, startcol=6)
            writer.sheets['XYZ'].set_column(2, 4, 15)
            writer.sheets['XYZ'].set_column(7, 9, 15)
        else:
            print('Hello World')

        workbook  = writer.book
        worksheet = writer.sheets['XYZ']
        (maxRow, maxCol) = df_degXYZ.shape

        if moduleVar.get() == 1:
            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N16', chart_z)

            chart_0 = workbook.add_chart({'type': 'line'})
            chart_0.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_0.set_title({'name': 'Right Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_0.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_0.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_0.set_legend({'position': 'none'})
            chart_0.set_size({'width': 360, 'height': 216})
            chart_0.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J27', chart_0)

            chart_1 = workbook.add_chart({'type': 'line'})
            chart_1.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_1.set_title({'name': 'Right Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_1.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_1.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_1.set_legend({'position': 'none'})
            chart_1.set_size({'width': 360, 'height': 216})
            chart_1.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N27', chart_1)
        elif moduleVar.get() == 2:
            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H16', chart_y)
        elif moduleVar.get() == 3:
            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H27', chart_z)
        elif moduleVar.get() == 4:
            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J5', chart_a)
           
            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J16', chart_b)

            chart_c = workbook.add_chart({'type': 'line'})
            chart_c.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_c.set_title({'name': 'Left Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_c.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_c.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_c.set_legend({'position': 'none'})
            chart_c.set_size({'width': 360, 'height': 216})
            chart_c.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N16', chart_c)

            chart_d = workbook.add_chart({'type': 'line'})
            chart_d.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_d.set_title({'name': 'Left Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_d.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_d.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_d.set_legend({'position': 'none'})
            chart_d.set_size({'width': 360, 'height': 216})
            chart_d.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J27', chart_d)

            chart_e = workbook.add_chart({'type': 'line'})
            chart_e.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_e.set_title({'name': 'Left Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_e.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_e.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_e.set_legend({'position': 'none'})
            chart_e.set_size({'width': 360, 'height': 216})
            chart_e.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N27', chart_e)
        elif moduleVar.get() == 5:
            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H16', chart_a)
        elif moduleVar.get() == 6:
            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H16', chart_a)

            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['XYZ', 1, 1, maxRow, 1], 'values': ['XYZ', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H27', chart_b)
        else:
            print('Hello World')

    #disable&enable
    fileBTN.config(state=DISABLED)
    clearBTN.config(state=NORMAL)
    runBTN.config(state=NORMAL)
    saveBTN.config(state=DISABLED)

    module_1.config(state=NORMAL)
    module_2.config(state=NORMAL)
    module_3.config(state=NORMAL)
    module_4.config(state=NORMAL)
    module_5.config(state=NORMAL)
    module_6.config(state=NORMAL)

    moduleVar.set(1)

    print('save')
    statusString.set("Completed Save")

def clearFile():
    checkModule()
    moduleVar.set(NONE)
    textString.set('Empty File')

    #disable&enable
    fileBTN.config(state=NORMAL)
    clearBTN.config(state=DISABLED)
    runBTN.config(state=DISABLED)
    saveBTN.config(state=DISABLED)

    module_1.config(state=DISABLED)
    module_2.config(state=DISABLED)
    module_3.config(state=DISABLED)
    module_4.config(state=DISABLED)
    module_5.config(state=DISABLED)
    module_6.config(state=DISABLED)

    print('clear')
    statusString.set("Completed Clear")

def checkModule():
    if moduleVar.get() == 1:
        print('right shoulder')
    elif moduleVar.get() == 2:
        print("right elbow")
    elif moduleVar.get() == 3:
        print('right wrist')
    elif moduleVar.get() == 4:
        print("left shoulder")
    elif moduleVar.get() == 5:
        print('left elbow')
    elif moduleVar.get() == 6:
        print("left wrist")
    else:
        print('Hello World')

# -------------------------------- Menu Bar -------------------------------------- #
screenMenu = tk.Menu(tearoff=False)
screen.config(menu=screenMenu)

#Create menu item
fileItem = tk.Menu(tearoff=False)
fileItem.add_command(label="About", command=aboutProgram)
fileItem.add_separator()
fileItem.add_command(label="Exit", command=exitProgram)

#Create menu bar
screenMenu.add_cascade(label="Menu", menu=fileItem)

#----------------------------Create Frame widget------------------------------------#
frameTop = tk.Frame(screen, bg='white')
frameTop.pack(fill=BOTH, side=TOP, expand=True)
frameLeft = tk.Frame(screen, bg='white')
frameLeft.pack(fill=BOTH, side=LEFT, expand=True)
frameRight = Frame(screen, bg='white')
frameRight.pack(fill=BOTH, side=RIGHT, expand=True)

#------------------------------Grouping Widget--------------------------------------#
fileFrame = tk.LabelFrame(frameTop, text='Selected File', fg="black", bg='white', labelanchor=N, width=690, height=100)
fileFrame.pack(side=TOP)
commandFrame = tk.LabelFrame(frameLeft, text='Selected Module', fg="black", bg='white', pady=10, padx=35, labelanchor=N)
commandFrame.pack(side=BOTTOM, anchor=E,pady=10, padx=5)
# commandFrame.grid(in_=frameLeft, column=0, row=1, pady=10, padx=5)
textFrame = tk.LabelFrame(frameRight, text='Status', fg="black", bg='white', width=100, height=113, labelanchor=N)
textFrame.pack(side=BOTTOM, pady=10, anchor=SE,padx=5, ipady=10, ipadx=59)
# textFrame.grid(in_=frameRight, column=1, row=1, pady=10, padx=5, ipady=10, ipadx=59)

#top label
textString = tk.StringVar()
textString.set("File Name")
fileLabel = tk.Label(frameTop, textvariable=textString, fg='black', bg='white')
fileLabel.place(in_=fileFrame, x=340, y=20, anchor=CENTER)

#button
fileBTN = tk.Button(fileFrame, text='Open File', height=1, width=20, relief="ridge", command=selectFile)
fileBTN.place(in_=fileFrame, x=200, y=60, anchor=CENTER)
# newFile_btn = tk.Button(File_frame, text='Open New File', state=DISABLED, height=1, width=20, relief="ridge", command=new_files)
# newFile_btn.place(in_=File_frame, x=345, y=60, anchor=CENTER)
clearBTN = tk.Button(fileFrame, text='Clear File', state=DISABLED, height=1, width=20, relief="ridge", command=clearFile)
clearBTN.place(in_=fileFrame, x=500, y=60, anchor=CENTER)

#radio button
moduleVar = tk.IntVar()
# tk.Label(Bottom_frame, text='Selected Module', fg='black', bg='white').grid(in_=Command_frame, column=0, row=1)
module_1 = tk.Radiobutton(frameLeft, text='Right  Shoulder', state=DISABLED, variable=moduleVar, value=1, bg='white')
module_1.grid(in_=commandFrame, column=0, row=1, pady=2)
module_2 = tk.Radiobutton(frameLeft, text='Right Elbow    ', state=DISABLED, variable=moduleVar, value=2, bg='white')
module_2.grid(in_=commandFrame, column=2, row=1, pady=2)
module_3 = tk.Radiobutton(frameLeft, text='Right Wrist    ', state=DISABLED, variable=moduleVar, value=3, bg='white')
module_3.grid(in_=commandFrame, column=4, row=1, pady=2)
module_4 = tk.Radiobutton(frameLeft, text='Left Shoulder   ', state=DISABLED, variable=moduleVar, value=4, bg='white')
module_4.grid(in_=commandFrame, column=0, row=2, pady=2)
module_5 = tk.Radiobutton(frameLeft, text='Left Elbow       ', state=DISABLED, variable=moduleVar, value=5, bg='white')
module_5.grid(in_=commandFrame, column=2, row=2, pady=2)
module_6 = tk.Radiobutton(frameLeft, text='Left Wrist      ', state=DISABLED, variable=moduleVar, value=6, bg='white')
module_6.grid(in_=commandFrame, column=4, row=2, pady=2)
moduleVar.set(NONE)

#button
runBTN = tk.Button(commandFrame, text='Run Module', state=DISABLED, height=1, width=20, relief="ridge", command=runFile)
runBTN.grid(columnspan=2, row=3, column=0, padx=3, pady=5)
saveBTN = tk.Button(commandFrame, text='Save File', state=DISABLED, height=1, width=20, relief="ridge", command=savefile)
saveBTN.grid(columnspan=2, row=3, column=3, padx=3, pady=5)

#left label
statusString = tk.StringVar()
statusString.set("Hello User")
status_label = tk.Label(textFrame, textvariable=statusString, fg='black', bg='white')
status_label.place(in_=textFrame, x=108, y=50, anchor=CENTER)

screen.mainloop()