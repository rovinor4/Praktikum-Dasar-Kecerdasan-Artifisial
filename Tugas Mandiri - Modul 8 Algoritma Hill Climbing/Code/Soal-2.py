import random

import matplotlib.pyplot as plt

tasks = ['A', 'B', 'C', 'D', 'E']

task_duration = {
    'A': 4,
    'B': 2,
    'C': 7,
    'D': 3,
    'E': 5
}

task_priority = {
    'A': 3,
    'B': 5,
    'C': 2,
    'D': 4,
    'E': 1
}


def calculate_cost(schedule):
    total_cost = 0
    completion_time = 0

    for task in schedule:
        completion_time += task_duration[task]
        total_cost += completion_time * task_priority[task]

    return total_cost


def get_best_neighbor(schedule):
    best_neighbor = schedule[:]
    best_cost = calculate_cost(schedule)

    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            neighbor = schedule[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

            neighbor_cost = calculate_cost(neighbor)

            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost

    return best_neighbor, best_cost


def hill_climbing():
    current_schedule = tasks[:]
    random.shuffle(current_schedule)

    initial_schedule = current_schedule[:]
    initial_cost = calculate_cost(initial_schedule)

    iteration = 0
    history = []

    print("Solusi awal:", initial_schedule)
    print("Cost awal:", initial_cost)
    print()

    history.append(initial_cost)

    while True:
        current_cost = calculate_cost(current_schedule)
        neighbor, neighbor_cost = get_best_neighbor(current_schedule)

        if neighbor_cost < current_cost:
            iteration += 1
            current_schedule = neighbor
            history.append(neighbor_cost)

            print("Iterasi ke-", iteration)
            print("Solusi:", current_schedule)
            print("Cost:", neighbor_cost)
            print()
        else:
            print("Solusi optimal lokal telah ditemukan")
            break

    return initial_schedule, initial_cost, current_schedule, calculate_cost(current_schedule), history


def plot_cost(history):
    plt.figure(figsize=(7, 5))
    plt.plot(range(len(history)), history, marker="o")
    plt.title("Perubahan Cost Setiap Iterasi")
    plt.xlabel("Iterasi")
    plt.ylabel("Cost")
    plt.grid(True)
    plt.show()


initial_schedule, initial_cost, best_schedule, final_cost, history = hill_climbing()

print("Solusi terbaik:", best_schedule)
print("Total cost akhir:", final_cost)

plot_cost(history)
