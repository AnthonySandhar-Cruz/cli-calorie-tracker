import numpy as np
import sys
import shutil
from datetime import date
import os


def tbsp_to_cups(tbsp):
    return tbsp*0.0625


def tsp_to_cups(tsp):
    return tsp*0.0208


def ml_to_cups(ml):
    return ml*0.00423


def l_to_cups(l):
    return l*4.227


def find_total():
    try:
        food, quantity, units = np.loadtxt('C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt',
                                           skiprows=2,
                                           unpack=True,
                                           delimiter=',',
                                           dtype=str)
        total = 0
        for i in range(len(food)):
            quant = float(quantity[i])
            if food[i].lower() in FOODS and units[i].lower() in UNITS:
                match units[i].lower():
                    case 'cups':
                        total += FOODS[food[i]]*quant
                    case 'none':
                        total += FOODS[food[i]]*quant
                    case 'ml':
                        quantity = ml_to_cups(quant)
                        total += FOODS[food[i]]*quant
                    case 'l':
                        quantity = l_to_cups(quant)
                        total += FOODS[food[i]]*quant
                    case 'tsp':
                        quantity = tsp_to_cups(quant)
                        total += FOODS[food[i]]*quant
                    case 'tbsp':
                        quantity = tbsp_to_cups(quant)
                        total += FOODS[food[i]]*quant
            else:
                print('Invalid entry in calories file. Check file and retry.')
        return total
    except:
        print('Error finding total calories.')


FOODS = {'banana': 110, 'kiwi': 44, 'nuts': 600, 'cheese': 451,
         'apple': 71, 'coffee': 50, 'eggs': 91, 'honey': 924,
         'pb': 1386, 'ramen': 460, 'rice': 640, 'dates': 66.5,
         'cabbage': 17, 'onion': 46, 'pasta': 387.5, 'sauce': 80,
         'vgb': 133.3, 'salad': 150, 'cucumber': 45}
UNITS = ['ml', 'l', 'tsp', 'tbsp', 'cups', 'none']

if sys.argv[1] == 'clear' or sys.argv[1] == 'init':
    try:
        with open('C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt', 'w') as calories:
            calories.write(f'Date: {date.today()}\n')
            calories.write('Food,Quantity,Units\n')
    except:
        print('Error clearing calories file.')
elif sys.argv[1] == 'dump':
    try:
        with open('C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt', 'a') as calories:
            calories.write(f'Total Calories:\n{find_total()}')
        source = 'C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt'
        destination = f'C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\days\\{date.today()}.txt'
        shutil.copy(source, destination)
        with open('C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt', 'w') as calories:
            calories.write(f'Date: {date.today()}\n')
            calories.write('Food,Quantity,Units\n')
    except:
        print('Error dumping contents of calories file.')
elif sys.argv[1] == 'add':
    try:
        if sys.argv[2].lower() in FOODS:
            with open('C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt', 'a') as calories:
                calories.write(f'{sys.argv[2]},{sys.argv[3]},{sys.argv[4]}\n')
        else:
            print('Please add food to dictionary.')
    except:
        print('Error adding food to calories file.')
elif sys.argv[1] == 'total':
    print(find_total())
elif sys.argv[1] == 'print':
    try:
        with open('C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\calories.txt', 'r') as calories:
            print(calories.read())
            print(f'Total calories: {find_total()}')
    except:
        print('Error printing contents of calories file.')
elif sys.argv[1] == 'avg':
    try:
        dir = "C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\days\\"
        total_cals = 0.0
        total_days = 0.0
        for fname in os.listdir(dir):
            fpath = os.path.join(dir, fname)
            with open(fpath, 'r') as f:
                total_days += 1.0
                total_cals += float(f.readlines()[-1].strip())
        print(f'Average Calories: {total_cals/total_days}')
    except:
        print('Error calculating average calorie consumption.')
elif sys.argv[1] == 'h' or sys.argv[1].lower() == 'help':
    print('Usage:')
    print('- init/clear: Clears the contents of the calories file. Use this at the start of each day.')
    print('- add food amount unit: Adds the given amount of food to your calories file. Use none for the unit if there is no applicable unit for it.')
    print('- print: Show the current contents of the calories file and the total calories.')
    print('- total: Prints the current calorie total of the calories file.')
    print('- dump: Saves the current contents of the calories file (and the total calories) to the location specified in the code with the title being the current date. This action will delete the conetents of the calories file when it is finished.')
    print('- avg: Prints the average daily calories from all of the saved calorie files.')
else:
    print('Invalid command.')
