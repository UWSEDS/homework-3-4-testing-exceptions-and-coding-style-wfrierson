# Homework 3-4: Coding style and Unit tests.

##### Grade: 13/14  

-1: In test_dataframe.py - you are using the '|' operator, which is the bitwise or. In general, people don't often use this in boolean expressions that are similar to what you have in the assert statement. Consider using the operators 'or' and 'and'.   

------

**Note: This homework has a total of 14 points.**

In this homework, you will create two python modules and put them in PEP8 style.

1. Function code (5 points). Last week you wrote python codes that read an online file and created a data frame that has at least 3 columns. Now: (a) create a python module ``dataframe.py`` that reads the data in homework 2;  and (b) ``dataframpe.py`` should generate an ValueError execption if the dataframe doesn't have the expected column names.

1. Test code (5 points). Create a python file ``test_dataframe.py`` that has unit tests for dataframe.py. Include at least 2 of the following tests:

   - You have the expected columns.
   - Values in the column are all of the expected type.
   - There are no nan values.
   - The dataframe has at least one row.
   
1. Coding style (4 points). Make all codes PEP8 compliant and provide the output from pylint to demonstrate that you have accomplished this.
