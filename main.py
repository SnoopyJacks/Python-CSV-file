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


plt.plot([2000, 2001, 2002], [1990, 1991, 1992], label='Europe')
plt.plot([2000, 2001, 2002], [1990, 1991, 1992], label='Asia')

plt.title("Internet Population per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid(True)
plt.legend()
plt.show()
