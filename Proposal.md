#  IT PROFESSIONAL SALARIES - 2022

**Author**: Sravika Sailada

**Date**: 11/27/2022

**Reviewer**: Sai Dheeraj Kistapuram


## Motivation 

* The Dataset which we have chosen is based on the explanation about the 
  companies which offers different salaries on different positions.  
  This dataset is helpful for those who pursued their higher studies and 
  planning to take up a job in IT field with in different major of these 
  particular companies and the amount of the salaries they offer. 
* This help the students to choose the company wisely based on their preferred roles. 
  This dataset also helps the students who want to take up their internships with 
  high pay compared to other company.

## Investigative Questions

1) List of job roles with an employment status for each city in the dataset.
2) Count of employment status (Full Time, Contractor, Intern) in a particular city.
3) List of job roles that fall between the given salary range of a city.


## Approach 

- Brief description of the data set the project will investigate (including source, size, organization, who contributed the data set, date of the most recent update)
- What kind of transformations and data structures you envision you will be using in carrying out the project work.
Do not use vague statements. Credit is earned for being specific, precise, clear, and well-organized.}
* The Dataset which I was taken is based on the details of the various company which offers the salaries based on the positions in IT  in different locations. I have taken these data form the source called Kaggle it is an online website where we can find multiple numbers of the datasets. Kaggle is a subsidiary of Google LLC. The data which I have taken consist of 22774 * ROWS and 6 * COLUMN. In which I am planning to take 254 * ROWS and 4  * COLUMN by sorting out based on the high pay on each role. This dataset was contributed by 
 **SOURAV BANERJEE** , and it was last updated 4 months ago.
* [Salary, Location, Employment Status , Job Role] using the list we can implement the data for each role. We can also implement distinct salary and the roles using dictionary, where role is the key , salary is the value. 
* We can also get the data by city where the respective roles are being paid high. Where city is key and list as a value where the list consist of role and salary

## Expected Results

* Attributes Used: [Location, Job Role, Salary, Employment Status]
* For the first investigative question, the output will be dictionary where the
  Location will be the key and the value is another dictionary with Status as 
  key and list of job roles as values.
  Dictionary1 = {Location: {Status: [List of Job Roles]}}
* For the second investigative question, the output will be dictionary where the
  Status will be the key and the value is the count.
  Dictionary2 = {Status1: #count, Status2: #count, Status3: #count}
* For the third investigative question, the output will be a list which consists
  of job roles that range between the given salary input of a city.

## New Python Packages or Modules 

* We need to import `csv` for the output file, for testcases we use `unittest`
  and also the `os` package for interacting with the operating system.

## Dataset Documentation

* https://www.kaggle.com/code/iamsouravbanerjee/software-professional-salaries/notebook 
* Using the above dataset we can build the methods we require for the questions that are mentioned above.
