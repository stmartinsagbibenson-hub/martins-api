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

from datetime import datetimefor record in data["records"]:
    employee_id = record["employee_id"]
    application_date = record["application_date"]
    offer_accepted_date = record["offer_accepted_date"]
    if application_date and offer_accepted_date:
        application = datetime.strptime(application_date, "%Y-%m-%d")
        accepted = datetime.strptime(offer_accepted_date, "%Y-%m-%d")
        days_taken = (accepted - application).days
        print(f"Employee ID: {employee_id}")
        print(f"Days between application and offer acceptance: {days_taken} days")
        print()

'''
***Answer**
Employee ID: EMP-3001
Days between application and offer acceptance: 10 days

Employee ID: EMP-3002
Days between application and offer acceptance: 11 days

Employee ID: EMP-3003
Days between application and offer acceptance: 12 days

Employee ID: EMP-3004
Days between application and offer acceptance: 13 days

Employee ID: EMP-3005
Days between application and offer acceptance: 14 days

Employee ID: EMP-3006
Days between application and offer acceptance: 15 days

Employee ID: EMP-3007
Days between application and offer acceptance: 16 days

Employee ID: EMP-3008
Days between application and offer acceptance: 17 days

Employee ID: EMP-3009
Days between application and offer acceptance: 18 days

Employee ID: EMP-3010
Days between application and offer acceptance: 19 days

Employee ID: EMP-3011
Days between application and offer acceptance: 20 days

Employee ID: EMP-3012
Days between application and offer acceptance: 21 days

Employee ID: EMP-3013
Days between application and offer acceptance: 22 days

Employee ID: EMP-3014
Days between application and offer acceptance: 23 days

Employee ID: EMP-3015
Days between application and offer acceptance: 24 days

Employee ID: EMP-3016
Days between application and offer acceptance: 25 days

Employee ID: EMP-3017
Days between application and offer acceptance: 26 days

Employee ID: EMP-3018
Days between application and offer acceptance: 27 days

Employee ID: EMP-3019
Days between application and offer acceptance: 10 days

Employee ID: EMP-3020
Days between application and offer acceptance: 11 days

Employee ID: EMP-3021
Days between application and offer acceptance: 12 days

Employee ID: EMP-3022
Days between application and offer acceptance: 13 days

Employee ID: EMP-3023
Days between application and offer acceptance: 14 days

Employee ID: EMP-3024
Days between application and offer acceptance: 15 days

Employee ID: EMP-3025
Days between application and offer acceptance: 16 days

Employee ID: EMP-3026
Days between application and offer acceptance: 17 days

Employee ID: EMP-3027
Days between application and offer acceptance: 18 days

Employee ID: EMP-3028
Days between application and offer acceptance: 19 days

Employee ID: EMP-3029
Days between application and offer acceptance: 20 days

Employee ID: EMP-3030
Days between application and offer acceptance: 21 days

Employee ID: EMP-3031
Days between application and offer acceptance: 22 days

Employee ID: EMP-3032
Days between application and offer acceptance: 23 days

Employee ID: EMP-3033
Days between application and offer acceptance: 24 days

Employee ID: EMP-3034
Days between application and offer acceptance: 25 days

Employee ID: EMP-3035
Days between application and offer acceptance: 26 days

Employee ID: EMP-3036
Days between application and offer acceptance: 27 days

Employee ID: EMP-3037
Days between application and offer acceptance: 10 days

Employee ID: EMP-3038
Days between application and offer acceptance: 11 days

Employee ID: EMP-3039
Days between application and offer acceptance: 12 days

Employee ID: EMP-3040
Days between application and offer acceptance: 13 days

Employee ID: EMP-3041
Days between application and offer acceptance: 14 days

Employee ID: EMP-3042
Days between application and offer acceptance: 15 days

Employee ID: EMP-3043
Days between application and offer acceptance: 16 days

Employee ID: EMP-3044
Days between application and offer acceptance: 17 days

Employee ID: EMP-3045
Days between application and offer acceptance: 18 days

Employee ID: EMP-3046
Days between application and offer acceptance: 19 days

Employee ID: EMP-3047
Days between application and offer acceptance: 20 days

Employee ID: EMP-3048
Days between application and offer acceptance: 21 days

Employee ID: EMP-3049
Days between application and offer acceptance: 22 days

Employee ID: EMP-3050
Days between application and offer acceptance: 23 days

Employee ID: EMP-3051
Days between application and offer acceptance: 24 days

Employee ID: EMP-3052
Days between application and offer acceptance: 25 days

Employee ID: EMP-3053
Days between application and offer acceptance: 26 days

Employee ID: EMP-3054
Days between application and offer acceptance: 27 days

Employee ID: EMP-3055
Days between application and offer acceptance: 10 days

Employee ID: EMP-3056
Days between application and offer acceptance: 11 days

Employee ID: EMP-3057
Days between application and offer acceptance: 12 days

Employee ID: EMP-3058
Days between application and offer acceptance: 13 days

Employee ID: EMP-3059
Days between application and offer acceptance: 14 days

Employee ID: EMP-3060
Days between application and offer acceptance: 15 days

Employee ID: EMP-3061
Days between application and offer acceptance: 16 days

Employee ID: EMP-3062
Days between application and offer acceptance: 17 days

Employee ID: EMP-3063
Days between application and offer acceptance: 18 days

Employee ID: EMP-3064
Days between application and offer acceptance: 19 days

Employee ID: EMP-3065
Days between application and offer acceptance: 20 days

Employee ID: EMP-3066
Days between application and offer acceptance: 21 days

Employee ID: EMP-3067
Days between application and offer acceptance: 22 days

Employee ID: EMP-3068
Days between application and offer acceptance: 23 days

Employee ID: EMP-3069
Days between application and offer acceptance: 24 days

Employee ID: EMP-3070
Days between application and offer acceptance: 25 days

Employee ID: EMP-3071
Days between application and offer acceptance: 26 days

Employee ID: EMP-3072
Days between application and offer acceptance: 27 days

Employee ID: EMP-3073
Days between application and offer acceptance: 10 days

Employee ID: EMP-3074
Days between application and offer acceptance: 11 days

Employee ID: EMP-3075
Days between application and offer acceptance: 12 days

Employee ID: EMP-3076
Days between application and offer acceptance: 13 days

Employee ID: EMP-3077
Days between application and offer acceptance: 14 days

Employee ID: EMP-3078
Days between application and offer acceptance: 15 days

Employee ID: EMP-3079
Days between application and offer acceptance: 16 days

Employee ID: EMP-3080
Days between application and offer acceptance: 17 days

Employee ID: EMP-3081
Days between application and offer acceptance: 18 days

Employee ID: EMP-3082
Days between application and offer acceptance: 19 days

Employee ID: EMP-3083
Days between application and offer acceptance: 20 days

Employee ID: EMP-3084
Days between application and offer acceptance: 21 days

Employee ID: EMP-3085
Days between application and offer acceptance: 22 days

Employee ID: EMP-3086
Days between application and offer acceptance: 23 days

Employee ID: EMP-3087
Days between application and offer acceptance: 24 days

Employee ID: EMP-3088
Days between application and offer acceptance: 25 days

Employee ID: EMP-3089
Days between application and offer acceptance: 26 days

Employee ID: EMP-3090
Days between application and offer acceptance: 27 days

Employee ID: EMP-BAD-STATUS
Days between application and offer acceptance: 18 days

**How I got there:**
i imported datetime then looped through the record and created new variables to store the emp_id,application and offer_accepted_date then used a conditional statement to check for application and offer accepted date and i then stripped the date using strptime and saved it in new variables then calculated the days interval and displayed the emp_id and the num of days interval.


***Q.9 What is the **average time-to-offer** per department?**
'''python

