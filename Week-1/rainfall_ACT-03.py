# Week-1 Activity 3: Rainfall Statistics

# Questions:
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())


import numpy as np

def rainfall_statistics(rainfall_data):
    rainfall_array = np.array(rainfall_data)
    total_rainfall = np.sum(rainfall_array)
    average_rainfall = np.mean(rainfall_array)
    percentile_75 = np.percentile(rainfall_array, 75)
    count_rainfall = np.sum(rainfall_array == 0.0)
    countbig_rainfall = np.sum(rainfall_array > 5.0)
    return rainfall_array,average_rainfall, percentile_75, total_rainfall, count_rainfall, countbig_rainfall

def main():
    rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

    rainfall_array, average_rainfall, percentile_75, total_rainfall, count_rainfall, countbig_rainfall = rainfall_statistics(rainfall)


    print("Rainfall Statistics:", rainfall_array, "mm")
    print(f"Total Rainfall: {total_rainfall:.2f} mm")
    print(f"Average Rainfall: {average_rainfall:.2f} mm")
    print(f"Count of Days with No Rainfall: {count_rainfall} mm")
    print(f"Count of Days with Heavy Rainfall (> 5.0 mm): {countbig_rainfall} mm")
    print(f"75th Percentile Rainfall: {percentile_75:.2f} mm")


if __name__ == "__main__":
    main()