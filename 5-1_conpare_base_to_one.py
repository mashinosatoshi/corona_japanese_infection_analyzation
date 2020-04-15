import matplotlib.pyplot as plt
import numpy as np
import math

beta = 0.18
alfa = 0.24
gamma = 0.16

population = 126180643

init = 1 / population
t = 400

i = np.array([init] + [0] * (t - 1), dtype = 'float128')
e = np.array([init] + [0] * (t - 1), dtype = 'float128')
r = np.array([0] + [0] * (t - 1), dtype = 'float128')
s = np.array([1 - r[0] - i[0]] + [0] * (t - 1), dtype = 'float128')

for j in range(t - 1):
  s[j + 1] = s[j] - beta * s[j] * (i[j] + e[j])
  e[j + 1] = e[j] + beta * s[j] * (i[j] + e[j]) - alfa * e[j]
  i[j + 1] = i[j] + alfa * e[j] - gamma * i[j]
  r[j + 1] = r[j] + gamma * i[j]

plt.plot(r) 

i = np.array([init] + [0] * (t - 1), dtype = 'float128')
e = np.array([init] + [0] * (t - 1), dtype = 'float128')
r = np.array([0] + [0] * (t - 1), dtype = 'float128')
s = np.array([1 - r[0] - i[0]] + [0] * (t - 1), dtype = 'float128')

k = 76

for j in range(t - 1):
  beta_t = beta
  if k <= j and j < k + 30:
    beta_t = beta / 2
  s[j + 1] = s[j] - beta_t * s[j] * (i[j] + e[j])
  e[j + 1] = e[j] + beta_t * s[j] * (i[j] + e[j]) - alfa * e[j]
  i[j + 1] = i[j] + alfa * e[j] - gamma * i[j]
  r[j + 1] = r[j] + gamma * i[j]

plt.plot(r) 
plt.savefig("5-1_conpare_base_to_one.png")
