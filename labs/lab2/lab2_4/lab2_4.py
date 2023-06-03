import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

def plot_(x_set, m_all, s_all, name):
    figures, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4, figsize=(15, 5))

    ax1.hist(x_set[0], density=True, histtype="stepfilled", label='n = 20', color="#a7da8e")
    ax1.legend(loc='upper right')
    ax1.set_title("histogram")
    ax1.set_ylim(0, 1)
    
    ax2.hist(x_set[1], density=True, histtype="stepfilled", label='n = 100', color="#a7da8e")
    ax2.legend(loc='upper right')
    ax2.set_title("histogram")
    ax2.set_ylim(0, 1)

    ax3.plot(m_all[0], [1, 1], 'go-', label='n = 20')
    ax3.plot(m_all[1], [1.1, 1.1], 'bo-', label='n = 100')
    ax3.legend()
    ax3.set_title(' "m" interval')
    ax3.set_ylim(0.9, 1.4)

    ax4.plot(s_all[0], [1, 1], 'go-', label='n = 20')
    ax4.plot(s_all[1], [1.1, 1.1], 'bo-', label='n = 100')
    ax4.legend()
    ax4.set_title(r' $\sigma$ '+"interval")
    ax4.set_ylim(0.9, 1.4)

    if(name=="norm"):
        figures.suptitle("Normal distribution and confidence intervals.")
    else:
        figures.suptitle("Normal distribution and confidence intervals. Asymptotic approach")

    figures.savefig('E:/_study/3 course/6th semester/MathStat/labs/lab2/lab2_4/pictures/' + name + ".png")
    plt.show()

def lab2_4():
    alpha = 0.05
    self_size=[20, 100]

    m_dict = {"norm": list(), "asymp": list()}
    s_dict = {"norm": list(), "asymp": list()}
    x_all = list()
    for n in self_size:
        x = np.random.standard_normal(size=n)
        x_all.append(x)
        m = np.mean(x)
        s = np.sqrt(np.mean(x*x) - (np.mean(x)) ** 2)
        m_n = [m - s * (stats.t.ppf(1 - alpha / 2, n - 1)) / np.sqrt(n - 1), m + s * (stats.t.ppf(1 - alpha / 2, n - 1)) / np.sqrt(n - 1)]
        s_n = [s * np.sqrt(n) / np.sqrt(stats.chi2.ppf(1 - alpha / 2, n - 1)), s * np.sqrt(n) / np.sqrt(stats.chi2.ppf(alpha / 2, n - 1))]

        m_dict["norm"].append(m_n)
        s_dict["norm"].append(s_n)

        m_a = [m - stats.norm.ppf(1 - alpha / 2) / np.sqrt(n), m + stats.norm.ppf(1 - alpha / 2) / np.sqrt(n)]
        e = (sum( (x - m) ** 4) / n) / s ** 4 - 3
        s_a = [s / np.sqrt(1 + stats.norm.ppf(1 - alpha / 2) * np.sqrt((e + 2) / n)), s / np.sqrt(1 - stats.norm.ppf(1 - alpha / 2) * np.sqrt((e + 2) / n))]

        m_dict["asymp"].append(m_a)
        s_dict["asymp"].append(s_a)

    for key in m_dict.keys():
        print(key)
        print(f"1 {key} : {round(m_dict[key][0][0], 2)} < $m$ < {round(m_dict[key][0][1], 2)} & {round(s_dict[key][0][0], 2)} < $\sigma$ < {round(s_dict[key][0][1], 2)}")
        print(f"2 {key} : {round(m_dict[key][1][0], 2)} < $m$ < {round(m_dict[key][1][1], 2)} & {round(s_dict[key][1][0], 2)} < $\sigma$ < {round(s_dict[key][1][1], 2)}")
        plot_(x_all, m_dict[key], s_dict[key], key)

lab2_4()