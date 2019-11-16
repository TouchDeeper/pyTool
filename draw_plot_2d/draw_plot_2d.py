
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


import os
# filepath = os.path.abspath('.')+"/"
#
# mu = []
#
# with open(filepath + 'lambda.txt', 'r') as f:
#     data = f.readlines()
#     for line in data:
#         mu_ = line.split()
#         numbers_float = map(float, mu_)
#         # print(numbers_float)
#         mu.append(numbers_float[0])
# x = list(range(0, len(mu), 1))
# print(x)
# print(mu)
# plt.xlabel("iteration")
# plt.ylabel("lambda")
# plt.plot(x, mu, color="r", linestyle="-", marker="*", linewidth=1.0)
# plt.show()


x = np.linspace(1, 60, 100)
y = 0.5 * np.power(2, np.exp(1-100.0/(100.0+1-x)))

plt.plot(x, y)

plt.title('200')
plt.xlabel('x')
plt.ylabel('y')

plt.show()



