import matplotlib.pyplot as plt

def salt(steps, speed_out=6):
    going_in = 6
    salt_going_in = 0.1
    going_out = speed_out
    total_water = 1000
    total_salt = 0

    amount = [0]
    times = [0]

    for step in range(steps):
        total_salt += (salt_going_in * going_in) - (total_salt / total_water * going_out)

        amount.append(total_salt)
        times.append(step)

    return amount, times

def plot_me():
    salt1, time1 = salt(1000)
    salt2, time2 = salt(1000,5)

    plt.plot(time1, salt1, label = "Outspeed = 6")
    plt.plot(time2, salt2, label = "Outspeed = 5")
    plt.legend()
    plt.show()

plot_me()