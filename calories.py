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
        food, quantity, units = np.loadtxt('calories.txt',
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
         'pb': 1386, 'ramen': 460, 'rice': 640}
UNITS = ['ml', 'l', 'tsp', 'tbsp', 'cups', 'none']

if sys.argv[1] == 'clear' or sys.argv[1] == 'init':
    try:
        with open('calories.txt', 'w') as calories:
            calories.write(f'Date: {date.today()}\n')
            calories.write('Food,Quantity,Units\n')
    except:
        print('Error clearing calories file.')
elif sys.argv[1] == 'dump':
    try:
        with open('calories.txt', 'a') as calories:
            calories.write(f'Total Calories:\n{find_total()}')
        source = 'calories.txt'
        destination = f'C:\\Users\\antho\\OneDrive\\Documents\\coding\\py\\calories\\days\\{date.today()}.txt'
        shutil.copy(source, destination)
    except:
        print('Error dumping contents of calories file.')
elif sys.argv[1] == 'add':
    try:
        if sys.argv[2].lower() in FOODS:
            with open('calories.txt', 'a') as calories:
                calories.write(f'{sys.argv[2]},{sys.argv[3]},{sys.argv[4]}\n')
        else:
            print('Please add food to dictionary.')
    except:
        print('Error adding food to calories file.')
elif sys.argv[1] == 'total':
    print(find_total())
elif sys.argv[1] == 'print':
    try:
        with open('calories.txt', 'r') as calories:
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
else:
    print('Invalid command.')
