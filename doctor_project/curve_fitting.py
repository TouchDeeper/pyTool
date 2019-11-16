# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class PolyFit:
    def __init__(self):
        self.__fig = plt.figure()
        self.__Troponin_popt = []
        self.__NT_ProBNP_popt = []

    def fun_Troponin(self, x, a, b, c):
        return 1/(a + b/(x+c))

    def fun_NT_ProBNP(self, x, a, b, c):
        return 1/(a + b/(x+c))

    def plot_2d_function(self, fun, x_start, x_end, num_points, x_lable_name, y_lable_name):
        # 也可使用yvals=np.polyval(f1, x)
        x = np.linspace(x_start, x_end, num_points)
        y = fun(x)

        plot2 = plt.plot(x, y, 'r', label='polyfit values')
        plt.xlabel(x_lable_name)
        plt.ylabel(y_lable_name)
        plt.legend(loc=4)  # 指定legend的位置右下角
        plt.title('polyfitting')
        plt.savefig(x_lable_name+'_'+y_lable_name+'.png')

    def plot_x_y(self, x, y, x_lable_name, y_lable_name):

        plt.plot(x, y, 'r', label='polyfit values')
        plt.xlabel(x_lable_name)
        plt.ylabel(y_lable_name)
        plt.legend(loc=4)  # 指定legend的位置右下角
        plt.title('polyfitting')
        plt.savefig(x_lable_name + '_' + y_lable_name + '.png')

    def poly_fit(self, data_x, data_y, poly_deg):
        # 定义x、y散点坐标
        x = np.array(data_x)
        y = np.array(data_y)
        # 用线性拟合
        f = np.polyfit(x, y, poly_deg)
        p = np.poly1d(f)
        print(p)
        plt.plot(x, y, 's', label='original values')

        return p


    def P_age(self):
        plt.clf()
        age = [44, 55, 65, 75, 90]
        points_age = [0.00, 0.75, 1.38, 2.0625, 3.0625]

        p_age = self.poly_fit(age, points_age, 1)
        self.plot_2d_function(p_age, 18, 98, 81, 'age', 'points')
        return p_age


    # def P_Troponin(self):
    #     plt.clf()
    #     Troponin = [1, 2, 5, 10, 30, 75, 180]
    #     points_Troponin = [0, 0.775, 1.775, 2.542, 3.75, 4.775, 5.725]
    #     p_Troponin = self.poly_fit(Troponin, points_Troponin, 3)
    #     self.plot_2d_function(p_Troponin, 1, 220, 220, 'Troponin', 'points')
    #
    #     return p_Troponin

    def P_Troponin(self):
        plt.clf()
        Troponin = [1, 2, 5, 10, 30, 75, 180]
        points_Troponin = [0, 0.775, 1.775, 2.542, 3.75, 4.775, 5.725]
        # p_Troponin = self.poly_fit(Troponin, points_Troponin, 3)
        self.__Troponin_popt, pcov = curve_fit(self.fun_Troponin, Troponin, points_Troponin)
        plt.plot(Troponin, points_Troponin, 's', label='original values')

        x = np.linspace(0, 220, 220)
        y = self.fun_Troponin(x, self.__Troponin_popt[0], self.__Troponin_popt[1], self.__Troponin_popt[2])
        self.plot_x_y(x, y, 'Troponin', 'points')

    def get_p_Troponin(self, x):
        y = self.fun_Troponin(x, self.__Troponin_popt[0], self.__Troponin_popt[1], self.__Troponin_popt[2])
        return y

    def P_Nt_ProBNP(self):
        plt.clf()

        NT_ProBNP = [25, 50, 100, 200, 400, 800, 1500, 3000, 5900]
        # for temp in NT_ProBNP:
        #     temp = 0.03 * temp
        NT_ProBNP = [0.03 * temp for temp in NT_ProBNP]
        points_NT_ProBNP = [0, 1.275, 2.542, 3.8, 5.083, 6.35, 7.5, 8.775, 10]
        # p_NT_ProBNP = self.poly_fit(NT_ProBNP, points_NT_ProBNP, 4)
        self.__NT_ProBNP_popt, pcov = curve_fit(self.fun_NT_ProBNP, NT_ProBNP, points_NT_ProBNP)
        plt.plot(NT_ProBNP, points_NT_ProBNP, 's', label='original values')
        # x = np.linspace(24, 6500, 6000)
        x = np.linspace(0, 220, 221)
        y = self.fun_NT_ProBNP(x, self.__NT_ProBNP_popt[0], self.__NT_ProBNP_popt[1], self.__NT_ProBNP_popt[2])
        self.plot_x_y(x, y, 'NT_ProBNP', 'points')

    def get_p_Nt_ProBNP(self, x):
        x = [0.03 * temp for temp in x]
        y = self.fun_NT_ProBNP(x, self.__NT_ProBNP_popt[0], self.__NT_ProBNP_popt[1], self.__NT_ProBNP_popt[2])
        return y


def points_compute(stroke_input, age_input, Troponin_input, NT_ProBNP_input):

    if(stroke_input == 1):
        p_stroke = 5.475
    else:
        p_stroke = 0
    poly_fitter = PolyFit()
    p_age = poly_fitter.P_age()

    # p_Troponin = poly_fitter.P_Troponin()
    poly_fitter.P_Troponin()
    # p_NT_ProBNP = poly_fitter.P_Nt_ProBNP()
    poly_fitter.P_Nt_ProBNP()
    # print('points_age: ', p_age(age_input))
    # print('points_Troponin: ', poly_fitter.get_p_Troponin(Troponin_input))
    # print('points_NT_ProBNP: ', p_NT_ProBNP(NT_ProBNP_input))
    return p_age(age_input) + poly_fitter.get_p_Troponin(Troponin_input) + poly_fitter.get_p_Nt_ProBNP(NT_ProBNP_input) + p_stroke

    # plt.show()


# print(points_compute(0, 62, 179, 1714))


