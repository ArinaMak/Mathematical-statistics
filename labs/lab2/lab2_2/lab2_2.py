import scipy
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

self_a = -1.8
self_b = 2
self_step = 0.2

def f_(x):
    return (2 * x + 2)

def f_with_err_(x):
    return [2 * xi + 2 + stats.norm.rvs(0, 1) for xi in x]

def beta_(x, y):
    beta_1 = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x * x) - np.mean(x) ** 2)
    beta_0 = np.mean(y) - beta_1 * np.mean(x)
    return beta_0, beta_1

def method_least_squares_(x, y):
    beta_0, beta_1 = beta_(x, y)
    return [beta_0 + beta_1 * xi for xi in x]

def least_module_(beta, x, y) -> float:
    beta_0, beta_1 = beta
    return sum([abs(y[i] - beta_0 - beta_1 * x[i]) for i in range(len(x))])

def least_module_beta_(x, y):
    beta_0, beta_1 = beta_(x, y)
    result = scipy.optimize.minimize(least_module_, [beta_0, beta_1], args=(x, y), method='SLSQP')
    return result.x[0], result.x[1]

def method_least_modules_(x, y):
    beta_0, beta_1 = least_module_beta_(x, y)
    return [beta_0 + beta_1 * xi for xi in x]

def plot_(x, y, name: str) -> None:
    y_mls = method_least_squares_(x, y)
    y_mlm = method_least_modules_(x, y)

    dist_mls = sum((f_(x)[i] - y_mls[i]) ** 2 for i in range(len(y)))
    dist_mlm = sum(abs(f_(x)[i] - y_mlm[i]) for i in range(len(y)))

    plt.scatter(x, y, c="black", s=3, label="Выборка")
    plt.plot(x, f_(x), color="red", label="Модель")
    plt.plot(x, y_mls, color="blue", label="МНК")
    plt.plot(x, y_mlm, color="green", label="МНМ")

    plt.xlim([self_a, self_b])
    plt.grid()
    plt.legend()
    plt.title(name)
    plt.savefig('E:/_study/3 course/6th semester/MathStat/labs/lab2/lab2_2/pictures/' + name + ".png")
    plt.show()
    

def lab2_2():
    x = np.arange(self_a, self_b, self_step)
    y = f_with_err_(x)
    plot_(x, y, "Distribution")
    print("y")
    print(y)
    y[0] += 10
    y[-1] -= 10
    plot_(x, y, "Distribution with perturbation")

lab2_2()