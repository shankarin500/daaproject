import itertools
from geopy.distance import geodesic

# Sample bus stops data: (id, name, latitude, longitude)
bus_stops = [
    (1, "Stop A", 19.0760, 72.8777),  # (id, name, lat, lon)
    (2, "Stop B", 19.0870, 72.8921),
    (3, "Stop C", 19.1010, 72.8842),
    (4, "Stop D", 19.1100, 72.8800)
]

# Function to calculate the distance between two bus stops using Geopy
def calculate_distance(stop1, stop2):
    return geodesic((stop1[2], stop1[3]), (stop2[2], stop2[3])).km

# Function to find the shortest route using brute-force approach (TSP)
def tsp_brute_force(stops):
    min_distance = float('inf')
    best_route = None
    # Generating all permutations of bus stops
    for perm in itertools.permutations(stops):
        route_distance = 0
        # Calculate distance for this permutation
        for i in range(len(perm) - 1):
            route_distance += calculate_distance(perm[i], perm[i + 1])
        # Check if the current route distance is the shortest
        if route_distance < min_distance:
            min_distance = route_distance
            best_route = perm
    return best_route, min_distance

# Finding the best route and its total distance
best_route, distance = tsp_brute_force(bus_stops)

# Displaying the result
print("Optimized Bus Route:")
for stop in best_route:
    print(f"Bus Stop: {stop[1]} (ID: {stop[0]})")
print(f"Total Distance: {distance} km")

# Function to check the accuracy (comparing with brute-force solution)
def check_accuracy(best_route, expected_distance):
    print("\nChecking the accuracy of the route optimization:")
    print(f"Optimized Route Distance: {expected_distance} km")
    print(f"Expected (Brute-Force) Distance: {expected_distance} km")
    if abs(expected_distance - distance) < 0.01:  # small tolerance
        print("The optimization is accurate!")
    else:
        print("There is a discrepancy in the optimization.")

# Checking the accuracy
check_accuracy(best_route, distance)
import itertools
from geopy.distance import geodesic
import matplotlib.pyplot as plt

# Sample bus stops data: (id, name, latitude, longitude)
bus_stops = [
    (1, "Stop A", 19.0760, 72.8777),  # (id, name, lat, lon)
    (2, "Stop B", 19.0870, 72.8921),
    (3, "Stop C", 19.1010, 72.8842),
    (4, "Stop D", 19.1100, 72.8800)
]

# Function to calculate the distance between two bus stops using Geopy
def calculate_distance(stop1, stop2):
    return geodesic((stop1[2], stop1[3]), (stop2[2], stop2[3])).km

# Function to find the shortest route using brute-force approach (TSP)
def tsp_brute_force(stops):
    min_distance = float('inf')
    best_route = None
    route_distances = []
    # Generating all permutations of bus stops
    for perm in itertools.permutations(stops):
        route_distance = 0
        # Calculate distance for this permutation
        for i in range(len(perm) - 1):
            route_distance += calculate_distance(perm[i], perm[i + 1])
        # Record the route distance
        route_distances.append(route_distance)
        # Check if the current route distance is the shortest
        if route_distance < min_distance:
            min_distance = route_distance
            best_route = perm
    return best_route, min_distance, route_distances

# Finding the best route and its total distance
best_route, distance, route_distances = tsp_brute_force(bus_stops)
# Displaying the result
print("Optimized Bus Route:")
for stop in best_route:
    print(f"Bus Stop: {stop[1]} (ID: {stop[0]})")
print(f"Total Distance: {distance} km")
# Function to check the accuracy (comparing with brute-force solution)
def check_accuracy(best_route, expected_distance):
    print("\nChecking the accuracy of the route optimization:")
    print(f"Optimized Route Distance: {expected_distance} km")
    print(f"Expected (Brute-Force) Distance: {expected_distance} km")
    accuracy_rate = (1 - (abs(expected_distance - distance) / expected_distance)) * 100
    print(f"Accuracy Rate: {accuracy_rate:.2f}%")
    return accuracy_rate

# Checking the accuracy and getting the accuracy rate
accuracy_rate = check_accuracy(best_route, distance)
# Visualizing the route distances and accuracy comparison using Matplotlib
def plot_accuracy_comparison(route_distances, best_route_distance):
    plt.figure(figsize=(10, 6))

    # Plotting the route distances
    plt.plot(route_distances, label="Route Distances", color="blue", marker='o', linestyle='--')

    # Highlighting the best route distance (optimized route)
    plt.axhline(y=best_route_distance, color='red', linestyle='-', label="Optimized Route Distance")

    # Adding labels and title
    plt.title("Route Distance Comparison and Optimization Accuracy")
    plt.xlabel("Route Number (Permutation)")
    plt.ylabel("Total Distance (km)")
    plt.legend()

    # Displaying the plot
    plt.show()

# Plotting the graph
plot_accuracy_comparison(route_distances, distance)
# Visualization
def plot_route(route, title, color):
    latitudes = [bus_stops[stop][0] for stop in route] + [bus_stops[route[0]][0]]
    longitudes = [bus_stops[stop][1] for stop in route] + [bus_stops[route[0]][1]]
    plt.plot(longitudes, latitudes, marker='o', label=title, color=color)
    for stop in route:
        plt.text(bus_stops[stop][1], bus_stops[stop][0], stop, fontsize=9, ha='right')

# Create the plot
plt.figure(figsize=(10, 6))
plot_route(actual_route, f"Actual Route ({actual_route_distance:.2f} km)", 'red')
plot_route(optimized_route, f"Optimized Route ({optimized_distance:.2f} km)", 'green')
plt.title("Actual vs Optimized Bus Routes")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid()
plt.show()
