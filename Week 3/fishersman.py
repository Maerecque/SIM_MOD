import matplotlib.pyplot as plt
import numpy as np

fish_plots = []
harvest_rates = [2e4, 5e4, 1e5, 2e5]

def logistic_growth():
    max_growth_rate = 0.5 
    carrying_capacity = 2e6

    duration = 10
    step_size = 0.1
    num_steps = int(duration / step_size)
    times = step_size * np.array(range(num_steps + 1))

    amount_fish = np.zeros([num_steps + 1]) 
    amount_fish[0] = 2e5

    for harvest_rate in harvest_rates:
        is_extinct = False
        for step in range(num_steps):
            if is_extinct:
                amount_fish[step+1] = 0
            else:
                amount_fish[step+1] = (amount_fish[step] + (step_size * max_growth_rate) * (1 - (amount_fish[step] / carrying_capacity)) * amount_fish[step]) - (harvest_rate * step_size)
                if amount_fish[step+1] <= 0:
                    is_extinct = True
                    amount_fish[step+1] = 0
        fish_plots.append(plt.plot(times, amount_fish))

    return amount_fish


def harvest():
    maximum_growth_rate = 0.5
    carrying_capacity = 2e6  
    maximum_harvest_rate = 0.7 * 2.5e5

    duration = 10.0
    step_size = 0.1
    num_steps = int(duration / step_size)

    amount_fish = np.zeros(num_steps + 1) 
    amount_fish[0] = 2e5

    results = []

    for ramp_start in np.arange(2.0, 10.01, 0.5):
        for ramp_end in np.arange(ramp_start, 10.01, 0.5):
            total_harvest = 0
            is_extinct = False
            for step in range(num_steps):
                time = step * step_size
                harvest_factor = 0.0
                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)

                harvest_rate = harvest_factor * maximum_harvest_rate

                if is_extinct:
                    amount_fish[step+1] = 0.0
                    current_harvest = 0
                else:
                    current_harvest = step_size * harvest_rate
                    amount_fish[step+1] = amount_fish[step] + step_size * (maximum_growth_rate * (1.0 - amount_fish[step] / carrying_capacity) * amount_fish[step] - harvest_rate)
                if amount_fish[step+1] <= 0.0:
                    is_extinct = True
                total_harvest += current_harvest
            results.append([ramp_start, ramp_end, total_harvest])
    return amount_fish, results

amount_fish, results = harvest()

for result in results:
    plt.scatter(x = result[0], y = result[1], s = result[2] / 10000, color = 'b')
    plt.xlabel("Start tijd")
    plt.ylabel("Eind tijd")
plt.title(label='MSY = 0.7')
plt.show()


# CODE FOR LOGISTIC GROWTH
# plot1, = fish_plots[0]
# plot2, = fish_plots[1]
# plot3, = fish_plots[2]
# plot4, = fish_plots[3]

plt.legend([harvestplot],harvest_rates)
axes = plt.gca()
axes.set_xlabel('Time in years')
axes.set_ylabel('Amount of fish')

plt.show()
