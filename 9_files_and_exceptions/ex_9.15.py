# ex_9.15: working with CSV Datasets Using the csv Module
import csv

with open('TitanicSurvival.csv', 'r', newline='') as titanic:
    # create a DictReader object
    reader = csv.DictReader(titanic)

    # Extract and convert ages, filtering out invalid entries
    ages = [float(row['age']) for row in reader if row['age']]

    if ages:
        average = sum(ages) / len(ages)
        print(f"Average age: {average:.2f}")
    else:
        print("Not valid data found")