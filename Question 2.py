## AUMSHREE P. SHAH
## 20231059

import matplotlib.pyplot as plt 
import numpy as np
from scipy.integrate import solve_ivp               

# variables
r1 = 1  
k1 = 200
a12 = 0.8 
r2 = 0.5
k2 = 300 
a21 = 2

griddd = 300        
mesh = 31

# creatting the basic isolines plots: 
N1, N2 = np.meshgrid(np.linspace(0, griddd, mesh), np.linspace(0, griddd, mesh)) 
dN1dt = r1*N1*(k1-N1-a12*N2)/k1
dN2dt = r2*N2*(k2-N2-a21*N1)/k2
norm = np.sqrt(np.square(dN1dt)+np.square(dN2dt))
dN1dt_normed = 40*dN1dt/norm #dividing it by norm
dN2dt_normed = 40*dN2dt/norm

# plotting isocline for image 1
plt.plot([0, k1], [k1/a12, 0], label=r'isocline for $N_1$', linestyle='--', color='r')
plt.plot([0, k2/a21], [k2, 0], label=r'isocline for $N_2$', linestyle='--', color='black')
plt.title('Isocline and vector feild for the given parameter values', fontsize = 20)
plt.xlim(-5, k1)
plt.ylim(-5, k2)
plt.grid()
plt.xlabel(r'$N_1$', fontsize = 18)
plt.ylabel(r'$N_2$', fontsize = 18)
# adding feild
plt.quiver(N1, N2, dN1dt_normed, dN2dt_normed, np.log(norm))
plt.legend()
plt.show()
#save as q2a.png    
#plotting           


def diffeq1(t, U):
    the_X, the_Y = U
    changeinX = r1*the_X*(k1-the_X-a12*the_Y)/k1
    changeinY = r2*the_Y*(k2-the_Y-a21*the_X)/k2
    return (changeinX, changeinY)

# plotting all in 2 by 2 grid
griddd = 300        
mesh = 21

figure, axes = plt.subplots(2, 2)
PLOTS = [[[70, 175], [0, 0], r'Case 1: $N_1=70, N_2=175$'],
[[70, 75], [0, 1], r'Case 2: $N_1=70, N_2=75$'],
[[30, 120], [1, 0], r'Case 3: $N_1=30, N_2=120$'],
[[30, 100], [1, 1], r'Case 4: $N_1=30, N_2=100$']
]
for _ in PLOTS: 
    lis = _[0]
    id = _[1]
    title = _[-1]


    axes[id[0], id[1]].plot([0, k1], [k1/a12, 0], label=r'isoline for $N_1$', linestyle='--', color='r')
    axes[id[0], id[1]].plot([0, k2/a21], [k2, 0], label=r'isoline for $N_2$', linestyle='--', color='black')
    #plotting vector feild
    axes[id[0], id[1]].quiver(N1, N2, dN1dt_normed, dN2dt_normed, np.log(norm))
    axes[id[0], id[1]].set_title(title)
    axes[id[0], id[1]].set_xlim(-5, 200)
    axes[id[0], id[1]].set_ylim(-5, 300)
    axes[id[0], id[1]].grid()
    axes[id[0], id[1]].set_xlabel(r'$N_1$')
    axes[id[0], id[1]].set_ylabel(r'$N_2$')             
    t_span = (0, 100)       
    t_eval = np.linspace(0, 100, 100000)
    result = solve_ivp(diffeq1, t_span, lis, t_eval=t_eval)
    axes[id[0], id[1]].plot(result.y[0], result.y[1], color='b') # trajectory
    axes[id[0], id[1]].plot(lis[0], lis[1], "-o", color='b', label='initial population and trajectory')

plt.legend()
plt.show()
# save as q2b.png




