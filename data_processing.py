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

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
germany_city = []
for city in cities:
    if city["country"] == "Germany":
        germany_city.append(city["city"])
print("Print all cities in Germany")
print(", ".join(germany_city))
print()

# Print all cities in Spain with a temperature above 12°C
spain_city_temp_above_12 = []
for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        spain_city_temp_above_12.append(city["city"])
print("Print all cities in Spain with a temperature above 12°C")
print(", ".join(spain_city_temp_above_12))
print()

# Count the number of unique countries
unique_countries = []
for city in cities:
    if city["country"] not in unique_countries:
        unique_countries.append(city["country"])
print("Count the number of unique countries")
print(len(unique_countries))
print()


# Print the average temperature for all the cities in Germany
germany_city_temp= []
for city in cities:
    if city["country"] == "Germany":
        germany_city_temp.append(float(city["temperature"]))
print("Print the average temperature for all the cities in Germany")
print(sum(germany_city_temp)/len(germany_city_temp))
print()

# Print the max temperature for all the cities in Italy
italy_city_temp= []
for city in cities:
    if city["country"] == "Italy":
        italy_city_temp.append(float(city["temperature"]))
print("Print the max temperature for all the cities in Italy")
print(max(italy_city_temp))
print()
