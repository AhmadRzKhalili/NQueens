import random
import timeit

def count_attacking_pairs(ground):
    pairs = 0

    # row attacking pairs
    for queen in ground:
        if ground.count(queen) > 1:
            pairs += 1

    N = len(ground)

    # diagonal attacking pairs
    for i in range(N):
        queen1 = ground[i]

        for j in range(N):
            if j != i:
                queen2 = ground[j]
                if queen1 - queen2 == i - j or queen2 - queen1 == i - j:
                    pairs += 1
                    
                    
    return pairs // 2

def count_total_pairs(ground):
    N = len(ground)
    return (N * (N - 1)) // 2

def fitness(ground):
    total_pairs = count_total_pairs(ground)
    attacking_pairs = count_attacking_pairs(ground)

    return total_pairs - attacking_pairs

def create_chromosome(N):
    chromosome = random.sample(range(N), N)
    for i in range(len(chromosome)):
        chromosome[i] += 1

    return chromosome

def crossover(chromosome1, chromosome2, N):
    index = random.choice(range(N))
    new_chromosome = chromosome1[:index]
    new_chromosome.extend(chromosome2[index:])

    return new_chromosome

def mutation(chromosome, N):
    index = random.choice(range(N))
    gene = random.choice(range(1, N + 1))
    chromosome_copy = chromosome.copy()
    chromosome_copy[index] = gene
   
    return chromosome_copy

def reproduce(chromosome1, chromosome2, N):
    new_chromosome = crossover(chromosome1, chromosome2, N)
    return mutation(new_chromosome, N)

def solve_GA(N, POPULATION_SIZE):
    population = []
    

    full_fitness = count_total_pairs(range(1, N + 1))

    for i in range(POPULATION_SIZE):
        chromosome = create_chromosome(N)
        population.append(chromosome)

    generation = 1
    while True:
        population = sorted(population, reverse=True, key=lambda x:fitness(x))
        
        if fitness(population[0]) == full_fitness:
            return population[0], generation
        else:
            generation += 1

            new_population = []

            elite_index = int(0.1 * POPULATION_SIZE)
            new_population.extend(population[:elite_index])

            reproduce_index = int(0.9 * POPULATION_SIZE)
            for i in range(reproduce_index):
                chromosome1 = random.choice(population[:POPULATION_SIZE // 2])
                chromosome2 = random.choice(population[:POPULATION_SIZE // 2])
                new_chromosome = reproduce(chromosome1, chromosome2, N)
                new_population.append(new_chromosome)

            population = new_population

def main():
    N = int(input('N: '))
    POPULATION_SIZE = int(input('POPULATION_SIZE: '))

    avg_time = 0
    avg_generation = 0
    for i in range(100):
        start = timeit.default_timer()
        result = solve_GA(N, POPULATION_SIZE)
        stop = timeit.default_timer()
        avg_time = avg_time + (stop - start)

        # print('solution: ', result[0], 'generation number: ', result[1])
        avg_generation += result[1]

    avg_time /= 100
    avg_generation /= 100

    print('Average time: ', avg_time * 1000, 'milliseconds')  
    print('Average generation: ', avg_generation)  
        


if __name__ == "__main__":
    main()