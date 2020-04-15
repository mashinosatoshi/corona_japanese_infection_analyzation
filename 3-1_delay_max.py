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

max_delay = 0
delay_k = 0
for k in range(t - dist):
  i = np.array([init] + [0] * (t - 1), dtype = 'float128')
  e = np.array([init] + [0] * (t - 1), dtype = 'float128')
  r = np.array([0] + [0] * (t - 1), dtype = 'float128')
  s = np.array([1 - r[0] - i[0]] + [0] * (t - 1), dtype = 'float128')

  tmp_max = 0
  max_t = 0
  for j in range(t - 1):
    beta_t = beta
    if k <= j and j < k + dist:
      beta_t = beta / 2
    s[j + 1] = s[j] - beta_t * s[j] * (i[j] + e[j])
    e[j + 1] = e[j] + beta_t * s[j] * (i[j] + e[j]) - alfa * e[j]
    i[j + 1] = i[j] + alfa * e[j] - gamma * i[j]
    r[j + 1] = r[j] + gamma * i[j]

    if tmp_max < i[j + 1]:
      tmp_max = i[j + 1]
      max_t = j # 感染者数がピークの時点
  
  if max_delay < max_t:
    max_delay = max_t
    delay_k = k
  emg[k] = max_t
print(delay_k)
plt.plot(emg)
plt.savefig("3-1_delay_max.png")

