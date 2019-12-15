import scipy as sp
import numpy as np
import math

m = 100000


def average(given_numbers):
    avg = 0
    for i in given_numbers:
        avg -= -i
    avg /= (len(given_numbers)-1)
    return avg


def variation(given_numbers):
    interval = np.arange(0, 1.1, step = 0.1)
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


# Pseudo random generator: made with the help of Computer Simulation Techniques by Harry Peros
def random_generator(seed, amount):
    # NOTE: set scenario for a guarantee full period
    # m and c cannot have a common divisor
    # a = 1 if m is a multiple of 4
    # a = 1 if r is a prime factor of m. That is true, if r is a prime number that can devide m, then it divides a-1

    a = 314
    c = 453

    sequence = []
    previous_step = seed

    for i in range(amount):
        new_num = ((a * previous_step) + c) % m
        previous_step = new_num
        sequence.append(new_num/m)

    return sequence


def test_generator():
    for i in range(1, 101):
        generated_numbers = random_generator(i, 1000)
        bin_count = bin_counter(variation(generated_numbers))
        print("Average of generated nums: ", average(generated_numbers), sp.stats.chisquare(bin_count))


def approach_pi():
    temp = 0

    calculated_pi = []
    smallest_number = []
    indexes_smallest = []

    for i in range(1, m):
        # Seed will have to be divided, because a larger seed will give worst results than a small(er) seed
        x = random_generator(i / 10, 1)          # x and y will get an almost identical seed.
        y = random_generator((i + 0.1) / 10, 1)  # because otherwise you'll get the same numbers (duh)

        if math.sqrt(x[0]**2 + y[0]**2) <= 1:  # x^2 + y^2
            temp += 1
        calculated_pi.append(4 * temp / (i + 1))

    for i in range(len(calculated_pi)):
        calc = abs(calculated_pi[i] - math.pi)
        indexes_smallest.append(i)
        smallest_number.append(calc)

    closest_num = min(smallest_number)
    index = indexes_smallest[smallest_number.index(closest_num)]
    return calculated_pi[index]
