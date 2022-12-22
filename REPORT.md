# Project Report

## CONTRIBUTORS: DHEERAJ & SRAVIKA SAILADA
## DATE: 12/21/2022


## 1. Purpose

Dataset used in the project is `Software Industry Salary Dataset - 2022`.

Dataset Source is from Kaggle: 
[Link to Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/software-professional-salaries-2022?select=Salary_Dataset_with_Extra_Features.csv)

Sourav Banerjee is the owner of the Dataset. Data has been collated from [Glassdoor](https://www.glassdoor.co.in/).

Dataset has been last updated on July 2022.


In this project we are going to investigate on three queries. For each of the 
queries we are going to write a class to provide an answer.


1. Count of Employment Status (Full Time, Contractor, Intern) in a particular city.

2. List of Job Roles that fall between the given salary range of a city.

3. List of Job Roles with an Employment Status for each city in the dataset.

## 2. Approach

- `main.py` file for reading dataset

The dataset is available in CSV format. First the CSV file has been read `csv` 
python module. Here each line of the CSV file will be stored as a list of lists 
and each element of that list will be an element of each line of the CSV file.

###  Count of Employment Status (Full Time, Contractor, Intern) in a particular city.

`Count` class contains `count()` method answers this query inside `status_count.py` file.

```
class Count:

    Attributes
    ----------
    dataset: List[List]
        Holds all the employees data read from the csv file
    city_name: str
        City Name
    
    Methods
    -------
    count(city_name) -> Dict
        Return counts of the number of employment status categories in the given city
```

Design

- Loop through all the employees dataset and count the employee status if the 
employee city is same as the one provided as an argument and add to the `output` dictionary.
- Once the all the players are looped return the `output`.

### List of Job Roles that fall between the given salary range of a city.

`Ranges` class contains `roles()` method answers this query inside `salary_range.py` file.

```
class Ranges:

    Attributes
    ----------
    dataset: List[List]
        Holds all the employees data read from the csv file
    city_name: str
        City Name
    low: int
        Lowest Salary range
    high: int
        Highest Salary range

    Methods
    -------
    roles(city_name, low, high) -> Set
        Returns set of all the Job Roles in the give city and salary range [low, high]
```

Design

- Loop through all the employees dataset and filter out employees whose city matches with `city_name` and employees salary lies between `low` and `high` and add employee's job role to the `output` set.
- Once the all the players are looped return the `output`.

### List of Job Roles with an Employment Status for each city in the dataset.

`EmployeeStatus` class contains `result()` method answers this query inside `employee_status.py` file.

```
class EmployeeStatus:

    Attributes
    ----------
    dataset: List[List]
        Holds all the employees data read from the csv file
    
    Methods
    -------
    result() -> Dict
        Return dictionary of the job roles for an employment status across all the cities
        where job roles are combined in a set and form keys for employement status.
```

Design

- Loop through the dataset and return a dictionary containing city as keys and 
a dictionary of status as keys, job roles as values.


## 3. Testing

`test` directory contains three test python files for respective three tasks.

### 3.1. `test_count.py`

Test cases for testing the `count()` method for class `Count` in task1 file. There are three test scenarios inside this test file.

#### 3.1.1 `test_valid_name`

This test scenario is when a valid city name has been given. As expected, it should return a dictionary of counts of the number of employment status categories.

- Call the `count()` method with the valid city name and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

#### 3.1.2 `test_empty_name`

This test scenario is when no city name has been given. As expected, it should return an empty dictionary.

- Call the `count()` method with no city name and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

#### 3.1.3 `test_wrong_name`

This test scenario is when wrong city name has been given. As expected, it should return an empty dictionary as the city name is not available in the dataset.

- Call the `count()` method with the given wrong city name and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

### 3.2. `test_ranges.py`

Test cases for testing the `roles()` method for class `JobRoles` in task2 file. 
There are three test scenarios inside this test file with salary range fixed 
across all the three scenarios.

#### 3.2.1 `test_valid_name`

This test scenario is when a valid city name has been given. As expected, it should return a set of Job Roles.

- Call the `roles()` method with the valid city name, fixed salary range and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

#### 3.2.2 `test_empty_name`

This test scenario is when no city name has been given. As expected, it should return an empty set.

- Call the `roles()` method with the valid city name, fixed salary range and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

#### 3.2.3 `test_wrong_name`

This test scenario is when wrong city name has been given. As expected, it should return an empty set as the city name is not available in the dataset.

- Call the `roles()` method with the valid city name, fixed salary range and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

### 3.3. `test_status.py`

Test cases for testing the `result()` method for class `EmployeeStatus` in task3 file. There are three test scenarios inside this test file.

#### 3.3.1 `test_multiple_entries`

This test scenario takes in `all.csv` file (full data). As expected, it should return a dictionary the job roles for an employment status across all the cities.

- Call the `result()` method and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

#### 3.3.2 `test_fifty_entries`

This test scenario takes in `fifty.csv` file (fifty records). As expected, it should return a dictionary the job roles for an employment status across all the cities.

- Call the `result()` method and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

#### 3.3.3 `test_ten_entries`

This test scenario takes in `ten.csv` file (ten records). As expected, it should return a dictionary the job roles for an employment status across all the cities.

- Call the `result()` method and store the result in `actual_result` variable.
- Compare the `actual_result` and `expected_result` with respective `assert` statement.

## 4. Results

```bash
# Output of the task 1. 
# Showing the counts of Job Status categories for the city: Hyderabad
Count of Job Roles at Hyderabad:  {'Full Time': 19, 'Intern': 6}


# Output of the task 2.
# Showing the Job Roles that fall between the given salary range of a city.
Job Roles at Hyderabad with salary range between 500000 and 1000000: 
{'SDE', 'Java', 'Testing', 'Android'}


# Output of the task 3. 
# Showing the job roles with an employment status for each city in the dataset.
{'Bangalore': {'Full Time': {'Web', 'Mobile', 'IOS', 'Frontend', 'Android', 'SDE', 'Python', 'Backend', 'Database', 'Testing'}, 'Intern': {'Frontend'}}, 'Chennai': {'Full Time': {'Frontend', 'Android', 'SDE', 'Java', 'Python'}, 'Intern': {'SDE', 'Python'}}, 'Hyderabad': {'Full Time': {'Frontend', 'Android', 'SDE', 'Java', 'Python', 'Backend', 'Testing'}, 'Intern': {'Android', 'Frontend', 'SDE', 'Java', 'Python'}}, 'Jaipur': {'Intern': {'SDE'}, 'Full Time': {'SDE'}}, 'Kerala': {'Full Time': {'SDE'}, 'Contractor': {'SDE'}}, 'Kolkata': {'Intern': {'SDE'}, 'Full Time': {'SDE'}}, 'Madhya Pradesh': {'Full Time': {'SDE'}, 'Intern': {'SDE'}}, 'Mumbai': {'Full Time': {'SDE'}, 'Contractor': {'SDE'}, 'Intern': {'SDE'}}, 'New Delhi': {'Full Time': {'IOS', 'Frontend', 'Android', 'SDE', 'Backend'}, 'Intern': {'SDE', 'Android'}}, 'Pune': {'Full Time': {'IOS', 'Android', 'Frontend', 'SDE', 'Backend'}, 'Intern': {'Frontend'}}}
```

## 5. Evaluation

### 5.1 What Works and Scope Assumptions

- All the three tasks works as expected even the dataset increases or decreases over the time.

- The project scope will not change once the stakeholders sign off on the scope statement.

- The solution was written in python and the methods were tested with multiple test scenarios.

- Project follows waterfall methodology.

### 5.2 Immediate Further Development

- The Job Roles task can be extended to get the job roles across all the cities instead of single city given as input. 

- Also in the Job Roles task we can fill the low and high arguments if they are not provided with lowest and highest salary in the dataset and return the results.
