# Program #3: US_Population
def us_population():
    population_data = []
    
    while True:
        year = int(input("Enter the year (or -1 to stop): "))
        if year == -1:
            break
        state = input("Enter the name of the state: ")
        population = int(input("Enter the population: "))
        population_data.append([year, state, population])

    query_year = int(input("Enter a year to query the total population: "))
    total_population = sum(pop[2] for pop in population_data if pop[0] == query_year)

    print(f"Total population for the year {query_year}: {total_population}")

us_population()
