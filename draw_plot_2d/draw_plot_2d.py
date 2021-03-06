# encoding=utf-8
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# read specified column of txt
import os
filepath = os.path.abspath('.')+"/"

# mu = []
# generation_num_uniform = []
# average_cost_uniform = []
# best_total_cost_uniform = []
# with open(filepath + 'report_uniform.txt', 'r') as f:
#     data = f.readlines()
#     for line in data:
#         mu_ = line.split()
#         numbers_float = map(float, mu_)
#         # print(numbers_float)
#         generation_num_uniform.append(numbers_float[0])
#         average_cost_uniform.append(numbers_float[1])
#         best_total_cost_uniform.append(numbers_float[2])

# x = list(range(0, len(mu), 1))
# print(x)
# print(mu)
fig, ax = plt.subplots(figsize=(3.5, 3.4)) # 1 inch = 2.54 cm
plt.subplots_adjust(wspace=0, hspace=0.5)#调整子图间距
# plt.figure(figsize=(10, 5))

# plt.xlabel("iteration")
# plt.ylabel("lambda")
# plt.subplot(211)
# legend_average_1, = plt.plot(generation_num_uniform, average_cost_uniform, color="r", linestyle="-", marker="o", linewidth=3)
# plt.subplot(212)
# legend_best_1, = plt.plot(generation_num_uniform, best_total_cost_uniform, color="r", linestyle="-", marker='o', linewidth=3)

# generation_num_normal = []
# average_cost_normal = []
# best_total_cost_normal = []
# with open(filepath + 'report_non_uniform.txt', 'r') as f:
#     data = f.readlines()
#     for line in data:
#         mu_ = line.split()
#         numbers_float = map(float, mu_)
#         # print(numbers_float)
#         generation_num_normal.append(numbers_float[0])
#         average_cost_normal.append(numbers_float[1])
#         best_total_cost_normal.append(numbers_float[2])
# plt.subplot(211)
# legend_average_2, = plt.plot(generation_num_normal, average_cost_normal, color="blue", linestyle="-", marker="o", linewidth=3)
# plt.subplot(212)
# legend_best_2, = plt.plot(generation_num_normal, best_total_cost_normal, color="blue", linestyle="-", marker='o', linewidth=3)

generation_num_chromosomes = []
average_cost_chromosomes = []
best_total_cost_chromosomes = []
with open(filepath + 'report_mutate_by_chromosomes.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        mu_ = line.split()
        numbers_float = [float(s) for s in line.split()]
        # print(numbers_float)
        generation_num_chromosomes.append(numbers_float[0])
        average_cost_chromosomes.append(numbers_float[1])
        best_total_cost_chromosomes.append(numbers_float[2])
plt.subplot(211)
legend_average_3, = plt.plot(generation_num_chromosomes, average_cost_chromosomes, color="black", linestyle="-", marker="o",markersize=2, linewidth=1)
plt.subplot(212)
legend_best_3, = plt.plot(generation_num_chromosomes, best_total_cost_chromosomes, color="black", linestyle="-", marker='o',markersize=2, linewidth=1)

font_legend = {'family': 'Times New Roman', 'weight': 'normal', 'size': 8}
font_label = {'family': 'Times New Roman', 'weight': 'bold', 'size': 10}
# font_sticks = {'family': 'Times New Roman', 'weight': 'normal', 'size': 23}

ax = plt.subplot(211)
# 设置坐标轴刻度字体
plt.tick_params(labelsize=8)
sticks = ax.get_xticklabels() + ax.get_yticklabels()
[stick.set_fontname('Times New Roman') for stick in sticks]

ax.set_yscale("log")
# plt.legend([legend_average_1, legend_average_2, legend_average_3], ['U', 'N', 'C'], loc='upper right', prop=font_legend)
plt.grid(linestyle="--")  # 设置背景网格线为虚线
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去掉上边框
ax.spines['right'].set_visible(False)  # 去掉右边框
plt.xlabel('generation', font_label)
plt.ylabel('average fitness', font_label)


plt.subplot(212)
# 设置坐标轴刻度字体
plt.tick_params(labelsize=7)
sticks = ax.get_xticklabels() + ax.get_yticklabels()
[stick.set_fontname('Times New Roman') for stick in sticks]

plt.grid(linestyle="--")  # 设置背景网格线为虚线
# plt.legend([legend_best_1, legend_best_2, legend_best_3], ['U', 'N', 'C'], loc='upper right', prop=font_legend)
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去掉上边框
ax.spines['right'].set_visible(False)  # 去掉右边框
plt.xlabel('generation', font_label)
plt.ylabel('best fitness', font_label)

plt.show()

# draw a funciton
# x = np.linspace(1, 60, 100)
# y = 0.5 * np.power(2, np.exp(1-100.0/(100.0+1-x)))
#
# plt.plot(x, y)
#
# plt.title('200')
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.show()


