In this project, you have to write a program that reads the grades of different people from a csv file and performs the following calculations on the grades and saves the resulting values in a file.

In this project, you have to implement 5 different tasks. The example of the source.py file that you should use for submission is at the bottom of the page (download file option). Click on this option to download the file.

 

Do not change the names of the functions in any way and implement all the codes you want to use in the same defs (do not put any code outside of the defs, except for importing the libraries and put them at the very beginning of the file) (to average only from Use the mean method (this method is imported from the statistics library in the file below.)) (none of the values should be rendered) (put all the libraries you intend to import only once at the beginning of the file and outside the defs and do not import in the def) and complete the corresponding function for each task and then make sure to extract this file with the name (source.py) and make sure it is zipped (not rar, just zip) and send it.

If you do not follow any of the above points, unfortunately, your score will be zero by the system.

Note: The online arbitration system uses Python 3.4, in this version the dictionaries do not remember the order of entering information and may not achieve the desired result if they are sorted, to solve this problem, use OrderedDict instead of dict. You can import this data structure from the collections library in the program.

 

1- calculate the average of each person and save it along with the name of each person, the output order of the names must be exactly equal to the order of the input file.

2- Save the rates in ascending order along with the name of each person. Please note that if you are using dict, the order of averages is not clear. Refer to this link for more information. https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries

3- Save the top three GPAs with each person's name.

4- Save the three low GPAs without each person's name.

5- Calculate and store the average grades.

Sample content of a csv file

Mandana, 5, 7, 3, 15
hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
sina, 19, 10, 19, 6, 8, 14, 3
sara, 0,5,20,14
soheila,13,2,5,1,3,10,12,4,13,17,7,7
Ali, 1, 9
sarvin,0,16,16,13,19,2,17,8

 

The output of the first task

Mandana, 7.5
Hamid, 6.066666666666666
sina, 11.285714285714286
Sarah, 9.75
Soheila, 7.833333333333333
Ali, 5.0
Sarvin, 11.375

 

The output of the second task

Ali, 5.0
Hamid, 6.066666666666666
Mandana, 7.5
Soheila, 7.833333333333333
Sarah, 9.75
sina, 11.285714285714286
Sarvin, 11.375

 

The output of the third task

Sarvin, 11.375
sina, 11.285714285714286
Sarah, 9.75

 

Fourth task output

5.0
6.066666666666666
7.5

 

Output of the fifth task

8.401530612244898

 

Note: Pay attention to this point in each step, if the GPA of several people is the same, the order of the output should be alphabetical, for example:

Hossein 16.5
Mona 16.5