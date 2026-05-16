import math
import random

import matplotlib.pyplot as plt

cities = [
    (0, 0),
    (2, 3),
    (5, 1),
    (6, 4),
    (8, 0),
    (1, 7),
    (4, 6)
]


def total_distance(route):
    distance = 0

    for i in range(len(route)):
        city_now = cities[route[i]]
        city_next = cities[route[(i + 1) % len(route)]]
        distance += euclidean_distance(city_now, city_next)

    return distance


def get_best_neighbor(route):
    best_neighbor = route[:]
    best_distance = total_distance(route)

    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

            neighbor_distance = total_distance(neighbor)

            if neighbor_distance < best_distance:
                best_neighbor = neighbor
                best_distance = neighbor_distance

    return best_neighbor, best_distance


def hill_climbing():
    current_route = list(range(len(cities)))
    random.shuffle(current_route)

    initial_route = current_route[:]
    initial_distance = total_distance(initial_route)

    while True:
        neighbor, neighbor_distance = get_best_neighbor(current_route)
        current_distance = total_distance(current_route)

        if neighbor_distance < current_distance:
            current_route = neighbor
        else:
            print("Solusi optimal lokal telah ditemukan")
            break

    return initial_route, initial_distance, current_route, total_distance(current_route)


def route_to_coordinates(route):
    x = [cities[i][0] for i in route]
    y = [cities[i][1] for i in route]

    x.append(cities[route[0]][0])
    y.append(cities[route[0]][1])

    return x, y


def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def plot_route(route, title):
    x, y = route_to_coordinates(route)

    plt.figure(figsize=(7, 5))
    plt.plot(x, y, marker="o")

    for i, city_index in enumerate(route):
        plt.text(cities[city_index][0], cities[city_index][1], f"K{city_index}")

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


initial_route, initial_distance, best_route, best_distance = hill_climbing()

print("Rute awal:")
print(initial_route)

print("\nRute terbaik hasil optimasi:")
print(best_route)

print("\nTotal jarak sebelum optimasi:")
print(round(initial_distance, 2))

print("\nTotal jarak sesudah optimasi:")
print(round(best_distance, 2))

plot_route(initial_route, "Visualisasi Rute Awal")
plot_route(best_route, "Visualisasi Rute Terbaik Hasil Hill Climbing")
