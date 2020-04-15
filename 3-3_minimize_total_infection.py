import matplotlib.pyplot as plt
import numpy as np
import math

beta = 0.18
alfa = 0.24
gamma = 0.16

population = 126180643

init = 1 / population
t = 400
dist = 30
emg = [0 for _ in range(t - dist)]

min_n = float('inf')
min_c = 0
for k in range(t - dist):
  i = np.array([init] + [0] * (t - 1), dtype = 'float128')
  e = np.array([init] + [0] * (t - 1), dtype = 'float128')
  r = np.array([0] + [0] * (t - 1), dtype = 'float128')
  s = np.array([1 - r[0] - i[0]] + [0] * (t - 1), dtype = 'float128')

  for j in range(t - 1):
    beta_t = beta
    if k <= j and j < k + dist:
      beta_t = beta / 2
    s[j + 1] = s[j] - beta_t * s[j] * (i[j] + e[j])
    e[j + 1] = e[j] + beta_t * s[j] * (i[j] + e[j]) - alfa * e[j]
    i[j + 1] = i[j] + alfa * e[j] - gamma * i[j]
    r[j + 1] = r[j] + gamma * i[j]

  if min_n > r[-1]:
    min_n = r[-1]
    min_c = k
  emg[k] = r[-1]
print(min_n * 100)
print(min_c)
plt.plot(emg)
plt.savefig("3-3_minimize_total_infection.png")

