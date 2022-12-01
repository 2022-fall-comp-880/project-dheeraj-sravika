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

### 3. def salary_range()


