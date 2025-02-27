import numpy as np

np.random.seed(123)

final_tails=[]
for x in range (100):
  tails=[0]
  for x in range(10):
    coin = random.randint(0,2)
    tails.append(tails[x] + coin)
  final_tails.append(tails[-1])
print(final_tails)
