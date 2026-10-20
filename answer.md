***Q1. Sales employees**
'''python
print("The id of staff in the sales department:")
    for record in data["records"]:
        if record["department"].lower().strip() == "sales":
             print(record["employee_id"])
             print("========")
'''

# ***Answer**
'''
The id of staff in the sales department:
EMP-3001

# EMP-3006

# EMP-3011

# EMP-3016

# EMP-3021

# EMP-3026

# EMP-3031

# EMP-3036

# EMP-3041

# EMP-3046

# EMP-3051

# EMP-3056

# EMP-3061

# EMP-3066

# EMP-3071

# EMP-3076

# EMP-3081

# EMP-3086

'''

**How I got there:**   
i used a for loop to iterate over the records in data,then in those records i searched for sales department and i used a print function to display the employee_id of employees in sales department.  
'''

**Q2. List all Active employees.**
'''python
print()
    print("The id of all active staff:")
    for record in data["records"]:
        if record["status"].lower().strip() == "active":
            print(record["employee_id"])
'''
***Answer**
'''
The id of all active staff:
EMP-3001
EMP-3002
EMP-3003
EMP-3004
EMP-3005
EMP-3006
EMP-3007
EMP-3008
EMP-3009
EMP-3010
EMP-3011
EMP-3013
EMP-3014
EMP-3015
EMP-3016
EMP-3017
EMP-3018
EMP-3019
EMP-3020
EMP-3021
EMP-3022
EMP-3024
EMP-3025
EMP-3026
EMP-3027
EMP-3028
EMP-3029
EMP-3030
EMP-3031
EMP-3032
EMP-3033
EMP-3035
EMP-3036
EMP-3037
EMP-3038
EMP-3039
EMP-3040
EMP-3041
EMP-3042
EMP-3043
EMP-3044
EMP-3046
EMP-3047
EMP-3048
EMP-3049
EMP-3050
EMP-3051
EMP-3052
EMP-3053
EMP-3054
EMP-3055
EMP-3057
EMP-3058
EMP-3059
EMP-3060
EMP-3061
EMP-3062
EMP-3063
EMP-3064
EMP-3065
EMP-3066
EMP-3067
EMP-3068
EMP-3069
EMP-3070
EMP-3071
EMP-3072
EMP-3073
EMP-3074
EMP-3075
EMP-3076
EMP-3077
EMP-3078
EMP-3079
EMP-3080
EMP-3081
EMP-3082
EMP-3083
EMP-3084
EMP-3085
EMP-3086
EMP-3087
EMP-3088
EMP-3089
EMP-3090
'''

**How I got there:** 
i used a for loop to iterate over the records in data, then used a conditional statement 'if' to check for all active employees from the record data then displayed the active employees employee_id.

***Q3.How many employees are in each department**
'''python
    print()
    department_count = {}
    departments = set()
    for record in data["records"]:
        department = record["department"].lower().strip()
        departments.add(department)
        if department in department_count:
            department_count[department] += 1
         else:
           department_count[department] = 1

```
 print("Department counts:")
 for department, count in department_count.items():
     print(f"{department}: {count}")
```

'''

***Answer**
'''
sales: 18
delivery: 19
people ops: 18
engineering: 19
customer success: 18
'''

**How I got there:** 
So i created a dict named department_count and  a variable containing an empty set, then i used a for loop to iterate over the record data and saved the "department" in a variable named department and called method .add on it so if we have a department appearing more than once it would just add it once then group the selected department in a set.then i used 'if' to check if the departents are in the record data,then for every department with more than 1 employees it would add the total employees and display it under the department.

***Q4.How many are Active, Exited, Candidate, or blank?**
'''python
employees_with_blanc_status = 0
for record in data["records"]: 
    if record["status"] == "":  
        employees_with_blanc_status =  employees_with_blanc_status + 1
print("sum of employees with blanc status is/are")
print(employees_with_blanc_status)
print()

