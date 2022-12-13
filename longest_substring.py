"""
Created on Fri Dec  9 18:57:39 2022

@author: Ryan Jiao (rsj7519@g.rit.edu), Xinyu Hu (xh1165@g.rit.edu)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import statistics as sta
import math

def generate_permutation(n, m):
    """
    create m permutations of length n
    :param n: length of each permutations
    :param m: number of permutations to check
    :return: list of permutations
    """
    p_list = []
    l = list(range(1, n + 1))
    i = 0
    factorial = math.factorial(n)
    if factorial < m:
        m = factorial
    while i < m:
        p = np.random.permutation(l)
        p_arr = list(p)
        if p_arr not in p_list:
            p_list.append(p_arr)
            i = i + 1
    return p_list


def longest_substring(p):
    """
    find the longest increasing substring of a permutation
    :param p: a permutation
    :return: longest increasing substring of the permutation
    """
    max_count = [1] * len(p)
    for i in range(1, len(max_count)):
        for j in range(i):
            if (p[i] > p[j]):
                max_count[i] = max(max_count[i], max_count[j]+1)
    return max(max_count)


def check_permutations(l):
    """
    Find the longest increasing substring for each permutation in a list
    :param l: list of permutations
    :return: list of the longest increasing substring of each permutation
    """
    lst = []
    for p in l:
        k = longest_substring(p)
        lst.append(k)
    return lst


def avg_len(l):
    """
    Find the average longest increasing substring for permutations of a given length
    :param l: list of the longest increasing substring for permutations of a given length
    :return: the average longest increasing substring
    """
    return sum(l)/len(l)

def graph(l, a):
    """
    Graph the average longest substring against the length of the permutations
    :param l: list of the length of the permutations
    :param a: list of the average longest substring of permutations of various length
    :return: None
    """
    plt.figure()
    plt.plot(l, a, label="Permutation Results")
    plt.xticks(fontsize=8)
    for xy in zip(l, a):
        plt.annotate('(%.2f, %.2f)' % xy, xy=xy)
    plt.title('Average Longest Increasing Substring for Different Length Permutations')
    plt.xlabel('Length of Permutations')
    plt.ylabel('Average Longest Substring')
    plt.legend()
    plt.show()


def graph_test(l, a):
    """
    Graph initial guesses for best fit line
    :param l: list of the length of the permutations
    :param a: list of the average longest substring of permutations of various length
    :return: None
    """
    plt.figure()
    plt.plot(l, a, label="Permutation Results")
    plt.xticks(fontsize=8)

    y1 = []
    for i in l:
        y1.append(math.log10(i))
    plt.plot(l, y1, label="log(x)")

    y2 = []
    for i in l:
        y2.append(math.log(i))
    plt.plot(l, y2, label="ln(x)")

    y3 = []
    for i in l:
        y3.append(math.sqrt(i))
    plt.plot(l, y3, label="sqrt(x)")

    plt.title('Initial Test of Best Fit Line')
    plt.xlabel('Length of Permutations')
    plt.ylabel('Average Longest Substring')
    plt.legend()
    plt.show()


def graph_fit(l, a):
    """
    Graph initial guesses for best fit line
    :param l: list of the length of the permutations
    :param a: list of the average longest substring of permutations of various length
    :return: The fitted parameter of the best fit curve
    """
    plt.figure()
    plt.plot(l, a, label="Permutation Results")
    plt.xticks(fontsize=8)

    l_np = np.array(l)
    a_np = np.array(a)
    popt, pcov = curve_fit(curve, l_np, a_np)
    plt.plot(l_np, curve(l_np, *popt), label="Best Fit: %f*sqrt(x)" % popt[0])

    plt.title('Best Fit of Permutations')
    plt.xlabel('Length of Permutations')
    plt.ylabel('Average Longest Substring')
    plt.legend()
    plt.show()

    return popt[0]


def curve(x, a):
    """
    General form of best fit curve (the square root function)
    :param x: Length of permutations
    :param a: The calculated value of the fitted curve
    :return: a list of the parameter of the fitted curve
    """
    return a*np.sqrt(x)


def chebyshev(l, a, d, param):
    """
    Calculate precision and accuracy using Chebyshev's inequality
    :param l: list of length of permutations
    :param a: list of average longest increasing substrings
    :param d: list of standard deviations
    :param param: The fitted parameter of the square root function
    :return: list of the calculated Chebyshev's value
    """
    t_lst = []
    chev = []
    for i in range(len(l)):
        t = abs(a[i] - curve(l[i], param))/d[i]
        t_lst.append(t)
        chev.append(1/t**2)
    return t_lst, chev


x = 16
# list of the length of permutations checked
length_lst = []
# list of the average longest increasing substring for permutations of different length
avg_lst = []
# list of standard deviation for permutations of different length
std_lst = []
while x <= 2048:
    length_lst.append(x)
    lst = generate_permutation(x, 100)
    l = check_permutations(lst)
    print(x)
    std_lst.append(sta.stdev(l))
    avg = avg_len(l)
    print(avg)
    avg_lst.append(avg)
    print()
    x = x * 2
graph(length_lst, avg_lst)
graph_test(length_lst, avg_lst)
param = graph_fit(length_lst, avg_lst)
result = chebyshev(length_lst, avg_lst, std_lst, param)
print("t")
print(result[0])
print("standard dev")
print(std_lst)
print("chev")
print(result[1])