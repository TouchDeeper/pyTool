import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skewnorm

NUM_SAMPLES = 100000
SKEW_PARAMS = [-3, 0]

def demo1():
    mu ,sigma = 0, 1
    sampleNo = 100000
    np.random.seed(0)
    s = np.random.normal(mu, sigma, sampleNo)

    plt.hist(s, bins=100, normed=True)
    plt.show()


def demo2():
    mu, sigma, num_bins = 0, 2, 50
    x = mu + sigma * np.random.randn(1000000)
    for i in range(len(x)):
        if x[i] > 0:
            x[i] = (x[i]-0)/(2-0)*(1-0)
    # 正态分布的数据
    n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor = 'blue', alpha = 0.5)
    # 拟合曲线
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('histogram of normal distribution: $\mu = 0$, $\sigma=1$')

    plt.subplots_adjust(left=0.15)
    plt.show()


def randn_skew_fast(N, alpha=0.0, loc=0.0, scale=1.0):
    sigma = alpha / np.sqrt(1.0 + alpha**2)
    u0 = np.random.randn(N)
    v = np.random.randn(N)
    u1 = (sigma*u0 + np.sqrt(1.0 - sigma**2)*v) * scale
    u1[u0 < 0] *= -1
    u1 = u1 + loc
    return u1


def normal_customized():
    sampleNo = 1000000
    mu1 = 0.01
    sigma1 = 0.025
    mu2 = mu1
    sigma2 = 0.015
    np.random.seed(0)
    s1 = np.random.normal(mu1, sigma1, sampleNo)
    s2 = np.random.normal(mu2, sigma2, sampleNo)
    for i in range(sampleNo):
        if s1[i] > mu1:
            s1[i] = mu1 - (s1[i] - mu1)
        if s2[i] < mu2:
            s2[i] = mu2 + mu2-s2[i]
    s = s1 + s2
    # np.histogram(s, bins=60, density=True)
    plt.figure(figsize=(10, 5))
    plt.grid(linestyle="--")  # 设置背景网格线为虚线
    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # 去掉上边框
    ax.spines['right'].set_visible(False)  # 去掉右边框
    plt.hist(s, normed=True, bins=100, histtype='step', color="black")
    plt.xlabel('genes', fontsize=13, fontweight='bold')
    plt.ylabel('probability density', fontsize=13, fontweight='bold')
    plt.xticks(fontsize=12, fontweight='bold')  # 默认字体大小为10
    plt.yticks(fontsize=12, fontweight='bold')
    plt.title("bi-side normal distribution", fontsize=12, fontweight='bold')  # 默认字体大小为12
    plt.vlines(mu1, 0, 15, colors="c", linestyles="dashed")
    plt.show()
# lets check again

if __name__ == '__main__':
    # # plt.subplots(figsize=(12, 4))
    # # for alpha_skew in SKEW_PARAMS:
    # #     p = randn_skew_fast(NUM_SAMPLES, alpha_skew)
    # #     sns.distplot(p)
    # fig, ax = plt.subplots(1, 1)
    # a = -3
    # mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')
    # x = np.linspace(skewnorm.ppf(0.01, a), skewnorm.ppf(0.99, a), 100)
    # ax.plot(x, skewnorm.pdf(x, a), 'r-', lw = 5, alpha = 0.6, label = 'skewnorm pdf')
    # # rv = skewnorm(a)
    # # ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
    # # vals = skewnorm.ppf([0.001, 0.5, 0.999], a)
    # # np.allclose([0.001, 0.5, 0.999], skewnorm.cdf(vals, a))
    # # r = skewnorm.rvs(a, size=1000)
    # # ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
    # # ax.legend(loc='best', frameon=False)
    # plt.show()

    normal_customized()


# demo1()
# demo2()
