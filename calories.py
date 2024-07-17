import numpy as np
import sys
import shutil
from datetime import date
import os
import xlsxwriter
import json


def tbsp_to_cups(tbsp):
    return tbsp*0.0625


def tsp_to_cups(tsp):
    return tsp*0.0208


def ml_to_cups(ml):
    return ml*0.00423


def l_to_cups(l):
    return l*4.227


def find_macros(quant, food):
    cals = float(FOODS[food]["Calories"])*quant
    protein = float(FOODS[food]["Protein"])*quant
    fat = float(FOODS[food]["Fat"])*quant
    carbs = float(FOODS[food]["Carbs"])*quant
    sugar = float(FOODS[food]["Sugar"])*quant
    return [cals, protein, fat, carbs, sugar]


def find_total():
    try:
        food, quantity, units = np.loadtxt(CALS_TMP,
                                           skiprows=2,
                                           unpack=True,
                                           delimiter=',',
                                           dtype=str)
        total_cals = 0
        total_protein = 0
        total_fat = 0
        total_carbs = 0
        total_sugar = 0
        for i in range(len(food)):
            quant = float(quantity[i])
            if food[i] in FOODS and units[i].lower() in UNITS:
                match units[i].lower():
                    case 'cups':
                        macros = find_macros(quant, food[i])
                        total_cals += macros[0]
                        total_protein += macros[1]
                        total_fat += macros[2]
                        total_carbs += macros[3]
                        total_sugar += macros[4]
                    case 'none':
                        macros = find_macros(quant, food[i])
                        total_cals += macros[0]
                        total_protein += macros[1]
                        total_fat += macros[2]
                        total_carbs += macros[3]
                        total_sugar += macros[4]
                    case 'ml':
                        quantity = ml_to_cups(quant)
                        macros = find_macros(quantity, food[i])
                        total_cals += macros[0]
                        total_protein += macros[1]
                        total_fat += macros[2]
                        total_carbs += macros[3]
                        total_sugar += macros[4]
                    case 'l':
                        quantity = l_to_cups(quant)
                        macros = find_macros(quantity, food[i])
                        total_cals += macros[0]
                        total_protein += macros[1]
                        total_fat += macros[2]
                        total_carbs += macros[3]
                        total_sugar += macros[4]
                    case 'tsp':
                        quantity = tsp_to_cups(quant)
                        macros = find_macros(quantity, food[i])
                        total_cals += macros[0]
                        total_protein += macros[1]
                        total_fat += macros[2]
                        total_carbs += macros[3]
                        total_sugar += macros[4]
                    case 'tbsp':
                        quantity = tbsp_to_cups(quant)
                        macros = find_macros(quantity, food[i])
                        total_cals += macros[0]
                        total_protein += macros[1]
                        total_fat += macros[2]
                        total_carbs += macros[3]
                        total_sugar += macros[4]
            else:
                print('Invalid entry in calories file. Check file and retry.')
        return [round(total_cals, 2), round(total_protein, 2), round(total_fat, 2), round(total_carbs, 2), round(total_sugar, 2)]
    except:
        print('Error finding total calories.')


FOODS = json.load(open('foods.json', 'r'))
UNITS = ['ml', 'l', 'tsp', 'tbsp', 'cups', 'none']
SAVE_DIR = 'days/'
CALS_TMP = 'calories.txt'

if sys.argv[1] == 'clear' or sys.argv[1] == 'init':
    try:
        with open(CALS_TMP, 'w') as calories:
            calories.write(f'Date: {date.today()}\n')
            calories.write('Food,Quantity,Units\n')
    except:
        print('Error clearing calories file.')
elif sys.argv[1] == 'dump':
    try:
        with open(CALS_TMP, 'a') as calories:
            total = find_total()
            calories.write(f'Total Calories,Total Protein,Total Fat,Total Carbs,Total Sugar\n{total[0]},{total[1]},{total[2]},{total[3]},{total[4]}')
        source = CALS_TMP
        destination = f'{SAVE_DIR}{date.today()}.txt'
        shutil.copy(source, destination)
    except:
        print('Error dumping contents of calories file.')
elif sys.argv[1] == 'add':
    try:
        if sys.argv[2].lower() in FOODS:
            with open(CALS_TMP, 'a') as calories:
                calories.write(f'{sys.argv[2]},{sys.argv[3]},{sys.argv[4]}\n')
        else:
            print('Please add food to dictionary.')
    except:
        print('Error adding food to calories file.')
elif sys.argv[1] == 'total':
    total = find_total()
    print(f'Total Calories: {total[0]}\nTotal Protein: {total[1]}\nTotal Fat: {total[2]}\nTotal Carbs: {total[3]}\nTotal Sugar: {total[4]}')
