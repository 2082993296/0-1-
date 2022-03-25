import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

m, n = map(int, input().split())
weight = []
value = []
for i in range(1, n+1):
    x, y = map(int, input().split())
    weight.append(x)
    value.append(y)
plt.scatter(weight, value)
plt.show()