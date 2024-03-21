# Command Line Calorie Tracker
A command line tool for tracking and saving your daily calorie intake written in Python.

## Set Up
There are 3 things that must be modified in 'calories.py'. 
1. The 'FOODS' dictionary must be filled out so that the key is a one word string representing a food item and the value is a list containing the nutritional information (see comment above FOODS definition for format). The information should be per cup of that food, except for foods you want to measure in discrete numbers, such as number of bananas. See 'UNITS' list to see available units. The 'none' unit is used for the food items that will be measured in discrete numbers. Additional units can be added, but a conversion function must be written, and a case for that unit must be added to the 'add' command.
2. The 'CALS_TMP' variable must be set to the file path of wherever you want to store the temporary file containing the current daily calorie information. This should be a '.txt' file.
3. The 'SAVE_DIR' variable must be set to the file path of wherever you want to store the saved daily calorie files. The 'dump' command will copy the current calorie file to this path with the title being the current date, then it will clear the contents of the current calorie file.

## Usage
It is recommended you set an alias for running the Python file. This will allow you to run the program from any directory. It is important that the alias allows for arguments so that the program runs without errors. Here is an example using Windows Powershell. Replace 'PATH_TO_CALS' with the path to the calories.py file, and 'cal' with whatever alias you want to use.

```powershell
function Run-Calories {
		python PATH_TO_CALS\calories.py $args
	}

Set-Alias cal Run-Calories
```

Add this to your Powershell profile by using the command ```notepad $PROFILE``` from Powershell. Replace 'notepad' with the text editor of your choice.

Type ```h``` or ```help``` to see a list of available commands. The output of this is shown below:

  - init OR clear: Clears the contents of the calories file. Use this at the start of each day. Make sure to use dump at the end of each day to save your progress so that this does not clear your unsaved progress.
  - add *food *amount *unit: Adds the given amount of food to your calories file. Use none for the unit if there is no applicable unit for it.
  - print: Show the current contents of the calories file and the total calories.
  - total: Prints the current calorie total of the calories file.
  - dump: Saves the current contents of the calories file (and the total calories) to the location specified in the code with the title being the current date. This action will delete the conetents of the calories file when it is finished.
  - avg: Prints the average daily calories from all of the saved calorie files.
  - sheet: Creates a spreadsheet of all the saved calorie files.

## Example
In this example, we will assume that the foods being added have already been added to the 'FOODS' dictionary with their associated number of calories. We will also assume an alias is set for running the file which is called 'cal'.

Here we will initialize the calories file and add our breakfast

```powershell
cal init
cal add banana 1 none
cal add coffee 1 none
cal add apple 1 none
cal add eggs 2 none
cal add potatoes 1 cups
cal add toast 2 none
cal add bacon 2 none
```

We can check the current total calories with

```powershell
cal total
```

This can be alternatively be done with ```print``` if you want to also see the contents of the calories file. Now let's say its the end of the day and you want to save today's calories file. Simply do

```
cal dump
```

This will copy the contents of the calories file to the directory specified by 'PATH_TO_SAVE' with the current date as the file name. Then you can repeat the process the next day.

