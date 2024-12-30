import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
    """ Generate a dictionary with the population per continent from a csv file """
    output = {}

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

            if continent not in output:
                output[continent] = {'years': [], 'population': []}
            output[continent]['years'].append(year)
            output[continent]['population'].append(population)

    return output

def generate_population_plot_from_dictionary(population_dictionary):
    for continent in population_dictionary:
        years = population_dictionary[continent]['years']
        population = population_dictionary[continent]['population']
        plt.plot(years, population, label=continent, marker="o", alpha=0.5)

    plt.title("Internet Population per Continent")
    plt.xlabel("Year")
    plt.ylabel("Internet Users")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

filename = 'data.csv'
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plot_from_dictionary(population_per_continent)
