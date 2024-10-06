# AUMSHREE P. SHAH
# 20231059

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# variables 
cheetas = 10
deers = 30

inic = [deers, cheetas]
required_point = [18, 15]
r1 = 1.05
C = 0.1
d2 = 0.6
g = 0.45

gridd = 15
length = 32

# x axis prey N (deer) and y axis predator P (cheetah)
def diffeq2(t, U):
    the_N, the_P = U
    changeinN = r1*the_N-C*the_N*the_P #N
    changeinP = -d2*the_P+g*C*the_N*the_P #P
    print(changeinN, changeinP)
    return [changeinN, changeinP]

# plot a 50 by 50
N, P = np.meshgrid(np.linspace(0, length, gridd), np.linspace(0, length, gridd)) 
dNdt = r1*N-C*N*P #N
dPdt = -d2*P+g*C*N*P #P
norm = np.sqrt(np.square(dNdt)+np.square(dPdt))
dNdt_normed = 40*dNdt/norm #dividing it by norm
dPdt_normed = 40*dPdt/norm
plt.plot(15, 18, "-o", color='r', label='target population')

plt.quiver(N, P, dNdt_normed, dPdt_normed, np.log(norm))
plt.title('')
plt.xlim(-1, length+1)
plt.ylim(-1, length+1)      
plt.grid()

#plotting           
t_span = (0, 30)
t_eval = np.linspace(0, 30, 10000) 

result = solve_ivp(diffeq2, t_span, inic, t_eval=t_eval, method='DOP853') # normal method doesnt work idk why
plt.plot(result.y[0], result.y[1], color='b', label='Population trajectory')

plt.xlabel('N')
plt.ylabel('P')
plt.title('Population as a growth of time in continous model    ')
plt.legend()
# save it as q4a.png
plt.show()


"""
THE ABOVE CODE WAS FOR ANSWER A OF QUESTION 4 SOLVED USING CONTINIOUS DYNAMICS THE BELOW CODE IS FOR DISCREATE CASE
WHICH I FEEL LIKE IS MORE LIKELY BUT I AM UNABLE TO CODE IT THE WAY I WANT TO DUE TO TIME CONSTRAINTS AND I ALSO CANNOT FIND 
A PROPER DOCUMENTATION FOR THE FUNCTIONS I WANT .-.
HERE IS THE CODE WHICH STILL NEEDS IMPROVMENT, ILL UPDATE IT ON GITHUB WHEN I AM DONE WITH IT: 
"""
# vars
r1 = 1.05
C = 0.1
d2 = 0.6
g = 0.45
N = 30
P = 10
target_N = 18
target_P = 15


def dN_dt(N, P):
    return r1 * N - C * N * P

def dP_dt(N, P):
    return -d2 * P + g * C * N * P

# Simulate the system
N_values = [N]
P_values = [P]
steps = 0
max_steps = 100

while True and steps != max_steps:  
    dN = dN_dt(N, P)
    dP = dP_dt(N, P)

    if abs(dN) > abs(dP):
        N += np.sign(dN) 
    else:
        P += np.sign(dP)  
    steps += 1
    N_values.append(N)
    P_values.append(P)

    if (N == target_N and P == target_P) or steps == max_steps:
        print(f"Reached target point (18, 15) or max steps in {steps} steps.")
        break

print(f"Final populations: N = {N}, P = {P}")

plt.figure(figsize=(10, 6))
plt.plot(N_values, P_values, color='b', marker='o', label='Population trajectory')
plt.xlabel('Prey Population (N)')
plt.ylabel('Predator Population (P)')
plt.title('Phase Space of Predator-Prey Dynamics')

# creating mesh
N_mesh, P_mesh = np.meshgrid(np.linspace(0, length, gridd), np.linspace(0, length, gridd)) 

dNdt = r1*N_mesh - C*N_mesh*P_mesh
dPdt = -d2*P_mesh + g*C*N_mesh*P_mesh


#nom agagin
norm = np.sqrt(np.square(dNdt) + np.square(dPdt))
dNdt_normed = 40 * dNdt / norm
dPdt_normed = 40 * dPdt / norm
plt.quiver(N_mesh, P_mesh, dNdt_normed, dPdt_normed, np.log(norm))
plt.xlim(-1, length+1)
plt.ylim(-1, length+1)  
plt.legend()
plt.grid(True)
plt.show()
exit()
