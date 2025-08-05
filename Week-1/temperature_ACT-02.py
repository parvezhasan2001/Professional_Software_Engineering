# Week 2 - Temperature Analysis
# This Activity calculates the average, highest, and lowest temperatures from a list of temperature values.

temperature = [18.5,19,20,25.0,2,30,13.9]
def calculate_average_temperature(values):
    average_score = sum(values) / len(values)
    return average_score
def calculate_highest_temperature(values):
    return max(values)
def calculate_lowest_temperature(values):
    return min(values)
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def calculate_number_of_days_temperature_exceeded(values):
    return len([temp for temp in values if temp > 20])


if __name__ == "__main__":
    average_temperature = calculate_average_temperature(temperature)
    highest_temperature = calculate_highest_temperature(temperature)
    lowest_temperature = calculate_lowest_temperature(temperature)
    print(f"The average temperature is: {average_temperature:.2f}°C")
    print(f"The highest temperature is: {highest_temperature:.2f}°C")
    print(f"The lowest temperature is: {lowest_temperature:.2f}°C")
    print(f"The average temperature in Fahrenheit is: {convert_to_fahrenheit(average_temperature):.2f}°F")
    print(f"The number of days the temperature exceeded 20°C is: {calculate_number_of_days_temperature_exceeded(temperature)}")