active_employees = 0
for record in data["records"]:
    if record["status"] == "Active":
        active_employees = active_employees + 1
print("sum of employees with active status is/are")
print(active_employees)
print()

exited_employees = 0 
for record in data["records"]:
    if record["status"] == "Exited":
        exited_employees = exited_employees + 1
print("sum of employees with exited status is/are")
print(exited_employees)
print()

candidates = 0 
for record in data["records"]:
    if record["status"] == "Candidate":
        candidates = candidates + 1
print("Total candidates is/are")
print(candidates)
'''
**How I got there:** 
i started by initializing counts for each status then i used the for loop to iterate over the record data and identified each employees status then saved each status and increased it based on how it occured in each eployees record. Then after getting total employees with different status then i added it together and displayed the sum.

***Q5.What distinct roles exist? Which department has which roles?**
''
    departmental_role = {}
    for record in data["records"]:
        department = record["department"].lower().strip()
        role = record["role"].lower().strip()
        if department in departmental_role:
            departmental_role[department].add(role)
        else:
            departmental_role[department] = {role}
    print(departmental_role)
'''

***Answer**
{'sales': {'associate'}, 'delivery': {'specialist', 'manager'}, 'people ops': {'specialist'}, 'engineering': {'analyst', 'lead'}, 'customer success': {'analyst'}}

**How I got there:** 
First i created a dict where i'll be saving the output. The looped through the records and created a variable for department and roles then used a conditional statement to check it the department is in the dict then if true then i used .add to add the role so it would be displayed together and if department has not be found or has no role, pick the department as key and add role to it as value.

***Q6.Which employees exited? Show their department and exit date.**
'''python
 for record in data["records"]:
        employee_id = record["employee_id"].lower().strip()
        status = record["status"].lower().strip()
        exit_date = record["exit_date"].lower().strip()
        if status == "Exited".lower().strip():
         print(employee_id,status,exit_date)  
'''
***Answer**
emp-3012 exited 2025-08-12
emp-3023 exited 2025-10-22
emp-3034 exited 2026-01-19
emp-3045 exited 2026-03-31
emp-3056 exited 2026-06-10
'''
**How I got there:** 
for this i looped through the entire records and created new variables for the key's i needed (status...) then i checked through the record and if employee status == exited i used the print function to display the employee_id,status and exit_date .

***Q7.Which department has had the most exits? Which has had none**
'''python
    department_exits = {}
    highest_count = 0
    highest_department = ""
    for record in data["records"]:
        department = record["department"].lower().strip()
        status = record["status"].lower().strip()
        if department not in department_exits:
            department_exits[department] = 0
        if status == "Exited".lower().strip():
            department_exits[department] += 1
    for department in department_exits:
        print(department, department_exits[department])
    for department in department_exits:
        if department_exits[department] > highest_count:
            highest_count = department_exits[department]
            highest_department = department
    print()
    print(f'Department with the most exits:', highest_department)
    print()
    print(f'Number of exits:', highest_count)
    print("Departments with no exits:")
    for department in department_exits:
        if department_exits[department] == 0:
            print(department, "has no exits")
'''
***Answer**
sales 1
delivery 1
people ops 1
engineering 1
customer success 1

Department with the most exits: sales
Number of exits: 1

Departments with no exits:
'''

**How I got there:** 
I used a dict called department_exits to count how many employees have exited each department, Then i looped through data["records"] to extract each employee's department and status, and i initialize new departments with a count of 0, and increases the count when the status is "exited".
To Display the counts I printed each department and its total number of employee exits.
To Find the most exits I used highest_count and highest_department to save the department with the largest number of exits.
To Find departments with no exits I checked the departments that have a count of 0 and prints their names.
'''
***Q8.For each employee with an offer, how many days between** `application_date` **and** `offer_accepted_date`**? Use** `datetime`
'''python

'''