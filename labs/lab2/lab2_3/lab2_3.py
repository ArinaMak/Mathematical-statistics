import math
import numpy as np
import scipy.stats as stats
from tabulate import tabulate

def get_k(size):
    return math.ceil(1.72 * (size) ** (1 / 3))

def get_rvs(name, size):
    distr = None
    if name == 'norm':
        distr = np.random.normal(0, 1, size=size)
    elif name == 'laplace':
        distr = stats.laplace.rvs(size=size, scale=1 / math.sqrt(2), loc=0)
    elif name == 'uniform':
        distr = stats.uniform.rvs(size=size, loc=-math.sqrt(3), scale=2 * math.sqrt(3))
    return distr

def get_probability(distr, limits, size):
        p_arr = np.array([])
        n_arr = np.array([])

        for idx in range(-1, len(limits)):
            prev_cdf = 0 if idx == -1 else stats.norm.cdf(limits[idx])
            cur_cdf = 1 if idx == len(limits) - 1 else stats.norm.cdf(limits[idx + 1])
            p_arr = np.append(p_arr, cur_cdf - prev_cdf)

            if idx == -1:
                n_arr = np.append(n_arr, len(distr[distr <= limits[0]]))
            elif idx == len(limits) - 1:
                n_arr = np.append(n_arr, len(distr[distr >= limits[-1]]))
            else:
                n_arr = np.append(n_arr, len(distr[(distr <= limits[idx + 1]) & (distr >= limits[idx])]))
        result = np.divide(np.multiply((n_arr - size * p_arr), (n_arr - size * p_arr)), p_arr * size)
        return n_arr, p_arr, result

def print_(n_arr, p_arr, result, size, limits):
    decimal = 4
    cols = ["i", "limits", "n_i", "p_i", "np_i", "n_i - np_i", "frac{(n_i-np_i)^2}{np_i}"]
    rows = []
    for i in range(0, len(n_arr)):
        if i == 0:
            boarders = [-np.inf, np.around(limits[0], decimals=decimal)]
        elif i == len(n_arr) - 1:
            boarders = [np.around(limits[-1], decimals=decimal), 'inf']
        else:
            boarders = [np.around(limits[i - 1], decimals=decimal), np.around(limits[i], decimals=decimal)]

        rows.append(
            [i + 1, boarders, n_arr[i], np.around(p_arr[i], decimals=decimal),
                np.around(p_arr[i] * size, decimals=decimal),
                np.around(n_arr[i] - size * p_arr[i], decimals=decimal),
                np.around(result[i], decimals=decimal)]
        )

    rows.append([len(n_arr) + 1, "-", np.sum(n_arr), np.around(np.sum(p_arr), decimals=4), np.around(np.sum(p_arr * size), decimals=decimal), -np.around(np.sum(n_arr - size * p_arr), decimals=decimal), np.around(np.sum(result), decimals=decimal)])
    print(tabulate(rows, cols, tablefmt="latex"))

def lab2_3():
    distr_names = {'norm': 100, 'laplace': 20, 'uniform': 20}
    alpha = 0.05

    for item in distr_names.items():
        distr = get_rvs(item[0], size=item[1])
        k = get_k(item[1])
        limits = np.linspace(-1.1, 1.1, num=k - 1)
        n_arr, p_arr, result = get_probability(distr, limits, item[1])
        print_(n_arr, p_arr, result, item[1], limits)

lab2_3()
