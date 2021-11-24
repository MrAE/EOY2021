from PIL import Image
import numpy as np
import cmath

colors = {
        'None': [0,0,0],  # 
        '0': [84,12,52],  # ( 1.042+0.823j)
        '1': [48,116,58], # ( 1.042-0.823j)
        '2': [155,126,59],# (-0.475+1.13j)
        '3': [255,0,0],   # (-0.475-1.13j)
        '4': [8,29,21],   # (-1.133+0j)
        '5': [84,12,52],  # 
        '6': [48,116,58], #
        '7': [155,126,59],#
        '8': [155,126,59]#
        }


coeff_f1 = [1,0,0,0,1,3]
coeff_f2 = [4,0,0,1,81]

roots_f1 = list(np.roots(coeff_f1))
roots_f2 = list(np.roots(coeff_f2))



def f1(x):
    return(x**5 + x + 3)


def f1p(x):
    return(5*x**4 + 1)


def newton(f,fp, x0, iterations = 100, tolerance = 1e-5):

    i = 0
    x = x0

    #print(f'itn\t x\t f(x)')
    #print(f'---\t -----\t ----')
    while(i < iterations):
        xp = x
        x = x - (f(x) / fp(x))
        i += 1
        #print(f'{i}\t {x}\t {f(x)}')
        if abs(xp - x) < tolerance:
            break
            

    if i >= iterations:
        #print("No root found")
        return(None)
    else:
        #print(f'iterations: {i}\tx*: {round(x.real, 8)} {round(x.imag,8)*1j}')
        return(x)

    
def main(eps = 0.01, f = f1, fp = f1p, tol = 1e-4):
    print('running\n\n')

    #eps = 0.005
    x = np.arange(-2, 2.0 +eps, eps)
    y = np.flip(np.arange(-2, 2.0 + eps, eps)) * 1j

    print(f'x:{len(x)}\ty:{len(y)}\t\t x * y {len(x)*len(y)}')

    xx, yy = np.meshgrid(x,y, sparse = True)
    zz = np.zeros([yy.shape[0], xx.shape[1], 3], dtype = 'uint8')

    for i in range(xx.shape[1]):
        for j in range(yy.shape[0]):
            xstar = newton(f, fp, (xx[0][i] + yy[j][0]), tolerance=tol)
            if xstar is not None:
                col = [str(i) for i in range(len(roots_f1))\
                        if cmath.isclose(xstar, roots_f1[i], rel_tol=tol)]

                if len(col) > 0:
                    zz[j][i] = colors[col[0]]
                else:
                    zz[j][i] = colors['None']

    return(zz)



if __name__ == '__main__':
    zz = main(0.0005, f1, f1p, tol = 1e-2)
    im = Image.fromarray(zz)
    im.save("Newton_fractal_x5_x_3.png")


    


