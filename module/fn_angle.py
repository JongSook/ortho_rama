import numpy as np
import numpy.linalg as LA
import math

#########################
##### function part #####
#########################
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