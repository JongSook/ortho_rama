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
screen.geometry("700x350+0+0")

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

    if xyz == 'x' or xyz == 'sh_x' or xyz == 'el_x' or xyz == 'wr_x':
        b = np.array([1,0,0])
    elif xyz == 'y' or xyz == 'sh_y' or xyz == 'el_y' or xyz == 'wr_y':
        b = np.array([0,1,0])
    elif xyz == 'z' or xyz == 'sh_z' or xyz == 'el_z' or xyz == 'wr_z':
        b = np.array([0,0,1])
    elif  xyz == 'xx' or xyz == 'sh_xx' or xyz == 'el_xx' or xyz == 'wr_xx':
        b = np.array([1,0,0])
    elif xyz == 'yy' or xyz == 'sh_yy' or xyz == 'el_yy' or xyz == 'wr_yy':
        b = np.array([0,1,0])
    elif xyz == 'zz' or xyz == 'sh_zz' or xyz == 'el_zz' or xyz == 'wr_zz':
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

        if moduleVar.get() == 1: # neck
            if xyz == 'x': # flexion/extension
                deg = 90 - deg
            elif xyz == 'y': # rotation, right/left
                deg = deg - 90
            elif xyz == 'z':
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 2: # back
            if xyz == 'x': # flexion/extension, rotation
                deg = deg - 90
            elif xyz == 'y': # right/left
                deg = deg - 90
            elif xyz == 'z':
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 3 or moduleVar.get() == 31 or moduleVar.get() == 32:
            if xyz == 'x': # eversion/inversion
                deg = deg - 110
            elif xyz == 'y':
                deg = deg
            elif xyz == 'z': # dorsiflexion/plantarflexion
                deg = deg - 90
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 4:
            if xyz == 'x': # flexion/extension
                deg = deg - 90
            elif xyz == 'y': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = deg - 90
            elif xyz == 'z': # internal/external rotation sagittal
                deg = deg - 90
            elif xyz == 'xx': # flexion/extension
                deg = (deg - 90) * (-1)
            elif xyz == 'yy': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'zz': # internal/external rotation sagittal
                deg = (deg - 90) * (-1)
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 5:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # pronation/supination
                deg = deg - 90
            elif xyz == 'z': # flexion/extension
                deg = deg
            elif xyz == 'xx':
                deg = deg
            elif xyz == 'yy': # pronation/supination
                deg = (deg -90) * (-1)
            elif xyz == 'zz': # flexion/extension
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 6:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # radial/ulnar transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'z': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            elif xyz == 'xx':
                deg = deg
            elif xyz == 'yy': # radial/ulnar transverse
                deg = deg - 90
            elif xyz == 'zz': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 41:
            if xyz == 'x': # flexion/extension
                deg = (deg - 90) * (-1)
            elif xyz == 'y': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'z': # internal/external rotation sagittal
                deg = (deg - 90) * (-1)
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 42:
            if xyz == 'x': # flexion/extension
                deg = deg - 90
            elif xyz == 'y': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = deg - 90
            elif xyz == 'z': # internal/external rotation sagittal
                deg = deg - 90
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 51:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # pronation/supination
                deg = (deg -90) * (-1)
            elif xyz == 'z': # flexion/extension
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 52:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # pronation/supination
                deg = deg - 90
            elif xyz == 'z': # flexion/extension
                deg = deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 61:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # radial/ulnar transverse
                deg = deg - 90
            elif xyz == 'z': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 62:
            if xyz == 'x':
                deg = deg
            elif xyz == 'y': # radial/ulnar transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'z': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            else:
                print("Hello World") # pass
        elif moduleVar.get() == 7:
            if xyz == 'sh_x': # flexion/extension
                deg = deg - 90
            elif xyz == 'sh_y': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = deg - 90
            elif xyz == 'sh_z': # internal/external rotation sagittal
                deg = deg - 90
            elif xyz == 'sh_xx': # flexion/extension
                deg = (deg - 90) * (-1)
            elif xyz == 'sh_yy': # adduction/abduction coronal, adduction/abduction transverse, internal/external rotation transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'sh_zz': # internal/external rotation sagittal
                deg = (deg - 90) * (-1)
            elif xyz == 'el_x':
                deg = deg
            elif xyz == 'el_y': # pronation/supination
                deg = deg - 90
            elif xyz == 'el_z': # flexion/extension
                deg = deg
            elif xyz == 'el_xx':
                deg = deg
            elif xyz == 'el_yy': # pronation/supination
                deg = (deg -90) * (-1)
            elif xyz == 'el_zz': # flexion/extension
                deg = deg
            elif xyz == 'wr_x':
                deg = deg
            elif xyz == 'wr_y': # radial/ulnar transverse
                deg = (deg - 90) * (-1)
            elif xyz == 'wr_z': # flexion/extension, radial/ulnar sagittal
                deg = 90 - deg
            elif xyz == 'wr_xx':
                deg = deg
            elif xyz == 'wr_yy': # radial/ulnar transverse
                deg = deg - 90
            elif xyz == 'wr_zz': # flexion/extension, radial/ulnar sagittal
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
    module_7.config(state=NORMAL)

    module_31.config(state=NORMAL)
    module_41.config(state=NORMAL)
    module_51.config(state=NORMAL)
    module_61.config(state=NORMAL)
    module_32.config(state=NORMAL)
    module_42.config(state=NORMAL)
    module_52.config(state=NORMAL)
    module_62.config(state=NORMAL)

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
    module_7.config(state=DISABLED)

    module_31.config(state=DISABLED)
    module_41.config(state=DISABLED)
    module_51.config(state=DISABLED)
    module_61.config(state=DISABLED)
    module_32.config(state=DISABLED)
    module_42.config(state=DISABLED)
    module_52.config(state=DISABLED)
    module_62.config(state=DISABLED)

    print('run')
    statusString.set("Completed Run")