from datetime import datetime

department_days = {}
department_count = {}
for record in data["records"]:
    department = record["department"].lower().strip()
    application_date = record["application_date"]
    offer_accepted_date = record["offer_accepted_date"]
    if application_date and offer_accepted_date:
        application = datetime.strptime(application_date, "%Y-%m-%d")
        accepted = datetime.strptime(offer_accepted_date, "%Y-%m-%d")
        days_taken = (accepted - application).days
        if department in department_days:
            department_days[department] += days_taken
            department_count[department] += 1
        else:
            department_days[department] = days_taken
            department_count[department] = 1

for department in department_days:
    average = department_days[department] / department_count[department]
    print(f"{department}: {average} days")
'''

***Answer**
sales: 18.5 days
delivery: 18.5 days
people ops: 18.5 days
engineering: 18.473684210526315 days


**How I got there:** 
i created two empty dict for the total number of days in each department and the second dict is for the count of employees in each department.then looped through the record and created 2 new variables to get and store department and application date then used an if condition to check for application and offer date. and stored them and calculated the days between the application and offer date then used an if condition t check for dapartment in the dict department_days and if it is there increase the employee count by 1  and the else creates new department and saves it incase it has not seen or recorded it before.then calculated the average in the for loop and displayed the result.

***Q10.What is the average days between `offer_accepted_date` and `start_date`?**
'''python
total_days = 0
employee_count = 0
for record in data["records"]:
    offer_accepted_date = record["offer_accepted_date"]
    start_date = record["start_date"]
    if offer_accepted_date and start_date:
        accepted = datetime.strptime(offer_accepted_date, "%Y-%m-%d")
        start = datetime.strptime(start_date, "%Y-%m-%d")
        days_taken = (start - accepted).days
        total_days += days_taken
        employee_count += 1
if employee_count > 0:
    average_days = total_days / employee_count
    print(f"Average days between offer acceptance and start date: {average_days} days")
else:
    print("None.")
'''

***Answer**
Average days between offer acceptance and start date: 11.472527472527473 days

**How I got there:** 
I initialize count for total days and employee count as 0 then looped through the record got the  offer_accepted_date and start_date and saved it then check for it again using conditional statement if tthen stripped it and saved it again then calculated the days between the  offer_accepted_date and start_date
by subtracting then  add the num of days taken by each employee to the total then increase the count for each employee the calculated the average and displayed the result.

***Q11.enure:for exited employees, how many days from `start_date` to `exit_date`? Who stayed the shortest?**
'''python
shortest_tenure = None
employee_with_shortest_tenure = None
for record in data["records"]:
    employee_id = record["employee_id"]
    start_date = record["start_date"]
    exit_date = record["exit_date"]
    if start_date and exit_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        exit_date = datetime.strptime(exit_date, "%Y-%m-%d")
        tenure = (exit_date - start).days
        if shortest_tenure is None:
            shortest_tenure = tenure
            employee_with_shortest_tenure = employee_id
        elif tenure < shortest_tenure:
            shortest_tenure = tenure
            employee_with_shortest_tenure = employee_id

print(f"Employee with shortest tenure: {employee_with_shortest_tenure}")
print(f"The shortest tenure is {shortest_tenure} days")
'''
***Answer**
Employee with shortest tenure: EMP-3012
The shortest tenure is 121 days

**How I got there:**
I initialize shortest tenure as none because i have not gotten the exact work days from any employee and the employee_with_shortest_tenure as none because ive not gotten any employee with short tenure then looped through the record and got the emp id start and exit date then saved it and used the if statement to check for the start and exit date then stripped it and saved it and used it in the calculation for tenure and then i used an if condition to check if there is nothing saved in shortest tenure the added the emp id with the shortest tenure and saved it then displayed the employee with shortest tenure and the number of days the emp worked for.

***Q12. How many people were hired (started) in each month? Which month was busiest?**
'''python
monthly_hires = {}
for record in data["records"]:
    start_date = record["start_date"]
    if start_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        month = start.strftime("%B")

        if month in monthly_hires:
            monthly_hires[month] += 1
        else:
            monthly_hires[month] = 1

for month, count in monthly_hires.items():
    print(f"{month}: {count}")

busiest_month = None
highest_count = 0

for month, count in monthly_hires.items():
    if count > highest_count:
        highest_count = count
        busiest_month = month

print(f"\nBusiest month: {busiest_month}")
print(f"Number of hires: {highest_count}")
'''

***Answer**
January: 6
February: 8
March: 8
April: 12
May: 12
June: 9
July: 8
August: 6
September: 7
October: 4
November: 4
December: 7

Busiest month: April
Number of hires: 12

**How I got there:**
I ceated a dict to save the number of hires per month then looped through the record and i used if statement to check for start date then  i got the start date and striped it and saved it then created another variable for month so i can saved the months i extracted in form of words using %B. then check the month in the dictionay and if found increase the hire count and if not recorded before save it and start counting from 1 and then used a for loop to select unique months using .items so it would just select one from each month and it would display a unique month and the total num of hires then it  would compare each month with others in the second for loop and it would dispay the answer.

***Q13. Which department is slowest to hire**? Defend your answer with numbers.**

slowest_department = None
highest_average = 0
for department in department_days:
    average = department_days[department] / department_count[department]
    if average > highest_average:
        highest_average = average
        slowest_department = department
print(f"Slowest department to hire: {slowest_department}")
print(f"Average time-to-offer: {highest_average} days")


***Answer**
Slowest department to hire: sales
Average time-to-offer: 18.5 days

**How I got there:**
i used the average i calculated before for this so i initialize slowest_dep as none because i have not recorded and departent yet then i also initialize highest_average as 0 then i looped through record then used the average formula  i used to calculate the average for all department then used an if condition to comapre then displayed the slowest department to hire and the average days.

***Q14 What is the **attrition rate** per department (exited ÷ total hired)? Is a small sample misleading here?**
'''python
department_hired = {}
department_exited = {}
for record in data["records"]:
    department = record["department"]
    if department in department_hired:
        department_hired[department] += 1
    else:
        department_hired[department] = 1
    if record["exit_date"]:
        if department in department_exited:
            department_exited[department] += 1
        else:
            department_exited[department] = 1
