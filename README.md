# Command Line Calorie Tracker
A command line tool for tracking and saving your daily calorie intake written in Python.

## Set Up
There are 3 things that must be modified in 'calories.py'. 
1. The 'FOODS' dictionary must be filled out so that the key is a one word string representing a food item and the value is the number of calories. The calories should be the approximate number of calories per cup of that food, except for foods you want to measure in discrete numbers, such as number of bananas. See 'UNITS' list to see available units. The 'none' unit is used for the food items that will be measured in discrete numbers. Additional units can be added, but a conversion function must be written, and a case for that unit must be added to the 'add' command.
2. The 'PATH_TO_CALS' variable must be set to the file path of wherever you want to store the temporary file containing the current daily calorie information. This should be a '.txt' file.
3. The 'PATH_TO_SAVE' variable must be set to the file path of wherever you want to store the saved daily calorie files. The 'dump' command will copy the current calorie file to this path with the title being the current date, then it will clear the contents of the current calorie file.

## Usage
It is recommended you set an alias for running the Python file. This will allow you to run the program from any directory. It is important that the alias allows for arguments so that the program runs without errors. Here is an example using Windows Powershell. Replace 'PATH_TO_CALORIES' with the path to the calories.py file, and 'cal' with whatever alias you want to use.

```
function Run-Calories {
		python PATH_TO_CALORIES\calories.py $args
	}

Set-Alias cal Run-Calories
```

Type ```h``` or ```help``` to see a list of available commands. The output of this is shown below:

  - init/clear: Clears the contents of the calories file. Use this at the start of each day.
  - add *food *amount *unit: Adds the given amount of food to your calories file. Use none for the unit if there is no applicable unit for it.
  - print: Show the current contents of the calories file and the total calories.
  - total: Prints the current calorie total of the calories file.
  - dump: Saves the current contents of the calories file (and the total calories) to the location specified in the code with the title being the current date. This action will delete the conetents of the calories file when it is finished.
  - avg: Prints the average daily calories from all of the saved calorie files.
