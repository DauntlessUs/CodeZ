# Open the file for reading
file = open("data.txt", "r")

# Read the data from the file as a string
data = file.read()

# Close the file
file.close()

# Split the data into a list of temperature strings
temperature_strings = data.split(", ")

# Use variables to store the info
number_of_temperatures = len(temperature_strings)
minimum_temperature = float(temperature_strings[0])
maximum_temperature = float(temperature_strings[0])
total_temperature = 0

# Convert temperature strings to floats
for temperature_str in temperature_strings:
    temperature = float(temperature_str)
    total_temperature += temperature

    if temperature < minimum_temperature:
        minimum_temperature = temperature

    if temperature > maximum_temperature:
        maximum_temperature = temperature

# Calculate the average temperature
average_temperature = total_temperature / number_of_temperatures

# Output
print("Number of temperature values:",number_of_temperatures)
print("Minimum temperature:", minimum_temperature)
print("Maximum temperature:", maximum_temperature)
print("Average temperature:", average_temperature)