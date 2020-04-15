import matplotlib.pyplot as plt
import numpy as np
import math

# 日本の感染者データ（2020/01/22~）
jp_confirm = np.array([2,2,2,2,4,4,7,7,11,15,20,20,20,22,22,22,25,25,26,26,26,28,28,29,43,59,66,74,84,94,105,122,147,159,170,189,214,228,241,256,274,293,331,360,420,461,502,511,581,639,639,701,773,839,839,878,889,924,963,1007,1101,1128,1193,1307,1387,1468,1693,1866,1866,1953,2178,2495,2617,3139,3139,3654,3906,4257,4667,5530,6005,6748,7370])
jp_death = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,4,4,5,6,6,6,6,6,6,6,6,10,10,15,16,19,22,22,27,29,29,29,33,35,41,42,43,45,47,49,52,54,54,56,57,62,63,77,77,85,92,93,94,99,99,108,123])
jp_recoverd = np.array([0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,9,9,9,9,12,12,12,13,18,18,22,22,22,22,22,22,22,22,32,32,32,43,43,43,46,76,76,76,101,118,118,118,118,118,144,144,144,150,191,232,235,235,285,310,359,372,404,424,424,424,472,472,514,514,514,575,592,622,632,685,762,762,784])
jp_confirm = (jp_confirm - jp_death - jp_recoverd) / 126180643
t = len(jp_confirm)

(ba, bb, bc) = (0, 1, 0.01)
(aa, ab, ac) = (0, 1, 0.01)
(ga, gb, gc) = (0, 1, 0.01)
beta = np.arange(ba, bb, bc)
alfa = np.arange(aa, ab, ac)
gamma = np.arange(ga, gb, gc)

min_n = float('inf')
min_c = '0,0,0'
for b in range(len(beta)):
  for a in range(len(alfa)):
    for g in range(len(gamma)):
      i = np.array([jp_confirm[0]] + [0] * (t - 1), dtype = 'float128')
      e = np.array([jp_confirm[0]] + [0] * (t - 1), dtype = 'float128')
      r = np.array([0] + [0] * (t - 1), dtype = 'float128')
      s = np.array([1 - r[0] - i[0]] + [0] * (t - 1), dtype = 'float128')
      
      for j in range(t - 1):
        s[j + 1] = s[j] - beta[b] * s[j] * (i[j] + e[j])
        e[j + 1] = e[j] + beta[b] * s[j] * (i[j] + e[j]) - alfa[a] * e[j]
        i[j + 1] = i[j] + alfa[a] * e[j] - gamma[g] * i[j]
        r[j + 1] = r[j] + gamma[g] * i[j]
      
      estimate = math.sqrt(np.sum((i - jp_confirm) ** 2))
      if min_n > estimate:
        min_n = estimate
        min_c = str(b) + ',' + str(a) + ',' + str(g)

(minb, mina, ming) = map(int, min_c.split(','))

print('β=' + str(ba + minb * bc))
print('α=' + str(aa + mina * ac))
print('γ=' + str(ga + ming * gc))