elif sys.argv[1] == 'print':
    try:
        with open(CALS_TMP, 'r') as calories:
            print(calories.read())
            total = find_total()
        print(f'Total Calories: {total[0]}\nTotal Protein: {total[1]}\nTotal Fat: {total[2]}\nTotal Carbs: {total[3]}\nTotal Sugar: {total[4]}')
    except:
        print('Error printing contents of calories file.')
elif sys.argv[1] == 'avg':
    try:
        total_cals = 0.0
        total_protein = 0.0
        total_fat = 0.0
        total_carbs = 0.0
        total_sugar = 0.0
        total_days = 0.0
        for fname in os.listdir(SAVE_DIR):
            fpath = os.path.join(SAVE_DIR, fname)
            with open(fpath, 'r') as f:
                macros = list(f.readlines()[-1].strip().split(','))
                total_days += 1.0
                total_cals += float(macros[0])
                total_protein += float(macros[1])
                total_fat += float(macros[2])
                total_carbs += float(macros[3])
                total_sugar += float(macros[4])
        print(f'Average Calories: {round(total_cals/total_days, 2)}\nAverage Protein: {round(total_protein/total_days, 2)}\nAverage Fat: {round(total_fat/total_days, 2)}\nAverage Carbs: {round(total_carbs/total_days, 2)}\nAverage Sugar: {round(total_sugar/total_days, 2)}')
    except:
        print('Error calculating average calorie consumption.')
elif sys.argv[1] == 'sheet':
    workbook = xlsxwriter.Workbook(f'{SAVE_DIR}calories_spreadsheet.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True, 'center_across': True, 'border': True, 'valign': 'vcenter', 'bg_color': '#0000FF', 'font_color': '#FFFFFF'})
    wrap1 = workbook.add_format({'text_wrap': True, 'center_across': True, 'border': True, 'valign': 'vcenter', 'bg_color': '#D9D9D9', 'font_color': '#000000'})
    wrap2 = workbook.add_format({'text_wrap': True, 'center_across': True, 'border': True, 'valign': 'vcenter', 'bg_color': '#E6E6E6', 'font_color': '#000000'})
    worksheet.write('A1', 'Date', bold)
    worksheet.write('B1', 'Food: (name:quantity:unit)', bold)
    worksheet.write('C1', 'Total Calories', bold)
    worksheet.write('D1', 'Total Protein', bold)
    worksheet.write('E1', 'Total Fat', bold)
    worksheet.write('F1', 'Total Carbs', bold)
    worksheet.write('G1', 'Total Sugar', bold)
    row = 1
    for fname in os.listdir(SAVE_DIR):
        fpath = os.path.join(SAVE_DIR, fname)
        food, quantity, units = np.loadtxt(fpath,
                                           skiprows=2,
                                           unpack=True,
                                           delimiter=',',
                                           dtype=str,
                                           usecols=(0, 1, 2))
        col2 = [[food[i], quantity[i], units[i]] for i in range(len(food)-2)]
        col2_str = ""
        for i in range(len(col2)):
            col2_str += f'{col2[i][0]}:{col2[i][1]}:{col2[i][2]} - '
        with open(fpath, 'r') as f:
            macros = list(f.readlines()[-1].strip().split(','))
        if row % 2 == 0:
            wrap = wrap1
        else:
            wrap = wrap2
        worksheet.write(row, 0, fname[:-4], wrap)
        worksheet.write(row, 1, col2_str, wrap)
        worksheet.write(row, 2, float(macros[0]), wrap)
        worksheet.write(row, 3, float(macros[1]), wrap)
        worksheet.write(row, 4, float(macros[2]), wrap)
        worksheet.write(row, 5, float(macros[3]), wrap)
        worksheet.write(row, 6, float(macros[4]), wrap)
        row += 1
    workbook.close()
elif sys.argv[1] == 'h' or sys.argv[1].lower() == 'help':
    print('Usage:')
    print('- init/clear: Clears the contents of the calories file. Use this at the start of each day.')
    print('- add food amount unit: Adds the given amount of food to your calories file. Use none for the unit if there is no applicable unit for it.')
    print('- print: Show the current contents of the calories file and the total calories.')
    print('- total: Prints the current calorie total of the calories file.')
    print('- dump: Saves the current contents of the calories file (and the total calories) to the location specified in the code with the title being the current date. This action will delete the conetents of the calories file when it is finished.')
    print('- avg: Prints the average daily calories from all of the saved calorie files.')
    print('- sheet: Creates a spreadsheet of all the saved calorie files.')
else:
    print('Invalid command.')
