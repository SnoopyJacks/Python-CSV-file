import csv
import matplotlib.pyplot as plt

filename = 'data.csv'

population_per_continent = {}


with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        continent = line['continent']
        year = line['year']
        population = line['population']

        if continent not in population_per_continent:
            population_per_continent[continent] = {'population': [], 'years': []}

        population_per_continent[continent]['population'].append(population) 
        population_per_continent[continent]['years'].append(year)

for continent in population_per_continent:
    years = population_per_continent[continent]['years']
    population = population_per_continent[continent]['population']
    plt.plot(years,population, label=continent, marker="o", alpha=0.5)

plt.title("Internet Population per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
