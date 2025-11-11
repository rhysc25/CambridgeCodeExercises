import control as ctr 
import numpy as np 
import matplotlib.pyplot as plt

G1 = ctr.tf([22000],[1,22000])
# Creates transfer function G1 when you pass in the numerator and denominator coefficients

#mag, phase, omega = ctr.bode(G1, plot=False)
fig3 = plt.figure()
plt.plot(ctr.bode(G1, plot=True))
plt.grid()
#plt.show()

# Create a second transfer function
G2 = ctr.tf([22000,0],np.convolve([1,300],[1,22000])) 
#mag, phase, omega = ctr.bode(G2)
fig4 = plt.figure()
plt.plot(ctr.bode(G2,plot=True))
plt.grid()
plt.show()

#print(mag, phase, omega)