def labelData():
    global df_label
    df_label = pd.DataFrame()

    for i in range(reader.point_labels.size):
        df_labelsLoop = pd.DataFrame([reader.point_labels[i]], index=[i+1], columns=['Point Labels'])
        df_label = df_label._append(df_labelsLoop)

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
                df_1 = df_1._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg1 = df_deg1._append(df_deg)
            elif f == 1:
                df_2 = df_2._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg2 = df_deg2._append(df_deg)
            elif f == 2:
                df_3 = df_3._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg3 = df_deg3._append(df_deg)
            elif f == 3:
                df_4 = df_4._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg4 = df_deg4._append(df_deg)
            elif f == 4:
                df_5 = df_5._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg5 = df_deg5._append(df_deg)
            elif f == 5:
                df_6 = df_6._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg6 = df_deg6._append(df_deg)
            elif f == 6:
                df_7 = df_7._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg7 = df_deg7._append(df_deg)
            elif f == 7:
                df_8 = df_8._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg8 = df_deg8._append(df_deg)
            elif f == 8:
                df_9 = df_9._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg9 = df_deg9._append(df_deg)
            elif f == 9:
                df_10 = df_10._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg10 = df_deg10._append(df_deg)
            elif f == 10:
                df_11 = df_11._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg11 = df_deg11._append(df_deg)
            elif f == 11:
                df_12 = df_12._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg12 = df_deg12._append(df_deg)
            elif f == 12:
                df_13 = df_13._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg13 = df_deg13._append(df_deg)
            elif f == 13:
                df_14 = df_14._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg14 = df_deg14._append(df_deg)
            elif f == 14:
                df_15 = df_15._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg15 = df_deg15._append(df_deg)
            elif f == 15:
                df_16 = df_16._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg16 = df_deg16._append(df_deg)
            elif f == 16:
                df_17 = df_17._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg17 = df_deg17._append(df_deg)
            elif f == 17:
                df_18 = df_18._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg18 = df_deg18._append(df_deg)
            elif f == 18:
                df_19 = df_19._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg19 = df_deg19._append(df_deg)
            elif f == 19:
                df_20 = df_20._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg20 = df_deg20._append(df_deg)
            elif f == 20:
                df_21 = df_21._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg21 = df_deg21._append(df_deg)
            elif f == 21:
                df_22 = df_22._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg22 = df_deg22._append(df_deg)
            elif f == 22:
                df_23 = df_23._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg23 = df_deg23._append(df_deg)
            elif f == 23:
                df_24 = df_24._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg24 = df_deg24._append(df_deg)
            elif f == 24:
                df_25 = df_25._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg25 = df_deg25._append(df_deg)
            elif f == 25:
                df_26 = df_26._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg26 = df_deg26._append(df_deg)
            elif f == 26:
                df_27 = df_27._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg27 = df_deg27._append(df_deg)
            elif f == 27:
                df_28 = df_28._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg28 = df_deg28._append(df_deg)
            elif f == 28:
                df_29 = df_29._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg29 = df_deg29._append(df_deg)
            elif f == 29:
                df_30 = df_30._append(df_labelsLoop)
                unit_x = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'x')
                unit_y = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'y')
                unit_z = angleUnitVector_1pt(points[f,0], points[f,1], points[f,2], 'z')
                df_deg = pd.DataFrame([[unit_x, unit_y, unit_z]], index=[i], columns=['X '+df_label.iat[f,0], 'Y '+df_label.iat[f,0], 'Z '+df_label.iat[f,0]])
                df_deg30 = df_deg30._append(df_deg)
            else:
                print("Hello World") # pass
                break

    for i, points, analog in reader.read_frames():
        time = ((i/120)*1)-(1/120)        
        if moduleVar.get() == 1: # neck
            two_unit_x = angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[3,0], points[3,1], points[3,2], 'x')
            two_unit_y = angleUnitVector_2pt(points[2,0], points[2,1], points[2,2], points[1,0], points[1,1], points[1,2], 'y') * (-1)
            two_unit_z = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[4,0], points[4,1], points[4,2], 'y')
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_y, two_unit_z]], index = [i], columns = ['Time (s)', 'FL/EXT', 'ROT', 'L/R'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 2: # back
            two_unit_x = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[10,0], points[10,1], points[10,2], 'x')
            two_unit_y = angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[5,0], points[5,1], points[5,2], 'x')              
            two_unit_z = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[10,0], points[10,1], points[10,2], 'y')  
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_y, two_unit_z]], index = [i], columns = ['Time (s)', 'FL/EXT', 'ROT', 'L/R'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 3: # foot            
            two_unit_x = (angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[7,0], points[7,1], points[7,2], 'z') + angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[8,0], points[8,1], points[8,2], 'z')) /2
            two_unit_y = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[16,0], points[16,1], points[16,2], 'z') + angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[17,0], points[17,1], points[17,2], 'z')) /2
            two_unit_z = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[8,0], points[8,1], points[8,2], 'x') - 5
            two_unit_a = angleUnitVector_2pt(points[16,0], points[16,1], points[16,2], points[17,0], points[17,1], points[17,2], 'x')
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_y, two_unit_z, two_unit_a]], index = [i], columns = ['Time (s)', 'R-DOR/PLA', 'L-DOR/PLA', 'R-EVE/INV', 'L-EVE/INV'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 31: # left foot            
            two_unit_x = (angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[7,0], points[7,1], points[7,2], 'z') + angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[8,0], points[8,1], points[8,2], 'z')) /2
            two_unit_y = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[16,0], points[16,1], points[16,2], 'z') + angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[17,0], points[17,1], points[17,2], 'z')) /2
            two_unit_z = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[8,0], points[8,1], points[8,2], 'x') - 5
            two_unit_a = angleUnitVector_2pt(points[16,0], points[16,1], points[16,2], points[17,0], points[17,1], points[17,2], 'x')
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_y, two_unit_z, two_unit_a]], index = [i], columns = ['Time (s)', 'R-DOR/PLA', 'L-DOR/PLA', 'R-EVE/INV', 'L-EVE/INV'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 32: # right foot            
            two_unit_x = (angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[7,0], points[7,1], points[7,2], 'z') + angleUnitVector_2pt(points[4,0], points[4,1], points[4,2], points[8,0], points[8,1], points[8,2], 'z')) /2
            two_unit_y = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[16,0], points[16,1], points[16,2], 'z') + angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[17,0], points[17,1], points[17,2], 'z')) /2
            two_unit_z = angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[8,0], points[8,1], points[8,2], 'x') - 5
            two_unit_a = angleUnitVector_2pt(points[16,0], points[16,1], points[16,2], points[17,0], points[17,1], points[17,2], 'x')
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_y, two_unit_z, two_unit_a]], index = [i], columns = ['Time (s)', 'R-DOR/PLA', 'L-DOR/PLA', 'R-EVE/INV', 'L-EVE/INV'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 4: # shoulder
            two_unit_x = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x') * (-1)
            two_unit_xx = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x')
            two_unit_y = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'y') * (-1)
            two_unit_z = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'y') * (-1)
            two_unit_0 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'y') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'y')) /2) * (-1)
            two_unit_1 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'z')) /2) * (-1)
            two_unit_a = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'xx')
            two_unit_aa = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'xx')
            two_unit_b = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'yy') * (-1)
            two_unit_c = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'yy') * (-1)
            two_unit_d = ((angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'yy') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'yy')) /2) * (-1)
            two_unit_e = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'zz') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'zz')) /2
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_xx, two_unit_y, two_unit_z, two_unit_0, two_unit_1, two_unit_a, two_unit_aa, two_unit_b, two_unit_c, two_unit_d, two_unit_e]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-EXT', 'R-ADD/ABD', 'R-HOR ADD/ABD', 'R-INT/EXT Tran', 'R-INT/EXT Sag', 'L-FL/EXT', 'L-EXT', 'L-ADD/ABD', 'L-HOR ADD/ABD', 'L-INT/EXT Tran', 'L-INT/EXT Sag'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 5: # elbow
            two_unit_rx = (angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'z')) /2            
            two_unit_ry = angleUnitVector_2pt(points[11,0], points[11,1], points[11,2], points[12,0], points[12,1], points[12,2], 'y') * (1) # 11 12
            two_unit_lx = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'zz') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'zz')) /2
            two_unit_ly = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[14,0], points[14,1], points[14,2], 'yy') * (1)) # 13 14
            df_deg = pd.DataFrame([[round(time,3), two_unit_rx, two_unit_ry, two_unit_lx, two_unit_ly]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-PRO/SUP', 'L-FL/EXT', 'L-PRO/SUP'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 6: # wrist
            two_unit_rx = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'z')) /2
            two_unit_ry = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'y') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'y')) /2
            two_unit_rz = ((angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'z')) /2) * (-1)
            two_unit_lx = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'zz') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'zz')) /2 
            two_unit_ly = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'yy') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'yy')) /2 
            two_unit_lz = ((angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'zz') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'zz')) /2) * (-1) 
            df_deg = pd.DataFrame([[round(time,3), two_unit_rx, two_unit_ry, two_unit_rz, two_unit_lx, two_unit_ly, two_unit_lz]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-Radial/Ulnar Tran', 'R-Radial/Ulnar Sag', 'L-FL/EXT', 'L-Radial/Ulnar Tran', 'L-Radial/Ulnar Sag'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 41: # left shoulder
            two_unit_a = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'x')
            two_unit_aa = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'x')
            two_unit_b = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'y') * (-1)
            two_unit_c = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'y') * (-1)
            two_unit_d = ((angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'y') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'y')) /2) * (-1)
            two_unit_e = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'z') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'z')) /2
            df_deg = pd.DataFrame([[round(time,3), two_unit_a, two_unit_aa, two_unit_b, two_unit_c, two_unit_d, two_unit_e]], index = [i], columns = ['Time (s)', 'L-FL/EXT', 'L-EXT', 'L-ADD/ABD', 'L-HOR ADD/ABD', 'L-INT/EXT Tran', 'L-INT/EXT Sag'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 42: # right shoulder
            two_unit_x = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x') * (-1)
            two_unit_xx = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'x')
            two_unit_y = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'y') * (-1)
            two_unit_z = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'y') * (-1)
            two_unit_0 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'y') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'y')) /2) * (-1)
            two_unit_1 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'z')) /2) * (-1)
            df_deg = pd.DataFrame([[round(time,3), two_unit_x, two_unit_xx, two_unit_y, two_unit_z, two_unit_0, two_unit_1]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-EXT', 'R-ADD/ABD', 'R-HOR ADD/ABD', 'R-INT/EXT Tran', 'R-INT/EXT Sag'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 51: # left elbow
            two_unit_lx = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'z') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'z')) /2
            two_unit_ly = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[14,0], points[14,1], points[14,2], 'y') * (1)) # 13 14
            df_deg = pd.DataFrame([[round(time,3), two_unit_lx, two_unit_ly]], index = [i], columns = ['Time (s)', 'L-FL/EXT', 'L-PRO/SUP'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 52: # right elbow
            two_unit_rx = (angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'z')) /2            
            two_unit_ry = angleUnitVector_2pt(points[11,0], points[11,1], points[11,2], points[12,0], points[12,1], points[12,2], 'y') * (1) # 11 12
            df_deg = pd.DataFrame([[round(time,3), two_unit_rx, two_unit_ry]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-PRO/SUP'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 61: # left wrist            
            two_unit_lx = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'z') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'z')) /2 
            two_unit_ly = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'y') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'y')) /2 
            two_unit_lz = ((angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'z') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'z')) /2) * (-1)
            df_deg = pd.DataFrame([[round(time,3), two_unit_lx, two_unit_ly, two_unit_lz]], index = [i], columns = ['Time (s)', 'L-FL/EXT', 'L-Radial/Ulnar Tran', 'L-Radial/Ulnar Sag'])
            df_degXYZ = df_degXYZ._append(df_deg)    
        elif moduleVar.get() == 62: # right wrist
            two_unit_rx = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'z')) /2
            two_unit_ry = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'y') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'y')) /2
            two_unit_rz = ((angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'z')) /2) * (-1)
            df_deg = pd.DataFrame([[round(time,3), two_unit_rx, two_unit_ry, two_unit_rz]], index = [i], columns = ['Time (s)', 'R-FL/EXT', 'R-Radial/Ulnar Tran', 'R-Radial/Ulnar Sag'])
            df_degXYZ = df_degXYZ._append(df_deg)
        elif moduleVar.get() == 7: # upper limb
            two_unit_sh_x = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'sh_x') * (-1)
            two_unit_sh_xx = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[7,0], points[7,1], points[7,2], 'sh_x')
            two_unit_sh_y = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'sh_y') * (-1)
            two_unit_sh_z = angleUnitVector_2pt(points[0,0], points[0,1], points[0,2], points[5,0], points[5,1], points[5,2], 'sh_y') * (-1)
            two_unit_sh_0 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'sh_y') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'sh_y')) /2) * (-1)
            two_unit_sh_1 = ((angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'sh_z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'sh_z')) /2) * (-1)
            two_unit_sh_a = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'sh_xx')
            two_unit_sh_aa = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[8,0], points[8,1], points[8,2], 'sh_xx')
            two_unit_sh_b = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'sh_yy') * (-1)
            two_unit_sh_c = angleUnitVector_2pt(points[1,0], points[1,1], points[1,2], points[6,0], points[6,1], points[6,2], 'sh_yy') * (-1)
            two_unit_sh_d = ((angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'sh_yy') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'sh_yy')) /2) * (-1)
            two_unit_sh_e = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'sh_zz') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'sh_zz')) /2

            two_unit_el_rx = (angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[9,0], points[9,1], points[9,2], 'el_z') + angleUnitVector_2pt(points[5,0], points[5,1], points[5,2], points[7,0], points[7,1], points[7,2], 'el_z')) /2            
            two_unit_el_ry = angleUnitVector_2pt(points[11,0], points[11,1], points[11,2], points[12,0], points[12,1], points[12,2], 'el_y') * (1) # 11 12
            two_unit_el_lx = (angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[8,0], points[8,1], points[8,2], 'el_zz') + angleUnitVector_2pt(points[6,0], points[6,1], points[6,2], points[10,0], points[10,1], points[10,2], 'el_zz')) /2
            two_unit_el_ly = (angleUnitVector_2pt(points[13,0], points[13,1], points[13,2], points[14,0], points[14,1], points[14,2], 'el_yy') * (1)) # 13 14

            two_unit_wr_rx = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'wr_z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'wr_z')) /2
            two_unit_wr_ry = (angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'wr_y') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'wr_y')) /2
            two_unit_wr_rz = ((angleUnitVector_2pt(points[7,0], points[7,1], points[7,2], points[11,0], points[11,1], points[11,2], 'wr_z') + angleUnitVector_2pt(points[9,0], points[9,1], points[9,2], points[12,0], points[12,1], points[12,2], 'wr_z')) /2) * (-1)
            two_unit_wr_lx = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'wr_zz') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'wr_zz')) /2 
            two_unit_wr_ly = (angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'wr_yy') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'wr_yy')) /2 
            two_unit_wr_lz = ((angleUnitVector_2pt(points[10,0], points[10,1], points[10,2], points[14,0], points[14,1], points[14,2], 'wr_zz') + angleUnitVector_2pt(points[8,0], points[8,1], points[8,2], points[13,0], points[13,1], points[13,2], 'wr_zz')) /2) * (-1)
            
            df_deg = pd.DataFrame([[round(time,3), two_unit_sh_x, two_unit_sh_xx, two_unit_sh_y, two_unit_sh_z, two_unit_sh_0, two_unit_sh_1, two_unit_sh_a, two_unit_sh_aa, two_unit_sh_b, two_unit_sh_c, two_unit_sh_d, two_unit_sh_e, two_unit_el_rx, two_unit_el_ry, two_unit_el_lx, two_unit_el_ly, two_unit_wr_rx, two_unit_wr_ry, two_unit_wr_rz, two_unit_wr_lx, two_unit_wr_ly, two_unit_wr_lz]], index = [i], columns = ['Time (s)', 'R-FL/EXT (S)', 'R-EXT (S)', 'R-ADD/ABD (S)', 'R-HOR ADD/ABD (S)', 'R-INT/EXT Tran (S)', 'R-INT/EXT Sag (S)', 'L-FL/EXT (S)', 'L-EXT (S)', 'L-ADD/ABD (S)', 'L-HOR ADD/ABD (S)', 'L-INT/EXT Tran (S)', 'L-INT/EXT Sag (S)', 'R-FL/EXT (E)', 'R-PRO/SUP (E)', 'L-FL/EXT (E)', 'L-PRO/SUP (E)', 'R-FL/EXT (W)', 'R-Radial/Ulnar Tran (W)', 'R-Radial/Ulnar Sag (W)', 'L-FL/EXT (W)', 'L-Radial/Ulnar Tran (W)', 'L-Radial/Ulnar Sag (W)'])
            df_degXYZ = df_degXYZ._append(df_deg)
        else:
            print('Hello World')

    if moduleVar.get() == 1 or moduleVar.get() == 2:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['FL/EXT', 'ROT', 'L/R']].agg(['min', 'max'])
    elif moduleVar.get() == 3 or moduleVar.get() == 31 or moduleVar.get() == 32:   
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-DOR/PLA', 'L-DOR/PLA', 'R-EVE/INV', 'L-EVE/INV']].agg(['min', 'max'])
    elif moduleVar.get() == 4:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-EXT', 'R-ADD/ABD', 'R-HOR ADD/ABD', 'R-INT/EXT Tran', 'R-INT/EXT Sag', 'L-FL/EXT', 'L-EXT', 'L-ADD/ABD', 'L-HOR ADD/ABD', 'L-INT/EXT Tran', 'L-INT/EXT Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 5:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-PRO/SUP', 'L-FL/EXT', 'L-PRO/SUP']].agg(['min', 'max'])
    elif moduleVar.get() == 6:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-Radial/Ulnar Tran', 'R-Radial/Ulnar Sag', 'L-FL/EXT', 'L-Radial/Ulnar Tran', 'L-Radial/Ulnar Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 41:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['L-FL/EXT', 'L-EXT', 'L-ADD/ABD', 'L-HOR ADD/ABD', 'L-INT/EXT Tran', 'L-INT/EXT Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 42:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-EXT', 'R-ADD/ABD', 'R-HOR ADD/ABD', 'R-INT/EXT Tran', 'R-INT/EXT Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 51:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['L-FL/EXT', 'L-PRO/SUP']].agg(['min', 'max'])    
    elif moduleVar.get() == 52:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-PRO/SUP']].agg(['min', 'max'])
    elif moduleVar.get() == 61:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['L-FL/EXT', 'L-Radial/Ulnar Tran', 'L-Radial/Ulnar Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 62:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT', 'R-Radial/Ulnar Tran', 'R-Radial/Ulnar Sag']].agg(['min', 'max'])
    elif moduleVar.get() == 7:
        df_valueXYZ = df_degXYZ[df_degXYZ != 0]
        df_value = df_valueXYZ[['R-FL/EXT (S)', 'R-EXT (S)', 'R-ADD/ABD (S)', 'R-HOR ADD/ABD (S)', 'R-INT/EXT Tran (S)', 'R-INT/EXT Sag (S)', 'L-FL/EXT (S)', 'L-EXT (S)', 'L-ADD/ABD (S)', 'L-HOR ADD/ABD (S)', 'L-INT/EXT Tran (S)', 'L-INT/EXT Sag (S)', 'R-FL/EXT (E)', 'R-PRO/SUP (E)', 'L-FL/EXT (E)', 'L-PRO/SUP (E)', 'R-FL/EXT (W)', 'R-Radial/Ulnar Tran (W)', 'R-Radial/Ulnar Sag (W)', 'L-FL/EXT (W)', 'L-Radial/Ulnar Tran (W)', 'L-Radial/Ulnar Sag (W)']].agg(['min', 'max'])
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

        if moduleVar.get() == 1:
            df_degXYZ.to_excel(writer, sheet_name='Neck', index=True)
            df_value.to_excel(writer, sheet_name='Neck', index=True, startcol=6)
            writer.sheets['Neck'].set_column(2, 4, 15)
            writer.sheets['Neck'].set_column(7, 9, 15)
        elif moduleVar.get() == 2:
            df_degXYZ.to_excel(writer, sheet_name='Back', index=True)
            df_value.to_excel(writer, sheet_name='Back', index=True, startcol=6)
            writer.sheets['Back'].set_column(2, 4, 15)
            writer.sheets['Back'].set_column(7, 9, 15)
        elif moduleVar.get() == 3 or moduleVar.get() == 31 or moduleVar.get() == 32:
            df_degXYZ.to_excel(writer, sheet_name='Foot', index=True)
            df_value.to_excel(writer, sheet_name='Foot', index=True, startcol=7)
            writer.sheets['Foot'].set_column(2, 5, 15)
            writer.sheets['Foot'].set_column(8, 11, 15)    
        elif moduleVar.get() == 4:
            df_degXYZ.to_excel(writer, sheet_name='Shoulder', index=True)
            df_value.to_excel(writer, sheet_name='Shoulder', index=True, startcol=15)
            writer.sheets['Shoulder'].set_column(2, 13, 15)
            writer.sheets['Shoulder'].set_column(16, 27, 15)
        elif moduleVar.get() == 5:
            df_degXYZ.to_excel(writer, sheet_name='Elbow', index=True)
            df_value.to_excel(writer, sheet_name='Elbow', index=True, startcol=7)
            writer.sheets['Elbow'].set_column(2, 5, 15)
            writer.sheets['Elbow'].set_column(8, 11, 15)
        elif moduleVar.get() == 6:
            df_degXYZ.to_excel(writer, sheet_name='Wrist', index=True)
            df_value.to_excel(writer, sheet_name='Wrist', index=True, startcol=9)
            writer.sheets['Wrist'].set_column(2, 7, 15)
            writer.sheets['Wrist'].set_column(10, 15, 15)
        elif moduleVar.get() == 41 or moduleVar.get() == 42:
            df_degXYZ.to_excel(writer, sheet_name='Shoulder', index=True)
            df_value.to_excel(writer, sheet_name='Shoulder', index=True, startcol=9)
            writer.sheets['Shoulder'].set_column(2, 7, 15)
            writer.sheets['Shoulder'].set_column(10, 15, 15)
        elif moduleVar.get() == 51 or moduleVar.get() == 52:
            df_degXYZ.to_excel(writer, sheet_name='Elbow', index=True)
            df_value.to_excel(writer, sheet_name='Elbow', index=True, startcol=5)
            writer.sheets['Elbow'].set_column(2, 3, 15)
            writer.sheets['Elbow'].set_column(6, 7, 15)
        elif moduleVar.get() == 61 or moduleVar.get() == 62:
            df_degXYZ.to_excel(writer, sheet_name='Wrist', index=True)
            df_value.to_excel(writer, sheet_name='Wrist', index=True, startcol=6)
            writer.sheets['Wrist'].set_column(2, 4, 15)
            writer.sheets['Wrist'].set_column(7, 9, 15)
        elif moduleVar.get() == 7:
            df_degXYZ[['Time (s)', 'R-FL/EXT (S)', 'R-EXT (S)', 'R-ADD/ABD (S)', 'R-HOR ADD/ABD (S)', 'R-INT/EXT Tran (S)', 'R-INT/EXT Sag (S)', 'L-FL/EXT (S)', 'L-EXT (S)', 'L-ADD/ABD (S)', 'L-HOR ADD/ABD (S)', 'L-INT/EXT Tran (S)', 'L-INT/EXT Sag (S)']].to_excel(writer, sheet_name='Shoulder', index=True)
            df_value[['R-FL/EXT (S)', 'R-EXT (S)', 'R-ADD/ABD (S)', 'R-HOR ADD/ABD (S)', 'R-INT/EXT Tran (S)', 'R-INT/EXT Sag (S)', 'L-FL/EXT (S)', 'L-EXT (S)', 'L-ADD/ABD (S)', 'L-HOR ADD/ABD (S)', 'L-INT/EXT Tran (S)', 'L-INT/EXT Sag (S)']].to_excel(writer, sheet_name='Shoulder', index=True, startcol=15)
            writer.sheets['Shoulder'].set_column(2, 13, 18)
            writer.sheets['Shoulder'].set_column(16, 27, 18)

            df_degXYZ[['Time (s)', 'R-FL/EXT (E)', 'R-PRO/SUP (E)', 'L-FL/EXT (E)', 'L-PRO/SUP (E)']].to_excel(writer, sheet_name='Elbow', index=True)
            df_value[['R-FL/EXT (E)', 'R-PRO/SUP (E)', 'L-FL/EXT (E)', 'L-PRO/SUP (E)']].to_excel(writer, sheet_name='Elbow', index=True, startcol=7)
            writer.sheets['Elbow'].set_column(2, 5, 18)
            writer.sheets['Elbow'].set_column(8, 11, 18)

            df_degXYZ[['Time (s)', 'R-FL/EXT (W)', 'R-Radial/Ulnar Tran (W)', 'R-Radial/Ulnar Sag (W)', 'L-FL/EXT (W)', 'L-Radial/Ulnar Tran (W)', 'L-Radial/Ulnar Sag (W)']].to_excel(writer, sheet_name='Wrist', index=True)
            df_value[['R-FL/EXT (W)', 'R-Radial/Ulnar Tran (W)', 'R-Radial/Ulnar Sag (W)', 'L-FL/EXT (W)', 'L-Radial/Ulnar Tran (W)', 'L-Radial/Ulnar Sag (W)']].to_excel(writer, sheet_name='Wrist', index=True, startcol=9)
            writer.sheets['Wrist'].set_column(2, 7, 23)
            writer.sheets['Wrist'].set_column(10, 15, 23)
        else:
            print('Hello World')

        if moduleVar.get() == 1:
            workbook  = writer.book
            worksheet = writer.sheets['Neck']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Neck', 1, 1, maxRow, 1], 'values': ['Neck', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Neck', 1, 1, maxRow, 1], 'values': ['Neck', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Rotation (Left/Right)', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Neck', 1, 1, maxRow, 1], 'values': ['Neck', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left/Right Lateral Bending', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('K5', chart_z)
        elif moduleVar.get() == 2:
            workbook  = writer.book
            worksheet = writer.sheets['Back']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Back', 1, 1, maxRow, 1], 'values': ['Back', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Back', 1, 1, maxRow, 1], 'values': ['Back', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Rotation (Left/Right)', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Back', 1, 1, maxRow, 1], 'values': ['Back', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left/Right Lateral Bending', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('K5', chart_z)
        elif moduleVar.get() == 3:    
            workbook  = writer.book
            worksheet = writer.sheets['Foot']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Dorsiflexion/Plantar Flexion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Left Dorsiflexion/Plantar Flexion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('L5', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Eversion/Inversion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H17', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Eversion/Inversion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('L17', chart_a)
        elif moduleVar.get() == 4:
            workbook  = writer.book
            worksheet = writer.sheets['Shoulder']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P27', chart_z)

            chart_0 = workbook.add_chart({'type': 'line'})
            chart_0.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_0.set_title({'name': 'Right Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_0.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_0.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_0.set_legend({'position': 'none'})
            chart_0.set_size({'width': 360, 'height': 216})
            chart_0.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P38', chart_0)

            chart_1 = workbook.add_chart({'type': 'line'})
            chart_1.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_1.set_title({'name': 'Right Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_1.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_1.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_1.set_legend({'position': 'none'})
            chart_1.set_size({'width': 360, 'height': 216})
            chart_1.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P49', chart_1)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 8, maxRow, 8], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T5', chart_a)
           
            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 10, maxRow, 10], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T16', chart_b)

            chart_c = workbook.add_chart({'type': 'line'})
            chart_c.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 11, maxRow, 11], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_c.set_title({'name': 'Left Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_c.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_c.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_c.set_legend({'position': 'none'})
            chart_c.set_size({'width': 360, 'height': 216})
            chart_c.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T27', chart_c)

            chart_d = workbook.add_chart({'type': 'line'})
            chart_d.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 12, maxRow, 12], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_d.set_title({'name': 'Left Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_d.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_d.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_d.set_legend({'position': 'none'})
            chart_d.set_size({'width': 360, 'height': 216})
            chart_d.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T38', chart_d)

            chart_e = workbook.add_chart({'type': 'line'})
            chart_e.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 13, maxRow, 13], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_e.set_title({'name': 'Left Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_e.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_e.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_e.set_legend({'position': 'none'})
            chart_e.set_size({'width': 360, 'height': 216})
            chart_e.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T49', chart_e)
        elif moduleVar.get() == 5:
            workbook  = writer.book
            worksheet = writer.sheets['Elbow']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('L5', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('L16', chart_a)
        elif moduleVar.get() == 6:
            workbook  = writer.book
            worksheet = writer.sheets['Wrist']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J27', chart_z)

            chart_zz = workbook.add_chart({'type': 'line'})
            chart_zz.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_zz.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_zz.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_zz.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_zz.set_legend({'position': 'none'})
            chart_zz.set_size({'width': 360, 'height': 216})
            chart_zz.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N5', chart_zz)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N16', chart_a)

            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N27', chart_b)
        elif moduleVar.get() == 31:
            workbook  = writer.book
            worksheet = writer.sheets['Foot']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Left Dorsiflexion/Plantar Flexion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_y)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Eversion/Inversion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H17', chart_a)
        elif moduleVar.get() == 32:
            workbook  = writer.book
            worksheet = writer.sheets['Foot']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Dorsiflexion/Plantar Flexion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_x)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Foot', 1, 1, maxRow, 1], 'values': ['Foot', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Eversion/Inversion', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H17', chart_z)
        elif moduleVar.get() == 41:
            workbook  = writer.book
            worksheet = writer.sheets['Shoulder']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J5', chart_a)
           
            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J16', chart_b)

            chart_c = workbook.add_chart({'type': 'line'})
            chart_c.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_c.set_title({'name': 'Left Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_c.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_c.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_c.set_legend({'position': 'none'})
            chart_c.set_size({'width': 360, 'height': 216})
            chart_c.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N16', chart_c)

            chart_d = workbook.add_chart({'type': 'line'})
            chart_d.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_d.set_title({'name': 'Left Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_d.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_d.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_d.set_legend({'position': 'none'})
            chart_d.set_size({'width': 360, 'height': 216})
            chart_d.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J27', chart_d)

            chart_e = workbook.add_chart({'type': 'line'})
            chart_e.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_e.set_title({'name': 'Left Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_e.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_e.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_e.set_legend({'position': 'none'})
            chart_e.set_size({'width': 360, 'height': 216})
            chart_e.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N27', chart_e)
        elif moduleVar.get() == 42:
            workbook  = writer.book
            worksheet = writer.sheets['Shoulder']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N16', chart_z)

            chart_0 = workbook.add_chart({'type': 'line'})
            chart_0.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_0.set_title({'name': 'Right Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_0.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_0.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_0.set_legend({'position': 'none'})
            chart_0.set_size({'width': 360, 'height': 216})
            chart_0.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J27', chart_0)

            chart_1 = workbook.add_chart({'type': 'line'})
            chart_1.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_1.set_title({'name': 'Right Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_1.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_1.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_1.set_legend({'position': 'none'})
            chart_1.set_size({'width': 360, 'height': 216})
            chart_1.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N27', chart_1)
        elif moduleVar.get() == 51:
            workbook  = writer.book
            worksheet = writer.sheets['Elbow']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('F5', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('F16', chart_a)
        elif moduleVar.get() == 52:
            workbook  = writer.book
            worksheet = writer.sheets['Elbow']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('F5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('F16', chart_y)
        elif moduleVar.get() == 61:
            workbook  = writer.book
            worksheet = writer.sheets['Wrist']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G5', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G16', chart_a)

            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G27', chart_b)
        elif moduleVar.get() == 62:
            workbook  = writer.book
            worksheet = writer.sheets['Wrist']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('G27', chart_z)
        elif moduleVar.get() == 7:
            workbook  = writer.book
            worksheet = writer.sheets['Shoulder']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P27', chart_z)

            chart_0 = workbook.add_chart({'type': 'line'})
            chart_0.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_0.set_title({'name': 'Right Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_0.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_0.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_0.set_legend({'position': 'none'})
            chart_0.set_size({'width': 360, 'height': 216})
            chart_0.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P38', chart_0)

            chart_1 = workbook.add_chart({'type': 'line'})
            chart_1.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_1.set_title({'name': 'Right Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_1.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_1.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_1.set_legend({'position': 'none'})
            chart_1.set_size({'width': 360, 'height': 216})
            chart_1.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('P49', chart_1)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 8, maxRow, 8], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T5', chart_a)
           
            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 10, maxRow, 10], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T16', chart_b)

            chart_c = workbook.add_chart({'type': 'line'})
            chart_c.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 11, maxRow, 11], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_c.set_title({'name': 'Left Horizontal Adduction/Abduction', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_c.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_c.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_c.set_legend({'position': 'none'})
            chart_c.set_size({'width': 360, 'height': 216})
            chart_c.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T27', chart_c)

            chart_d = workbook.add_chart({'type': 'line'})
            chart_d.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 12, maxRow, 12], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_d.set_title({'name': 'Left Internal/External Rotation Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_d.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_d.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_d.set_legend({'position': 'none'})
            chart_d.set_size({'width': 360, 'height': 216})
            chart_d.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T38', chart_d)

            chart_e = workbook.add_chart({'type': 'line'})
            chart_e.add_series({'categories': ['Shoulder', 1, 1, maxRow, 1], 'values': ['Shoulder', 1, 13, maxRow, 13], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_e.set_title({'name': 'Left Internal/External Rotation Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_e.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_e.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_e.set_legend({'position': 'none'})
            chart_e.set_size({'width': 360, 'height': 216})
            chart_e.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('T49', chart_e)

            workbook  = writer.book
            worksheet = writer.sheets['Elbow']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('H16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('L5', chart_z)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Elbow', 1, 1, maxRow, 1], 'values': ['Elbow', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Pronate/Supinate', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('L16', chart_a)

            workbook  = writer.book
            worksheet = writer.sheets['Wrist']
            (maxRow, maxCol) = df_degXYZ.shape

            chart_x = workbook.add_chart({'type': 'line'})
            chart_x.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 2, maxRow, 2], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_x.set_title({'name': 'Right Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_x.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_x.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_x.set_legend({'position': 'none'})
            chart_x.set_size({'width': 360, 'height': 216})
            chart_x.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J5', chart_x)

            chart_y = workbook.add_chart({'type': 'line'})
            chart_y.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 3, maxRow, 3], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_y.set_title({'name': 'Right Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_y.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_y.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_y.set_legend({'position': 'none'})
            chart_y.set_size({'width': 360, 'height': 216})
            chart_y.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J16', chart_y)

            chart_z = workbook.add_chart({'type': 'line'})
            chart_z.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 4, maxRow, 4], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_z.set_title({'name': 'Right Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_z.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_z.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_z.set_legend({'position': 'none'})
            chart_z.set_size({'width': 360, 'height': 216})
            chart_z.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('J27', chart_z)

            chart_zz = workbook.add_chart({'type': 'line'})
            chart_zz.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 5, maxRow, 5], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_zz.set_title({'name': 'Left Flexion/Extension', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_zz.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_zz.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_zz.set_legend({'position': 'none'})
            chart_zz.set_size({'width': 360, 'height': 216})
            chart_zz.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N5', chart_zz)

            chart_a = workbook.add_chart({'type': 'line'})
            chart_a.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 6, maxRow, 6], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_a.set_title({'name': 'Left Radial/Ulnar Tran', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_a.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_a.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_a.set_legend({'position': 'none'})
            chart_a.set_size({'width': 360, 'height': 216})
            chart_a.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N16', chart_a)

            chart_b = workbook.add_chart({'type': 'line'})
            chart_b.add_series({'categories': ['Wrist', 1, 1, maxRow, 1], 'values': ['Wrist', 1, 7, maxRow, 7], 'line': {'color': '#0000FF', 'width': 1.2}})
            chart_b.set_title({'name': 'Left Radial/Ulnar Sag', 'name_font': {'name': 'Time New Roman', 'bold': True, 'size': 14, 'color': 'black'}})
            chart_b.set_x_axis({'name': 'Motion Points (Samples)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'interval_unit': 120, 'label_position': 'low', 'line': {'none': True}})
            chart_b.set_y_axis({'name': 'Angles in Degree (°)', 'name_font': {'name': 'Time New Roman', 'bold': False, 'size': 10, 'color': 'black'}, 'major_gridlines': {'visible': False}})
            chart_b.set_legend({'position': 'none'})
            chart_b.set_size({'width': 360, 'height': 216})
            chart_b.set_plotarea({'layout': {'x': 0.13, 'y': 0.1, 'width': 0.82, 'height': 0.7}})
            worksheet.insert_chart('N27', chart_b)
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
    module_7.config(state=NORMAL)

    module_31.config(state=NORMAL)
    module_41.config(state=NORMAL)
    module_51.config(state=NORMAL)
    module_61.config(state=NORMAL)
    module_32.config(state=NORMAL)
    module_42.config(state=NORMAL)
    module_52.config(state=NORMAL)
    module_62.config(state=NORMAL)

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
    module_7.config(state=DISABLED)

    module_31.config(state=DISABLED)
    module_41.config(state=DISABLED)
    module_51.config(state=DISABLED)
    module_61.config(state=DISABLED)
    module_32.config(state=DISABLED)
    module_42.config(state=DISABLED)
    module_52.config(state=DISABLED)
    module_62.config(state=DISABLED)

    print('clear')
    statusString.set("Completed Clear")

def checkModule():
    if moduleVar.get() == 1:
        print('neck')
    elif moduleVar.get() == 2:
        print("back")
    elif moduleVar.get() == 3:
        print('foot')
    elif moduleVar.get() == 4:
        print("shoulder")
    elif moduleVar.get() == 5:
        print('elbow')
    elif moduleVar.get() == 6:
        print("wrist")
    elif moduleVar.get() == 31:
        print('left foot')
    elif moduleVar.get() == 41:
        print("left shoulder")
    elif moduleVar.get() == 51:
        print('left elbow')
    elif moduleVar.get() == 61:
        print("left wrist")
    elif moduleVar.get() == 32:
        print('right foot')
    elif moduleVar.get() == 42:
        print("right shoulder")
    elif moduleVar.get() == 52:
        print('right elbow')
    elif moduleVar.get() == 62:
        print("right wrist")
    elif moduleVar.get() == 7:
        print("upper limb")
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
textFrame.pack(side=BOTTOM, pady=10, anchor=SE,padx=5, ipady=53, ipadx=59)
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
module_1 = tk.Radiobutton(frameLeft, text='Neck      ', state=DISABLED, variable=moduleVar, value=1, bg='white')
module_1.grid(in_=commandFrame, column=0, row=1, pady=2)
module_2 = tk.Radiobutton(frameLeft, text='Back               ', state=DISABLED, variable=moduleVar, value=2, bg='white')
module_2.grid(in_=commandFrame, column=2, row=1, pady=2)
module_7 = tk.Radiobutton(frameLeft, text='Upper Limb      ', state=DISABLED, variable=moduleVar, value=7, bg='white')
module_7.grid(in_=commandFrame, column=4, row=1, pady=2)
module_3 = tk.Radiobutton(frameLeft, text='Foot       ', state=DISABLED, variable=moduleVar, value=3, bg='white')
module_3.grid(in_=commandFrame, column=0, row=2, pady=2)
module_31 = tk.Radiobutton(frameLeft, text='Left Foot        ', state=DISABLED, variable=moduleVar, value=31, bg='white')
module_31.grid(in_=commandFrame, column=2, row=2, pady=2)
module_32 = tk.Radiobutton(frameLeft, text='Right Foot        ', state=DISABLED, variable=moduleVar, value=32, bg='white')
module_32.grid(in_=commandFrame, column=4, row=2, pady=2)
module_4 = tk.Radiobutton(frameLeft, text='Shoulder', state=DISABLED, variable=moduleVar, value=4, bg='white')
module_4.grid(in_=commandFrame, column=0, row=3, pady=2)
module_41 = tk.Radiobutton(frameLeft, text='Left Shoulder', state=DISABLED, variable=moduleVar, value=41, bg='white')
module_41.grid(in_=commandFrame, column=2, row=3, pady=2)
module_42 = tk.Radiobutton(frameLeft, text='Right Shoulder', state=DISABLED, variable=moduleVar, value=42, bg='white')
module_42.grid(in_=commandFrame, column=4, row=3, pady=2)
module_5 = tk.Radiobutton(frameLeft, text='Elbow     ', state=DISABLED, variable=moduleVar, value=5, bg='white')
module_5.grid(in_=commandFrame, column=0, row=4, pady=2)
module_51 = tk.Radiobutton(frameLeft, text='Left Elbow     ', state=DISABLED, variable=moduleVar, value=51, bg='white')
module_51.grid(in_=commandFrame, column=2, row=4, pady=2)
module_52 = tk.Radiobutton(frameLeft, text='Right Elbow     ', state=DISABLED, variable=moduleVar, value=52, bg='white')
module_52.grid(in_=commandFrame, column=4, row=4, pady=2)
module_6 = tk.Radiobutton(frameLeft, text='Wrist       ', state=DISABLED, variable=moduleVar, value=6, bg='white')
module_6.grid(in_=commandFrame, column=0, row=5, pady=2)
module_61 = tk.Radiobutton(frameLeft, text='Left Wrist       ', state=DISABLED, variable=moduleVar, value=61, bg='white')
module_61.grid(in_=commandFrame, column=2, row=5, pady=2)
module_62 = tk.Radiobutton(frameLeft, text='Right Wrist       ', state=DISABLED, variable=moduleVar, value=62, bg='white')
module_62.grid(in_=commandFrame, column=4, row=5, pady=2)
moduleVar.set(NONE)

#button
runBTN = tk.Button(commandFrame, text='Run Module', state=DISABLED, height=1, width=20, relief="ridge", command=runFile)
runBTN.grid(columnspan=2, row=6, column=0, padx=3, pady=5)
saveBTN = tk.Button(commandFrame, text='Save File', state=DISABLED, height=1, width=20, relief="ridge", command=savefile)
saveBTN.grid(columnspan=2, row=6, column=3, padx=3, pady=5)

#left label
statusString = tk.StringVar()
statusString.set("Hello User")
status_label = tk.Label(textFrame, textvariable=statusString, fg='black', bg='white')
status_label.place(in_=textFrame, x=95, y=95, anchor=CENTER)

screen.mainloop()