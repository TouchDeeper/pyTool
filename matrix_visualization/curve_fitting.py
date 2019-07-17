# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def poly_fit(data_x, data_y, poly_deg, x_lable_name, y_lable_name):
    # 定义x、y散点坐标
    x = np.array(data_x)
    y = np.array(data_y)
    # 用线性拟合
    f = np.polyfit(x, y, poly_deg)
    p = np.poly1d(f)
    print(p)
    # 也可使用yvals=np.polyval(f1, x)
    yvals = p(x)

    # 绘图
    fig = plt.figure()
    plot1 = plt.plot(x, y, 's', label='original values')
    plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
    plt.xlabel(x_lable_name)
    plt.ylabel(y_lable_name)
    plt.legend(loc=4)  # 指定legend的位置右下角
    plt.title('polyfitting')
    plt.savefig(x_lable_name+'_'+y_lable_name+'.png')
    return p

def points_compute(age_input, Troponin_input, NT_ProBNP_input):
    # 定义x、y散点坐标
    age = [44, 55, 65, 75, 90]
    Troponin = [1, 2, 5, 10, 30, 75, 180]
    NT_ProBNP = [25, 50, 100, 200, 400, 800, 1500, 3000, 5900]

    points_age = [0.00, 0.75, 1.38, 2.0625, 3.0625]
    points_Troponin = [0, 0.775, 1.775, 2.542, 3.75, 4.775, 5.725]
    points_NT_ProBNP = [0, 1.275, 2.542, 3.8, 5.083, 6.35, 7.5, 8.775, 10]

    p_age = poly_fit(age, points_age, 1, 'age', 'points')
    p_Troponin = poly_fit(Troponin, points_Troponin, 5, 'Troponin', 'points')
    p_NT_ProBNP = poly_fit(NT_ProBNP, points_NT_ProBNP, 6, 'NT_ProBNP', 'points')
    # print('points_age: ', p_age(age_input))
    # print('points_Troponin: ', p_Troponin(Troponin_input))
    # print('points_NT_ProBNP: ', p_NT_ProBNP(NT_ProBNP_input))
    return p_age(age_input) + p_Troponin(Troponin_input) + p_NT_ProBNP(NT_ProBNP_input)

    # plt.show()


# points_compute(55, 2, 50)
