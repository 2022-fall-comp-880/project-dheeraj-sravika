# COMP880-Final-Project

# Design Document

## Contributors: Sai Dheeraj Kistapuram & Sravika Sailada
## Date: 11/30/2022

## Packages to be imported: `unitest`, `csv`, `os`

## Classes: `init()` and `str()`

## Functions Used: 

### 1. def job_roles_by_status()

* This function will return the dictionary which consists of `location` as key 
  and the value is another dictionary with `status` as key and list of `job roles`
  as values.
* Input is taken from the csv file using file handling operations and the output
  is resulted into an empty dictionary.
* Consolidate all the job roles for a particular city by removing the duplicates
  and `append()` them into a list which is used a values again.
* Now using the above list as values to the employment status store them in a 
  temporary dictionary.
* Example - {Bangalore : {Full Time : [Web, Backend, Mobile, Database, Frontend, SDE, Testing, Android, IOS, Python]}}


### 2. def count_status()

* Input is taken as CSV file and output is in form of dictionary
* So, output is in form of dictionary so by initializing the empty_list()
* By taking city as input we will be getting the Employment status
* For example: By giving the input as Bangalore it gives the output with number count on number of interns , number of contractors, number of Full-time roles on that particular given city.
* Bangalore = {Full-Time: 24, Contractor: 0, Intern: 1}

### 3. def salary_range()

* We use this function for displaying the dictionary of job roles that has 
  given salary range.
* Using the **with** function start reading the input file by keyword **r**, 
  and also create an empty dictionary for storing the output.
* From the input file, search for the **salaries** and categorize them
  into ranges accordingly as 15-20k, 20-25k and so on.
* Using **salary ranges** as keys add them into the created dictionary and for
  the values use the corresponding salary ranges and append all the **job 
  roles** into a list and add them into the dictionary.
* If the input file has no data or missing salary values, do not take any
  action and just return empty dictionary.


