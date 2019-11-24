import numpy
import matplotlib.pyplot as plt

population = 55000000
contacts_per_day = 49
chance_infection = 0.09
transmission_coeff = 1 / (contacts_per_day * chance_infection)

i0 = 1
r0 = 0
e0 = 0
s0 = population - i0 - r0 - e0

sigma = chance_infection
gamma = 0
beta = transmission_coeff

def seir(S, E, I, R, N, T, sigma, gamma, beta):
    s = numpy.zeros(T + 1)
    e = numpy.zeros(T + 1)
    i = numpy.zeros(T + 1)
    r = numpy.zeros(T + 1)
    t = numpy.zeros(T + 1)

    for step in range(0, T+1):
        S -= beta * (S * I / N)
        E += beta * (S * I / N) - sigma * E
        I += sigma * E - gamma * I
        R += gamma * I

        s[step] = S
        i[step] = I
        e[step] = E
        r[step] = R

        t[step] = step

    return s, e, i, r, t

s, e, i, r, times = seir(s0,i0,e0,r0,60,population,sigma,gamma,beta)
plt.plot(times, s)
plt.plot(times, e)
plt.plot(times, i)
plt.plot(times, r)
plt.show()


