import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            value = float(item[aggregation_key])
            temps.append(value)
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)

# Print all cities in Germany
germany_cities = filter(lambda x: x["country"] == "Germany", cities)
print("Print all cities in Germany")
print(" ".join(city["city"] for city in germany_cities))
print()

# Print the average temperature of all the cities
avg_temp = aggregate("temperature", lambda x: sum(x) / len(x), cities)
print("Print the average temperature of all the cities")
print(avg_temp)
print()

# Print all cities in Spain with a temperature above 12°C
spain_cities = filter(lambda x: x["country"] == "Spain" and float(x["temperature"]) > 12, cities)
print("Print all cities in Spain with a temperature above 12°C")
print(" ".join(city["city"] for city in spain_cities))
print()

# Count the number of unique countries
print("Count the number of unique countries")
print(len(set(aggregate("country", lambda x: x, cities))))
print()

# Print the average temperature for all the cities in Germany
germany_cities = filter(lambda x: x["country"] == "Germany", cities)
avg_temp_germany = aggregate("temperature", lambda x: sum(x) / len(x), germany_cities)
print(avg_temp_germany)
print()

# Print the max temperature for all the cities in Italy
italy_cities = filter(lambda x: x["country"] == "Italy", cities)
max_temp_italy = aggregate("temperature", lambda x: max(x), italy_cities)
print("Print the max temperature for all the cities in Italy")
print(max_temp_italy)
print()
