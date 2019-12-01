import matplotlib.pyplot as plt

def salt(steps):
    going_in_a = 6
    going_out_a = 4
    going_out_a2b = 3
    going_in_b = going_out_a2b
    going_out_b2a = 1
    going_out_b = 2
    salt_going_in_a = 0.2
    total_water = 100
    total_salt_in_a = 0
    total_salt_in_b = 20

    amountA = [total_salt_in_a]
    amountB = [total_salt_in_b]
    times = [0]

    for step in range(steps):
        temp_salt_add_a = ((salt_going_in_a * going_in_a) + going_out_b2a * (total_salt_in_b / total_water)) - ((going_out_a + going_out_a2b) * (total_salt_in_a / total_water))
        temp_salt_add_b = (going_in_b * (total_salt_in_a / total_water)) - ((going_out_b + going_out_b2a) * (total_salt_in_b / total_water))
        total_salt_in_a += temp_salt_add_a
        total_salt_in_b += temp_salt_add_b

        amountA.append(total_salt_in_a)
        amountB.append(total_salt_in_b)
        times.append(step)

    return amountA, amountB, times

def plot_me():
    salt1,salt2, time1 = salt(200)

    plt.plot(time1, salt1, label = "Tank A")
    plt.plot(time1, salt2, label = "Tank B")
    plt.legend()
    plt.show()

plot_me()