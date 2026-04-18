# This program chooses 7 dinners for the week
# 1 of the dinners can feed more than 2 people. 

import random 
import csv

def calculate_weight(food):
    if food["rating"] != '' and food["times_eaten"] != '': 
        return ((float(food["rating"]) + 1) ** 2) / (float(food["times_eaten"]) + 1)
    return 100

def pick_food(foods: dict):
    food_for_the_week = []
    while len(food_for_the_week) < 7:
        choices = random.choices(list(foods.keys()), weights=list(foods.values()), k=7)
        [food_for_the_week.append(choice) for choice in choices if choice not in food_for_the_week and len(food_for_the_week) < 7]
    return food_for_the_week
    

def main(): 
    food_options = {}
    with open('food_options.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            weight = calculate_weight(row)
            row = {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}
            food_options[row["name"]] = weight
    [print(f"{food}") for food in pick_food(food_options)]


main()