for department in department_hired:
    total_hired = department_hired[department]
    if department in department_exited:
        total_exited = department_exited[department]
    else:
        total_exited = 0
    attrition_rate = (total_exited / total_hired) * 100
    print(f"Department: {department}")
    print(f"Total hired: {total_hired}")
    print(f"Total exited: {total_exited}")
    print(f"Attrition rate: {attrition_rate:.2f}%")
    print()
'''

***Answer**
Department: Sales
Total hired: 18
Total exited: 1
Attrition rate: 5.56%

Department: Delivery
Total hired: 19
Total exited: 1
Attrition rate: 5.26%

Department: People Ops
Total hired: 18
Total exited: 1
Attrition rate: 5.56%

Department: Engineering
Total hired: 19
Total exited: 1
Attrition rate: 5.26%

Department: Customer Success
Total hired: 18
Total exited: 1
Attrition rate: 5.56%

**How I got there:**
i created a dict for then number of hired emp in each department and for the number of exited employes then i looped through record and extracted the departments in the record  and saved it as department then i used if condition check if the departments exists in the dict called department_hired and if it exixts the count will be increased and saved else it would save the department name and start counting from 1 the do the same thing for "exit_date" it would check and increse it if needed then for the attrition rate it would be in percentage so i used a for loop to loop through the department in department_exited and save the result  in a variable  named total hired and check use if to check for department in department_exited then saved the result in total exited then used the saved value to calculate the attritition rate for each department.then display the result.

***Q15.. How many employees were employed at some chosen date (started on or before it, not exited before it)?**
'''python
chosen_date = datetime.strptime("2025-06-30", "%Y-%m-%d")
total_employees = 0
for record in data["records"]:
    start_date = record["start_date"]
    exit_date = record["exit_date"]
    if start_date:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        if start <= chosen_date:
            if not exit_date:
                total_employees += 1
            else:
                exit = datetime.strptime(exit_date, "%Y-%m-%d")
                if exit >= chosen_date:
                    total_employees += 1

print(f"{total_employees} employees were employeed on {chosen_date.date()}")
'''

***Answer**
25 employees were employeed on 2025-06-30

**How I got there:**
i started by choosing a date randomly from the api records then i created a variable so i can sve the total employees later and initialized it as 0 because ive not found any empoyee for that date.Then used  a for loop to extract and save the start and exit date then used if condition to check for start date and stripped it and then started coparing the start date of all employees with the date i chose randonmly and for each employee that matches with the date it would save and count them or the else block will run and then the result will be displayed.


***Q16. Which records are invalid (missing dates, missing status, exit before start)? Write a function `is_valid(record)` and use it to clean the data.**
'''python
from function import is_valid
valid_records = []
invalid_records = []
for record in data["records"]:
    if is_valid(record):
        valid_records.append(record)
    else:
        invalid_records.append(record)

print("Valid records:", len(valid_records))
print("Invalid records:", len(invalid_records))

for record in invalid_records:
    print(record)
