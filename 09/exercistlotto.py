
from random import random
lottos = []
for i in range(10):
    lotto = set()
    while(len(lotto) < 6):
        lotto.add(int(random()*45) + 1)
    lottos.append(lotto)
print(lottos)