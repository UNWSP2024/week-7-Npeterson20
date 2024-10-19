# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def rainfall():
    rainfall_data = []
    
    for month in range(1, 13):
        while True:
            try:
                rain = float(input(f"Enter the total rainfall for month {month}: "))
                rainfall_data.append(rain)
                break
            except ValueError:
                print("Please enter a valid number.")

    total_rainfall = sum(rainfall_data)
    average_rainfall = total_rainfall / 12
    highest_rainfall = max(rainfall_data)
    lowest_rainfall = min(rainfall_data)
    highest_month = rainfall_data.index(highest_rainfall) + 1
    lowest_month = rainfall_data.index(lowest_rainfall) + 1

    print(f"\nTotal rainfall for the year: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with highest rainfall: Month {highest_month} with {highest_rainfall:.2f} inches")
    print(f"Month with lowest rainfall: Month {lowest_month} with {lowest_rainfall:.2f} inches")

rainfall()
