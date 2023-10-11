import random
cities = {
    'City1': (2, 2),
    'City2': (4, 4),
    'City3': (6, 2),
    'City4': (8, 5),
    'City5': (3, 7),
    'City6': (9, 9),
    'City7': (8, 2),
    'City8': (1, 6)
}
def calculate_total_distance(tour):
    distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance += ((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2) ** 0.5
    return distance
def generate_initial_population(population_size):
    population = []
    cities_list = list(cities.keys())
    for _ in range(population_size):
        random.shuffle(cities_list)
        population.append(cities_list[:])
    return population
def tournament_selection(population, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        tournament = random.sample(population, 3)
        tournament.sort(key=lambda x: calculate_total_distance(x))
        selected_parents.append(tournament[0])
    return selected_parents
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [''] * len(parent1)
    for i in range(start, end + 1):
        child[i] = parent1[i]
    remaining_cities = [city for city in parent2 if city not in child]
    j = 0
    for i in range(len(child)):
        if child[i] == '':
            child[i] = remaining_cities[j]
            j += 1
    return child
def mutate(child):
    idx1, idx2 = random.sample(range(len(child)), 2)
    child[idx1], child[idx2] = child[idx2], child[idx1]
    return child
population_size = 100
num_generations = 1000
num_parents = 50
population = generate_initial_population(population_size)
for generation in range(num_generations):
    parents = tournament_selection(population, num_parents)
    new_population = parents.copy()
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        if random.random() < 0.2: 
            child = mutate(child)
        new_population.append(child)
    population = new_population
best_tour = min(population, key=lambda x: calculate_total_distance(x))
print("Best Tour:", best_tour)
print("Total Distance:", calculate_total_distance(best_tour))