'''
***Answer**
Valid records: 90
Invalid records: 2
{'employee_id': 'EMP-MISS-OFFER', 'department': 'Delivery', 'role': 'Specialist', 'application_date': '2026-04-02', 'offer_accepted_date': '', 'start_date': '', 'exit_date': '', 'status': 'Candidate'}
{'employee_id': 'EMP-BAD-STATUS', 'department': 'Engineering', 'role': 'Analyst', 'application_date': '2026-05-12', 'offer_accepted_date': '2026-05-30', 'start_date': '2026-06-08', 'exit_date': '', 'status': ''}

**How I got there:**
first i opened a new file named function.py then i defined a function called is_valid and the function takes in the record so i called the function in api_analitics.py so ill be able to use it there so the i created two empty list for valid and invalid records then i used a for loop to loop through the record and used conditional statement if to check and save both the valid and invalid record by using .append to append the records to the empty list i created before then i called len on the list to give me the length of both valid and invalid record and displayed it then i used a for loop to check for the records i have in list of invalid_records the printed those records which will print the information about the eployee.




##TURN ANSWERS TO END POINT...
**1.| `GET /employees` | all clean records (optional `?department=` and `?status=` filters) |**
***Answer**
[
  {
    "employee_id": "EMP-3001",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-01-08",
    "offer_accepted_date": "2025-01-18",
    "start_date": "2025-01-25",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3002",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-01-14",
    "offer_accepted_date": "2025-01-25",
    "start_date": "2025-02-02",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3003",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-01-20",
    "offer_accepted_date": "2025-02-01",
    "start_date": "2025-02-10",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3004",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-01-26",
    "offer_accepted_date": "2025-02-08",
    "start_date": "2025-02-18",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3005",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-02-01",
    "offer_accepted_date": "2025-02-15",
    "start_date": "2025-02-26",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3006",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-02-07",
    "offer_accepted_date": "2025-02-22",
    "start_date": "2025-03-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3007",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-02-13",
    "offer_accepted_date": "2025-03-01",
    "start_date": "2025-03-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3008",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-02-19",
    "offer_accepted_date": "2025-03-08",
    "start_date": "2025-03-22",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3009",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-02-25",
    "offer_accepted_date": "2025-03-15",
    "start_date": "2025-03-30",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3010",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-03-03",
    "offer_accepted_date": "2025-03-22",
    "start_date": "2025-04-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3011",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-03-09",
    "offer_accepted_date": "2025-03-29",
    "start_date": "2025-04-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3012",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-03-15",
    "offer_accepted_date": "2025-04-05",
    "start_date": "2025-04-13",
    "exit_date": "2025-08-12",
    "status": "Exited"
  },
  {
    "employee_id": "EMP-3013",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-03-21",
    "offer_accepted_date": "2025-04-12",
    "start_date": "2025-04-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3014",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-03-27",
    "offer_accepted_date": "2025-04-19",
    "start_date": "2025-04-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3015",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-04-02",
    "offer_accepted_date": "2025-04-26",
    "start_date": "2025-05-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3016",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-04-08",
    "offer_accepted_date": "2025-05-03",
    "start_date": "2025-05-15",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3017",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-04-14",
    "offer_accepted_date": "2025-05-10",
    "start_date": "2025-05-23",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3018",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-04-20",
    "offer_accepted_date": "2025-05-17",
    "start_date": "2025-05-31",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3019",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-04-26",
    "offer_accepted_date": "2025-05-06",
    "start_date": "2025-05-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3020",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-05-02",
    "offer_accepted_date": "2025-05-13",
    "start_date": "2025-05-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3021",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-05-08",
    "offer_accepted_date": "2025-05-20",
    "start_date": "2025-05-27",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3022",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-05-14",
    "offer_accepted_date": "2025-05-27",
    "start_date": "2025-06-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3023",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-05-20",
    "offer_accepted_date": "2025-06-03",
    "start_date": "2025-06-12",
    "exit_date": "2025-10-22",
    "status": "Exited"
  },
  {
    "employee_id": "EMP-3024",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-05-26",
    "offer_accepted_date": "2025-06-10",
    "start_date": "2025-06-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3025",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-06-01",
    "offer_accepted_date": "2025-06-17",
    "start_date": "2025-06-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3026",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-06-07",
    "offer_accepted_date": "2025-06-24",
    "start_date": "2025-07-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3027",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-06-13",
    "offer_accepted_date": "2025-07-01",
    "start_date": "2025-07-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3028",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-06-19",
    "offer_accepted_date": "2025-07-08",
    "start_date": "2025-07-22",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3029",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-06-25",
    "offer_accepted_date": "2025-07-15",
    "start_date": "2025-07-30",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3030",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-07-01",
    "offer_accepted_date": "2025-07-22",
    "start_date": "2025-08-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3031",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-07-07",
    "offer_accepted_date": "2025-07-29",
    "start_date": "2025-08-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3032",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-07-13",
    "offer_accepted_date": "2025-08-05",
    "start_date": "2025-08-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3033",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-07-19",
    "offer_accepted_date": "2025-08-12",
    "start_date": "2025-08-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3034",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-07-25",
    "offer_accepted_date": "2025-08-19",
    "start_date": "2025-08-29",
    "exit_date": "2026-01-19",
    "status": "Exited"
  },
  {
    "employee_id": "EMP-3035",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-07-31",
    "offer_accepted_date": "2025-08-26",
    "start_date": "2025-09-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3036",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-08-06",
    "offer_accepted_date": "2025-09-02",
    "start_date": "2025-09-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3037",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-08-12",
    "offer_accepted_date": "2025-08-22",
    "start_date": "2025-09-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3038",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-08-18",
    "offer_accepted_date": "2025-08-29",
    "start_date": "2025-09-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3039",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-08-24",
    "offer_accepted_date": "2025-09-05",
    "start_date": "2025-09-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3040",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-08-30",
    "offer_accepted_date": "2025-09-12",
    "start_date": "2025-09-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3041",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-09-05",
    "offer_accepted_date": "2025-09-19",
    "start_date": "2025-09-26",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3042",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-09-11",
    "offer_accepted_date": "2025-09-26",
    "start_date": "2025-10-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3043",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-09-17",
    "offer_accepted_date": "2025-10-03",
    "start_date": "2025-10-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3044",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-09-23",
    "offer_accepted_date": "2025-10-10",
    "start_date": "2025-10-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3045",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-09-29",
    "offer_accepted_date": "2025-10-17",
    "start_date": "2025-10-28",
    "exit_date": "2026-03-31",
    "status": "Exited"
  },
  {
    "employee_id": "EMP-3046",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-10-05",
    "offer_accepted_date": "2025-10-24",
    "start_date": "2025-11-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3047",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-10-11",
    "offer_accepted_date": "2025-10-31",
    "start_date": "2025-11-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3048",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-10-17",
    "offer_accepted_date": "2025-11-07",
    "start_date": "2025-11-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3049",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-10-23",
    "offer_accepted_date": "2025-11-14",
    "start_date": "2025-11-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3050",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-10-29",
    "offer_accepted_date": "2025-11-21",
    "start_date": "2025-12-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3051",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-11-04",
    "offer_accepted_date": "2025-11-28",
    "start_date": "2025-12-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3052",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-11-10",
    "offer_accepted_date": "2025-12-05",
    "start_date": "2025-12-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3053",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-11-16",
    "offer_accepted_date": "2025-12-12",
    "start_date": "2025-12-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3054",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-11-22",
    "offer_accepted_date": "2025-12-19",
    "start_date": "2025-12-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3055",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-11-28",
    "offer_accepted_date": "2025-12-08",
    "start_date": "2025-12-19",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3056",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-12-04",
    "offer_accepted_date": "2025-12-15",
    "start_date": "2025-12-27",
    "exit_date": "2026-06-10",
    "status": "Exited"
  },
  {
    "employee_id": "EMP-3057",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-12-10",
    "offer_accepted_date": "2025-12-22",
    "start_date": "2026-01-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3058",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-12-16",
    "offer_accepted_date": "2025-12-29",
    "start_date": "2026-01-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3059",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-12-22",
    "offer_accepted_date": "2026-01-05",
    "start_date": "2026-01-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3060",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-12-28",
    "offer_accepted_date": "2026-01-12",
    "start_date": "2026-01-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3061",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-01-03",
    "offer_accepted_date": "2026-01-19",
    "start_date": "2026-01-26",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3062",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-01-09",
    "offer_accepted_date": "2026-01-26",
    "start_date": "2026-02-03",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3063",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-01-15",
    "offer_accepted_date": "2026-02-02",
    "start_date": "2026-02-11",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3064",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-01-21",
    "offer_accepted_date": "2026-02-09",
    "start_date": "2026-02-19",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3065",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-01-27",
    "offer_accepted_date": "2026-02-16",
    "start_date": "2026-02-27",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3066",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-02-02",
    "offer_accepted_date": "2026-02-23",
    "start_date": "2026-03-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3067",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-02-08",
    "offer_accepted_date": "2026-03-02",
    "start_date": "2026-03-15",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3068",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-02-14",
    "offer_accepted_date": "2026-03-09",
    "start_date": "2026-03-23",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3069",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-02-20",
    "offer_accepted_date": "2026-03-16",
    "start_date": "2026-03-31",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3070",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-02-26",
    "offer_accepted_date": "2026-03-23",
    "start_date": "2026-04-08",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3071",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-03-04",
    "offer_accepted_date": "2026-03-30",
    "start_date": "2026-04-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3072",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-03-10",
    "offer_accepted_date": "2026-04-06",
    "start_date": "2026-04-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3073",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-03-16",
    "offer_accepted_date": "2026-03-26",
    "start_date": "2026-04-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3074",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-03-22",
    "offer_accepted_date": "2026-04-02",
    "start_date": "2026-04-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3075",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-03-28",
    "offer_accepted_date": "2026-04-09",
    "start_date": "2026-04-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3076",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-04-03",
    "offer_accepted_date": "2026-04-16",
    "start_date": "2026-04-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3077",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-04-09",
    "offer_accepted_date": "2026-04-23",
    "start_date": "2026-05-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3078",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-04-15",
    "offer_accepted_date": "2026-04-30",
    "start_date": "2026-05-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3079",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-04-21",
    "offer_accepted_date": "2026-05-07",
    "start_date": "2026-05-22",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3080",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-04-27",
    "offer_accepted_date": "2026-05-14",
    "start_date": "2026-05-30",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3081",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-05-03",
    "offer_accepted_date": "2026-05-21",
    "start_date": "2026-05-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3082",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-05-09",
    "offer_accepted_date": "2026-05-28",
    "start_date": "2026-06-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3083",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-05-15",
    "offer_accepted_date": "2026-06-04",
    "start_date": "2026-06-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3084",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-05-21",
    "offer_accepted_date": "2026-06-11",
    "start_date": "2026-06-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3085",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-05-27",
    "offer_accepted_date": "2026-06-18",
    "start_date": "2026-06-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3086",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-06-02",
    "offer_accepted_date": "2026-06-25",
    "start_date": "2026-07-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3087",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-06-08",
    "offer_accepted_date": "2026-07-02",
    "start_date": "2026-07-15",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3088",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-06-14",
    "offer_accepted_date": "2026-07-09",
    "start_date": "2026-07-23",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3089",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-06-20",
    "offer_accepted_date": "2026-07-16",
    "start_date": "2026-07-31",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3090",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-06-26",
    "offer_accepted_date": "2026-07-23",
    "start_date": "2026-08-08",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-MISS-OFFER",
    "department": "Delivery",
    "role": "Specialist",
    "application_date": "2026-04-02",
    "offer_accepted_date": "",
    "start_date": "",
    "exit_date": "",
    "status": "Candidate"
  },
  {
    "employee_id": "EMP-BAD-STATUS",
    "department": "Engineering",
    "role": "Analyst",
    "application_date": "2026-05-12",
    "offer_accepted_date": "2026-05-30",
    "start_date": "2026-06-08",
    "exit_date": "",
    "status": ""
  }
]
***Response code is 200 ok **

***Q2.| `GET /employees/active` | only Active employees |**
***Answer**
[
  {
    "employee_id": "EMP-3001",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-01-08",
    "offer_accepted_date": "2025-01-18",
    "start_date": "2025-01-25",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3002",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-01-14",
    "offer_accepted_date": "2025-01-25",
    "start_date": "2025-02-02",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3003",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-01-20",
    "offer_accepted_date": "2025-02-01",
    "start_date": "2025-02-10",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3004",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-01-26",
    "offer_accepted_date": "2025-02-08",
    "start_date": "2025-02-18",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3005",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-02-01",
    "offer_accepted_date": "2025-02-15",
    "start_date": "2025-02-26",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3006",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-02-07",
    "offer_accepted_date": "2025-02-22",
    "start_date": "2025-03-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3007",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-02-13",
    "offer_accepted_date": "2025-03-01",
    "start_date": "2025-03-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3008",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-02-19",
    "offer_accepted_date": "2025-03-08",
    "start_date": "2025-03-22",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3009",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-02-25",
    "offer_accepted_date": "2025-03-15",
    "start_date": "2025-03-30",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3010",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-03-03",
    "offer_accepted_date": "2025-03-22",
    "start_date": "2025-04-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3011",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-03-09",
    "offer_accepted_date": "2025-03-29",
    "start_date": "2025-04-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3013",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-03-21",
    "offer_accepted_date": "2025-04-12",
    "start_date": "2025-04-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3014",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-03-27",
    "offer_accepted_date": "2025-04-19",
    "start_date": "2025-04-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3015",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-04-02",
    "offer_accepted_date": "2025-04-26",
    "start_date": "2025-05-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3016",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-04-08",
    "offer_accepted_date": "2025-05-03",
    "start_date": "2025-05-15",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3017",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-04-14",
    "offer_accepted_date": "2025-05-10",
    "start_date": "2025-05-23",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3018",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-04-20",
    "offer_accepted_date": "2025-05-17",
    "start_date": "2025-05-31",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3019",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-04-26",
    "offer_accepted_date": "2025-05-06",
    "start_date": "2025-05-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3020",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-05-02",
    "offer_accepted_date": "2025-05-13",
    "start_date": "2025-05-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3021",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-05-08",
    "offer_accepted_date": "2025-05-20",
    "start_date": "2025-05-27",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3022",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-05-14",
    "offer_accepted_date": "2025-05-27",
    "start_date": "2025-06-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3024",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-05-26",
    "offer_accepted_date": "2025-06-10",
    "start_date": "2025-06-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3025",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-06-01",
    "offer_accepted_date": "2025-06-17",
    "start_date": "2025-06-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3026",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-06-07",
    "offer_accepted_date": "2025-06-24",
    "start_date": "2025-07-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3027",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-06-13",
    "offer_accepted_date": "2025-07-01",
    "start_date": "2025-07-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3028",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-06-19",
    "offer_accepted_date": "2025-07-08",
    "start_date": "2025-07-22",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3029",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-06-25",
    "offer_accepted_date": "2025-07-15",
    "start_date": "2025-07-30",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3030",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-07-01",
    "offer_accepted_date": "2025-07-22",
    "start_date": "2025-08-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3031",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-07-07",
    "offer_accepted_date": "2025-07-29",
    "start_date": "2025-08-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3032",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-07-13",
    "offer_accepted_date": "2025-08-05",
    "start_date": "2025-08-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3033",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-07-19",
    "offer_accepted_date": "2025-08-12",
    "start_date": "2025-08-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3035",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-07-31",
    "offer_accepted_date": "2025-08-26",
    "start_date": "2025-09-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3036",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-08-06",
    "offer_accepted_date": "2025-09-02",
    "start_date": "2025-09-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3037",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-08-12",
    "offer_accepted_date": "2025-08-22",
    "start_date": "2025-09-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3038",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-08-18",
    "offer_accepted_date": "2025-08-29",
    "start_date": "2025-09-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3039",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-08-24",
    "offer_accepted_date": "2025-09-05",
    "start_date": "2025-09-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3040",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-08-30",
    "offer_accepted_date": "2025-09-12",
    "start_date": "2025-09-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3041",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-09-05",
    "offer_accepted_date": "2025-09-19",
    "start_date": "2025-09-26",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3042",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-09-11",
    "offer_accepted_date": "2025-09-26",
    "start_date": "2025-10-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3043",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-09-17",
    "offer_accepted_date": "2025-10-03",
    "start_date": "2025-10-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3044",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-09-23",
    "offer_accepted_date": "2025-10-10",
    "start_date": "2025-10-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3046",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-10-05",
    "offer_accepted_date": "2025-10-24",
    "start_date": "2025-11-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3047",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-10-11",
    "offer_accepted_date": "2025-10-31",
    "start_date": "2025-11-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3048",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-10-17",
    "offer_accepted_date": "2025-11-07",
    "start_date": "2025-11-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3049",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-10-23",
    "offer_accepted_date": "2025-11-14",
    "start_date": "2025-11-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3050",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-10-29",
    "offer_accepted_date": "2025-11-21",
    "start_date": "2025-12-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3051",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2025-11-04",
    "offer_accepted_date": "2025-11-28",
    "start_date": "2025-12-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3052",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-11-10",
    "offer_accepted_date": "2025-12-05",
    "start_date": "2025-12-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3053",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-11-16",
    "offer_accepted_date": "2025-12-12",
    "start_date": "2025-12-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3054",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-11-22",
    "offer_accepted_date": "2025-12-19",
    "start_date": "2025-12-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3055",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-11-28",
    "offer_accepted_date": "2025-12-08",
    "start_date": "2025-12-19",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3057",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2025-12-10",
    "offer_accepted_date": "2025-12-22",
    "start_date": "2026-01-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3058",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2025-12-16",
    "offer_accepted_date": "2025-12-29",
    "start_date": "2026-01-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3059",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2025-12-22",
    "offer_accepted_date": "2026-01-05",
    "start_date": "2026-01-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3060",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2025-12-28",
    "offer_accepted_date": "2026-01-12",
    "start_date": "2026-01-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3061",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-01-03",
    "offer_accepted_date": "2026-01-19",
    "start_date": "2026-01-26",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3062",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-01-09",
    "offer_accepted_date": "2026-01-26",
    "start_date": "2026-02-03",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3063",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-01-15",
    "offer_accepted_date": "2026-02-02",
    "start_date": "2026-02-11",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3064",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-01-21",
    "offer_accepted_date": "2026-02-09",
    "start_date": "2026-02-19",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3065",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-01-27",
    "offer_accepted_date": "2026-02-16",
    "start_date": "2026-02-27",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3066",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-02-02",
    "offer_accepted_date": "2026-02-23",
    "start_date": "2026-03-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3067",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-02-08",
    "offer_accepted_date": "2026-03-02",
    "start_date": "2026-03-15",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3068",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-02-14",
    "offer_accepted_date": "2026-03-09",
    "start_date": "2026-03-23",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3069",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-02-20",
    "offer_accepted_date": "2026-03-16",
    "start_date": "2026-03-31",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3070",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-02-26",
    "offer_accepted_date": "2026-03-23",
    "start_date": "2026-04-08",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3071",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-03-04",
    "offer_accepted_date": "2026-03-30",
    "start_date": "2026-04-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3072",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-03-10",
    "offer_accepted_date": "2026-04-06",
    "start_date": "2026-04-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3073",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-03-16",
    "offer_accepted_date": "2026-03-26",
    "start_date": "2026-04-04",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3074",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-03-22",
    "offer_accepted_date": "2026-04-02",
    "start_date": "2026-04-12",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3075",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-03-28",
    "offer_accepted_date": "2026-04-09",
    "start_date": "2026-04-20",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3076",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-04-03",
    "offer_accepted_date": "2026-04-16",
    "start_date": "2026-04-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3077",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-04-09",
    "offer_accepted_date": "2026-04-23",
    "start_date": "2026-05-06",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3078",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-04-15",
    "offer_accepted_date": "2026-04-30",
    "start_date": "2026-05-14",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3079",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-04-21",
    "offer_accepted_date": "2026-05-07",
    "start_date": "2026-05-22",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3080",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-04-27",
    "offer_accepted_date": "2026-05-14",
    "start_date": "2026-05-30",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3081",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-05-03",
    "offer_accepted_date": "2026-05-21",
    "start_date": "2026-05-28",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3082",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-05-09",
    "offer_accepted_date": "2026-05-28",
    "start_date": "2026-06-05",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3083",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-05-15",
    "offer_accepted_date": "2026-06-04",
    "start_date": "2026-06-13",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3084",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-05-21",
    "offer_accepted_date": "2026-06-11",
    "start_date": "2026-06-21",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3085",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-05-27",
    "offer_accepted_date": "2026-06-18",
    "start_date": "2026-06-29",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3086",
    "department": "Sales",
    "role": "Associate",
    "application_date": "2026-06-02",
    "offer_accepted_date": "2026-06-25",
    "start_date": "2026-07-07",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3087",
    "department": "Delivery",
    "role": "Manager",
    "application_date": "2026-06-08",
    "offer_accepted_date": "2026-07-02",
    "start_date": "2026-07-15",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3088",
    "department": "People Ops",
    "role": "Specialist",
    "application_date": "2026-06-14",
    "offer_accepted_date": "2026-07-09",
    "start_date": "2026-07-23",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3089",
    "department": "Engineering",
    "role": "Lead",
    "application_date": "2026-06-20",
    "offer_accepted_date": "2026-07-16",
    "start_date": "2026-07-31",
    "exit_date": "",
    "status": "Active"
  },
  {
    "employee_id": "EMP-3090",
    "department": "Customer Success",
    "role": "Analyst",
    "application_date": "2026-06-26",
    "offer_accepted_date": "2026-07-23",
    "start_date": "2026-08-08",
    "exit_date": "",
    "status": "Active"
  }
]
***Response code is 200 ok **

***Q3| `GET /departments/{name}/employees` | employees in one department (e.g. Sales) |**
***Answer**
An empty list 

***Response** is 404 Error




***Q4.| `GET /stats/headcount` | count per department |**
***Answer**
  {
    "sales": 18,
    "delivery": 19,
    "people ops": 18,
    "engineering": 19,
    "customer success": 18
  },
***Response code is 200 ok **


***Q5.| `GET /stats/status-summary` | count by status**
***Answer**
{
  "blanc": 1,
  "Active": 85,
  "Exited": 5,
  "Candidate": 1
}
***Response code is 200 ok **


***Q6.`GET /stats/exits` | exited employees with tenure in days |**
***Answer**
[
  {
    "employee_id": "EMP-3012",
    "tenure_days": 121
  },
  {
    "employee_id": "EMP-3023",
    "tenure_days": 132
  },
  {
    "employee_id": "EMP-3034",
    "tenure_days": 143
  },
  {
    "employee_id": "EMP-3045",
    "tenure_days": 154
  },
  {
    "employee_id": "EMP-3056",
    "tenure_days": 165
  }
]
***Response code is 200 ok **

***Q7.| `GET /stats/time-to-offer` | average days to offer, per department |**
**Answer**
{
  "sales": 18.5,
  "delivery": 18.5,
  "people ops": 18.5,
  "engineering": 18.473684210526315,
  "customer success": 18.5
}

***Response code is 200 ok **

***Q8.GET /stats/hiring-by-month` | hires per month |**
**Answer**
{
  "January": 6,
  "February": 8,
  "March": 8,
  "April": 12,
  "May": 12,
  "June": 9,
  "July": 8,
  "August": 6,
  "September": 7,
  "October": 4,
  "November": 4,
  "December": 7
}

***Response code is 200 ok **

***Q9.| `GET /data-quality` | the invalid records and why they are invalid |**
**Answer**
{
  "valid_records": [
    {
      "employee_id": "EMP-3001",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-01-08",
      "offer_accepted_date": "2025-01-18",
      "start_date": "2025-01-25",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3002",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-01-14",
      "offer_accepted_date": "2025-01-25",
      "start_date": "2025-02-02",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3003",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-01-20",
      "offer_accepted_date": "2025-02-01",
      "start_date": "2025-02-10",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3004",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-01-26",
      "offer_accepted_date": "2025-02-08",
      "start_date": "2025-02-18",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3005",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-02-01",
      "offer_accepted_date": "2025-02-15",
      "start_date": "2025-02-26",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3006",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-02-07",
      "offer_accepted_date": "2025-02-22",
      "start_date": "2025-03-06",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3007",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-02-13",
      "offer_accepted_date": "2025-03-01",
      "start_date": "2025-03-14",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3008",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-02-19",
      "offer_accepted_date": "2025-03-08",
      "start_date": "2025-03-22",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3009",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-02-25",
      "offer_accepted_date": "2025-03-15",
      "start_date": "2025-03-30",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3010",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-03-03",
      "offer_accepted_date": "2025-03-22",
      "start_date": "2025-04-07",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3011",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-03-09",
      "offer_accepted_date": "2025-03-29",
      "start_date": "2025-04-05",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3012",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-03-15",
      "offer_accepted_date": "2025-04-05",
      "start_date": "2025-04-13",
      "exit_date": "2025-08-12",
      "status": "Exited"
    },
    {
      "employee_id": "EMP-3013",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-03-21",
      "offer_accepted_date": "2025-04-12",
      "start_date": "2025-04-21",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3014",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-03-27",
      "offer_accepted_date": "2025-04-19",
      "start_date": "2025-04-29",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3015",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-04-02",
      "offer_accepted_date": "2025-04-26",
      "start_date": "2025-05-07",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3016",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-04-08",
      "offer_accepted_date": "2025-05-03",
      "start_date": "2025-05-15",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3017",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-04-14",
      "offer_accepted_date": "2025-05-10",
      "start_date": "2025-05-23",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3018",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-04-20",
      "offer_accepted_date": "2025-05-17",
      "start_date": "2025-05-31",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3019",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-04-26",
      "offer_accepted_date": "2025-05-06",
      "start_date": "2025-05-21",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3020",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-05-02",
      "offer_accepted_date": "2025-05-13",
      "start_date": "2025-05-29",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3021",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-05-08",
      "offer_accepted_date": "2025-05-20",
      "start_date": "2025-05-27",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3022",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-05-14",
      "offer_accepted_date": "2025-05-27",
      "start_date": "2025-06-04",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3023",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-05-20",
      "offer_accepted_date": "2025-06-03",
      "start_date": "2025-06-12",
      "exit_date": "2025-10-22",
      "status": "Exited"
    },
    {
      "employee_id": "EMP-3024",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-05-26",
      "offer_accepted_date": "2025-06-10",
      "start_date": "2025-06-20",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3025",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-06-01",
      "offer_accepted_date": "2025-06-17",
      "start_date": "2025-06-28",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3026",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-06-07",
      "offer_accepted_date": "2025-06-24",
      "start_date": "2025-07-06",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3027",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-06-13",
      "offer_accepted_date": "2025-07-01",
      "start_date": "2025-07-14",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3028",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-06-19",
      "offer_accepted_date": "2025-07-08",
      "start_date": "2025-07-22",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3029",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-06-25",
      "offer_accepted_date": "2025-07-15",
      "start_date": "2025-07-30",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3030",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-07-01",
      "offer_accepted_date": "2025-07-22",
      "start_date": "2025-08-07",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3031",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-07-07",
      "offer_accepted_date": "2025-07-29",
      "start_date": "2025-08-05",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3032",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-07-13",
      "offer_accepted_date": "2025-08-05",
      "start_date": "2025-08-13",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3033",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-07-19",
      "offer_accepted_date": "2025-08-12",
      "start_date": "2025-08-21",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3034",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-07-25",
      "offer_accepted_date": "2025-08-19",
      "start_date": "2025-08-29",
      "exit_date": "2026-01-19",
      "status": "Exited"
    },
    {
      "employee_id": "EMP-3035",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-07-31",
      "offer_accepted_date": "2025-08-26",
      "start_date": "2025-09-06",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3036",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-08-06",
      "offer_accepted_date": "2025-09-02",
      "start_date": "2025-09-14",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3037",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-08-12",
      "offer_accepted_date": "2025-08-22",
      "start_date": "2025-09-04",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3038",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-08-18",
      "offer_accepted_date": "2025-08-29",
      "start_date": "2025-09-12",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3039",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-08-24",
      "offer_accepted_date": "2025-09-05",
      "start_date": "2025-09-20",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3040",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-08-30",
      "offer_accepted_date": "2025-09-12",
      "start_date": "2025-09-28",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3041",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-09-05",
      "offer_accepted_date": "2025-09-19",
      "start_date": "2025-09-26",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3042",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-09-11",
      "offer_accepted_date": "2025-09-26",
      "start_date": "2025-10-04",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3043",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-09-17",
      "offer_accepted_date": "2025-10-03",
      "start_date": "2025-10-12",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3044",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-09-23",
      "offer_accepted_date": "2025-10-10",
      "start_date": "2025-10-20",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3045",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-09-29",
      "offer_accepted_date": "2025-10-17",
      "start_date": "2025-10-28",
      "exit_date": "2026-03-31",
      "status": "Exited"
    },
    {
      "employee_id": "EMP-3046",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-10-05",
      "offer_accepted_date": "2025-10-24",
      "start_date": "2025-11-05",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3047",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-10-11",
      "offer_accepted_date": "2025-10-31",
      "start_date": "2025-11-13",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3048",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-10-17",
      "offer_accepted_date": "2025-11-07",
      "start_date": "2025-11-21",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3049",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-10-23",
      "offer_accepted_date": "2025-11-14",
      "start_date": "2025-11-29",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3050",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-10-29",
      "offer_accepted_date": "2025-11-21",
      "start_date": "2025-12-07",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3051",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-11-04",
      "offer_accepted_date": "2025-11-28",
      "start_date": "2025-12-05",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3052",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-11-10",
      "offer_accepted_date": "2025-12-05",
      "start_date": "2025-12-13",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3053",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-11-16",
      "offer_accepted_date": "2025-12-12",
      "start_date": "2025-12-21",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3054",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-11-22",
      "offer_accepted_date": "2025-12-19",
      "start_date": "2025-12-29",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3055",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-11-28",
      "offer_accepted_date": "2025-12-08",
      "start_date": "2025-12-19",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3056",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2025-12-04",
      "offer_accepted_date": "2025-12-15",
      "start_date": "2025-12-27",
      "exit_date": "2026-06-10",
      "status": "Exited"
    },
    {
      "employee_id": "EMP-3057",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2025-12-10",
      "offer_accepted_date": "2025-12-22",
      "start_date": "2026-01-04",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3058",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2025-12-16",
      "offer_accepted_date": "2025-12-29",
      "start_date": "2026-01-12",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3059",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2025-12-22",
      "offer_accepted_date": "2026-01-05",
      "start_date": "2026-01-20",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3060",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2025-12-28",
      "offer_accepted_date": "2026-01-12",
      "start_date": "2026-01-28",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3061",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2026-01-03",
      "offer_accepted_date": "2026-01-19",
      "start_date": "2026-01-26",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3062",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2026-01-09",
      "offer_accepted_date": "2026-01-26",
      "start_date": "2026-02-03",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3063",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2026-01-15",
      "offer_accepted_date": "2026-02-02",
      "start_date": "2026-02-11",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3064",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2026-01-21",
      "offer_accepted_date": "2026-02-09",
      "start_date": "2026-02-19",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3065",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2026-01-27",
      "offer_accepted_date": "2026-02-16",
      "start_date": "2026-02-27",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3066",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2026-02-02",
      "offer_accepted_date": "2026-02-23",
      "start_date": "2026-03-07",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3067",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2026-02-08",
      "offer_accepted_date": "2026-03-02",
      "start_date": "2026-03-15",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3068",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2026-02-14",
      "offer_accepted_date": "2026-03-09",
      "start_date": "2026-03-23",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3069",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2026-02-20",
      "offer_accepted_date": "2026-03-16",
      "start_date": "2026-03-31",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3070",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2026-02-26",
      "offer_accepted_date": "2026-03-23",
      "start_date": "2026-04-08",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3071",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2026-03-04",
      "offer_accepted_date": "2026-03-30",
      "start_date": "2026-04-06",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3072",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2026-03-10",
      "offer_accepted_date": "2026-04-06",
      "start_date": "2026-04-14",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3073",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2026-03-16",
      "offer_accepted_date": "2026-03-26",
      "start_date": "2026-04-04",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3074",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2026-03-22",
      "offer_accepted_date": "2026-04-02",
      "start_date": "2026-04-12",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3075",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2026-03-28",
      "offer_accepted_date": "2026-04-09",
      "start_date": "2026-04-20",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3076",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2026-04-03",
      "offer_accepted_date": "2026-04-16",
      "start_date": "2026-04-28",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3077",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2026-04-09",
      "offer_accepted_date": "2026-04-23",
      "start_date": "2026-05-06",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3078",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2026-04-15",
      "offer_accepted_date": "2026-04-30",
      "start_date": "2026-05-14",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3079",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2026-04-21",
      "offer_accepted_date": "2026-05-07",
      "start_date": "2026-05-22",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3080",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2026-04-27",
      "offer_accepted_date": "2026-05-14",
      "start_date": "2026-05-30",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3081",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2026-05-03",
      "offer_accepted_date": "2026-05-21",
      "start_date": "2026-05-28",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3082",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2026-05-09",
      "offer_accepted_date": "2026-05-28",
      "start_date": "2026-06-05",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3083",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2026-05-15",
      "offer_accepted_date": "2026-06-04",
      "start_date": "2026-06-13",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3084",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2026-05-21",
      "offer_accepted_date": "2026-06-11",
      "start_date": "2026-06-21",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3085",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2026-05-27",
      "offer_accepted_date": "2026-06-18",
      "start_date": "2026-06-29",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3086",
      "department": "Sales",
      "role": "Associate",
      "application_date": "2026-06-02",
      "offer_accepted_date": "2026-06-25",
      "start_date": "2026-07-07",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3087",
      "department": "Delivery",
      "role": "Manager",
      "application_date": "2026-06-08",
      "offer_accepted_date": "2026-07-02",
      "start_date": "2026-07-15",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3088",
      "department": "People Ops",
      "role": "Specialist",
      "application_date": "2026-06-14",
      "offer_accepted_date": "2026-07-09",
      "start_date": "2026-07-23",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3089",
      "department": "Engineering",
      "role": "Lead",
      "application_date": "2026-06-20",
      "offer_accepted_date": "2026-07-16",
      "start_date": "2026-07-31",
      "exit_date": "",
      "status": "Active"
    },
    {
      "employee_id": "EMP-3090",
      "department": "Customer Success",
      "role": "Analyst",
      "application_date": "2026-06-26",
      "offer_accepted_date": "2026-07-23",
      "start_date": "2026-08-08",
      "exit_date": "",
      "status": "Active"
    }
  ],
  "invalid_records": [
    {
      "employee_id": "EMP-MISS-OFFER",
      "department": "Delivery",
      "role": "Specialist",
      "application_date": "2026-04-02",
      "offer_accepted_date": "",
      "start_date": "",
      "exit_date": "",
      "status": "Candidate"
    },
    {
      "employee_id": "EMP-BAD-STATUS",
      "department": "Engineering",
      "role": "Analyst",
      "application_date": "2026-05-12",
      "offer_accepted_date": "2026-05-30",
      "start_date": "2026-06-08",
      "exit_date": "",
      "status": ""
    }
  ]
}

***Response code is 200 ok **

