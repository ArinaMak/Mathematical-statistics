from scipy.stats import norm, laplace, poisson, cauchy, uniform
from statsmodels.distributions.empirical_distribution import ECDF
import seaborn as sns
import math as math
import numpy as np
import matplotlib.pyplot as plt

sizes = [20, 60, 100]
koeff = [0.5, 1, 2]
left_boarder, right_boarder = -4, 4
poisson_left_boarder, poisson_right_boarder = 6, 14
number_of_dist = 5

def get_rvs(size):
    rvs_list = [norm.rvs(size=size),
                cauchy.rvs(size=size), laplace.rvs(size=size),
                poisson.rvs(10, size=size), uniform.rvs(size=size, loc=-math.sqrt(3), scale=2 * math.sqrt(3))]
    return rvs_list

def get_pdf(x):
    pdf_list = [norm.pdf(x),
            cauchy.pdf(x), laplace.pdf(x, loc=0, scale=1 / math.sqrt(2)),
            poisson(10).pmf(x),
            uniform.pdf(x, loc=-math.sqrt(3), scale=2 * math.sqrt(3))]
    return pdf_list

def get_cdf(x):
    cdf_list = [norm.cdf(x),
                cauchy.cdf(x), laplace.cdf(x, loc=0, scale=1 / math.sqrt(2)),
                poisson.cdf(x, mu=10),
                uniform.cdf(x, loc=-math.sqrt(3), scale=2 * math.sqrt(3))]
    return cdf_list

def DrawCDF():
    sns.set_style('whitegrid')
    for num in range(number_of_dist):
        figures, axs = plt.subplots(ncols=3, figsize=(15, 5))
        name_list =["Normal distribution", "Cauchy distribution", "Laplace distribution", "Poisson distribution", "Uniform distribution"]
        for size in range(len(sizes)):
            rvs_list = get_rvs(sizes[size])
            if num != 3:
                x = np.linspace(left_boarder, right_boarder, 10000)
            else:
                x = np.linspace(poisson_left_boarder, poisson_right_boarder, 10000)
            y = get_cdf(x)
            sample = rvs_list[num]
            sample.sort()
            ecdf = ECDF(sample)
            axs[size].plot(x, y[num], color='blue', label='cdf')
            axs[size].plot(x, ecdf(x), color='red', label='ecdf')
            axs[size].legend(loc='lower right')
            axs[size].set(xlabel='x', ylabel='$F(x)$')
            axs[size].set_title(name_list[num] + ' n = ' + str(sizes[size]))
        figures.savefig('E:/_study/3 course/6th semester/MathStat/labs/lab1/lab1_4/pictures/' + name_list[num] + str(sizes[size]) + ".png")
    return

DrawCDF()

def DrawKDE():
    sns.set_style('whitegrid')
    for num in range(number_of_dist):
        name_list =["Normal distribution", "Cauchy distribution", "Laplace distribution", "Poisson distribution", "Uniform distribution"]
        for size in range(len(sizes)):
            figures, axs = plt.subplots(ncols=3, figsize=(15, 5))
            rvs_list = get_rvs(sizes[size])
            if num != 3:
                x = np.linspace(left_boarder, right_boarder, 10000)
            else:
                x = np.linspace(poisson_left_boarder, poisson_right_boarder, -poisson_left_boarder + poisson_right_boarder + 1)

            for kf in range(len(koeff)):
                y = get_pdf(x)
                sample = rvs_list[num]
                axs[kf].plot(x, y[num], color='red', label='pdf')
                sns.kdeplot(data=sample, bw_method='scott', bw_adjust=koeff[kf], ax=axs[kf], color='green',
                            fill=True, common_norm=False, linewidth=1.5, label='kde')
                axs[kf].legend(loc='upper right')
                axs[kf].set(xlabel='x', ylabel='$f(x)$')
                if num != 3:
                    axs[kf].set_xlim([left_boarder, right_boarder])
                else:
                    axs[kf].set_xlim([poisson_left_boarder, poisson_right_boarder])
                axs[kf].set_title(' h = ' + str(koeff[kf]))
            figures.suptitle(name_list[num] + ' KDE n = ' + str(sizes[size]))
            plt.show()
            figures.savefig('E:/_study/3 course/6th semester/MathStat/labs/lab1/lab1_4/pictures/' + name_list[num] + 'KDE' + str(sizes[size]) + ".png")
    return

DrawKDE()