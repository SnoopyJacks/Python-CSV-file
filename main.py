import csv
import matplotlib.pyplot as plt

filename = 'data.csv'

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        continent = line['continent']
        year = line['year']
        population = line['population']

        print(continent)
        print(year)
        print(population)



plt.plot([2000, 2001, 2002], [1990, 1991, 1992], label='Europe')
plt.plot([2000, 2001, 2002], [1990, 1991, 1992], label='Asia')

plt.title("Internet Population per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid(True)
plt.show()
