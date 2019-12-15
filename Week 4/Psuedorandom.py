import scipy as sp
import random
import numpy as np
import math

def average(given_numbers):
    avg = 0
    for i in given_numbers:
        avg -=-i
    avg /= (len(given_numbers)-1)
    return avg


def variation(given_numbers):
    interval = np.arange(0, 1.1, step=.1)
    bins = []

    for i in range(len(interval)-1):
        new_bin = []
        for num in given_numbers:
            if interval[i] < num and num <= interval[i+1]:
                new_bin.append(num)
        bins.append(new_bin)

    return np.array(bins)

def bin_counter(bins):
    bin_count = []
    for i in bins:
        bin_count.append(len(i))
    return bin_count



