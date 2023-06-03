import statistics
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib import transforms
from matplotlib.patches import Ellipse

self_sizes = [20, 60, 100]
self_iterations = 1000
self_rhos = [0, 0.5, 0.9]

#create a multivariate normal distribution and take random samples from it
def multivariate_normal_(size, rho, sig):
    #scipy.stats.multivariate_normal.rvs(mean,cov,size, random_state)
    return stats.multivariate_normal.rvs([0, 0], [[sig, rho], [rho, sig]], size=size)

def mixed_multivariate_normal_(size, rho, sig):
    #f(x,y)=0.9N(x, y, 0, 0, 1, 1, 0.9)+0.1N(x, y, 0, 0, 10, 10, -0.9)
    return 0.9*multivariate_normal_(size, 0.9, 1.0) + 0.1*multivariate_normal_(size, -0.9, 10.0)

#r_Q
def selective_quadrant_corel_coef_(x, y):
    x_med = np.median(x)
    y_med = np.median(y)
    n = [0, 0, 0, 0]

    for i in range(len(x)):
        if (x[i]-x_med) >= 0  and (y[i]-y_med) >= 0:
            n[0] += 1
        elif (x[i]-x_med) < 0 and (y[i]-y_med) >= 0:
            n[1] += 1
        elif (x[i]-x_med) < 0:
            n[2] += 1
        else:
            n[3] += 1

    return ((n[0] + n[2]) - (n[1] + n[3])) / len(x)

def print_row_(arr):
    str_print = "& "
    for a in arr:
        str_print += str(a) + " & "
    str_print += "\n"
    return str_print

def generate_stats(distr_generator, size, rho, sig):

    pearson_arr = list()
    spearman_arr = list()
    quadrant_arr = list()

    mean = list()
    sq_mean = list()
    disp = list()

    for i in range(self_iterations):
        multi_var = distr_generator(size, rho, 1.0)
        x, y = multi_var[:, 0], multi_var[:, 1]

        pearson_arr.append(stats.pearsonr(x, y)[0])
        spearman_arr.append(stats.spearmanr(x, y)[0])
        quadrant_arr.append(selective_quadrant_corel_coef_(x, y))

    mean.append(np.median(pearson_arr))
    sq_mean.append(np.median([pearson_arr[k] ** 2 for k in range(self_iterations)]))
    disp.append(statistics.variance(pearson_arr))

    mean.append(np.median(spearman_arr))
    sq_mean.append(np.median([spearman_arr[k] ** 2 for k in range(self_iterations)]))
    disp.append(statistics.variance(spearman_arr))

    mean.append(np.median(quadrant_arr))
    sq_mean.append(np.median([quadrant_arr[k] ** 2 for k in range(self_iterations)]))
    disp.append(statistics.variance(quadrant_arr))
    

    return np.around(mean, decimals=4), np.around(sq_mean, decimals=4), np.around(disp, decimals=4)

def build_ellipse(x, y, ax):
    pearson = np.cov(x, y)[0, 1] / np.sqrt(np.cov(x, y)[0, 0] * np.cov(x, y)[1, 1])

    #standard deviation      
    r_x = np.sqrt(1 + pearson)
    r_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=r_x*2, height=r_y * 2, facecolor='none', edgecolor='green', linewidth=2)
    scale_x = np.sqrt(np.cov(x, y)[0, 0]) * 3.0
    scale_y = np.sqrt(np.cov(x, y)[1, 1]) * 3.0

    transf = transforms.Affine2D().rotate_deg(45).scale(scale_x, scale_y).translate(np.mean(x), np.mean(y))
    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

def draw_ellipse(size):
    figures, ax = plt.subplots(1, 3)
    titles = [r'$ \rho = 0$', r' $\rho = 0.5 $', r' $ \rho = 0.9$']

    for i in range(len(self_rhos)):
        sample = multivariate_normal_(size, self_rhos[i], 1.0)
        x, y = sample[:, 0], sample[:, 1]
        build_ellipse(x, y, ax[i])
        ax[i].grid()
        ax[i].scatter(x, y, s=5, color="green")
        ax[i].set_title(titles[i])

    plt.suptitle(f"The scattering ellipse size={size}")
    plt.show()
    figures.savefig('E:/_study/3 course/6th semester/MathStat/labs/lab2/lab2_1/pictures/' + 'the scattering ellipse size=' + str(size) + ".png")

def lab2_1():
    for size in self_sizes:
        for rho in self_rhos:
            mean, sq_mean, disp = generate_stats(multivariate_normal_, size, rho, 1.0)
            print(f"Normal\t Size = {size}\t Rho = {rho}\n\t E(z) = \t {print_row_(mean)}\t E(z^2) = \t {print_row_(sq_mean)}\t D(z) = \t {print_row_(disp)}")

        mean, sq_mean, disp = generate_stats(mixed_multivariate_normal_, size, 0, 0)
        print(f"Mixed\t Size = {size}\n\t E(z) = \t {print_row_(mean)}\t E(z^2) = \t {print_row_(sq_mean)}\t D(z) = \t {print_row_(disp)}")
        print("-----------------------------------------------------------------------------")

        draw_ellipse(size)

lab2_1()