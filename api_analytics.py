import requests
from datetime import datetime
from fastapi import FastAPI, HTTPException 
import os
from dotenv import load_dotenv
load_dotenv()

PEOPLE_OPS_URL = os.getenv("PEOPLE_OPS_URL")

if PEOPLE_OPS_URL is None:
    raise RuntimeError(
        "PEOPLE_OPS_URL is not set. Check your .env file."
    )

def make_request(url, method="GET"):
    response = requests.request(
        method=method,
        url=url,
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def fetch_people_ops():
   try:
     return make_request(PEOPLE_OPS_URL)

   except requests.RequestException as e:
     raise HTTPException(
         status_code=502,
         detail=f"People Ops API request failed: {e}"
     )

data = make_request(PEOPLE_OPS_URL, "GET")

print(type(data))

print(type(data["records"]))
# print(data)

print("The id of staff in the sales department:")
for record in data["records"]:
    if record["department"].lower().strip() == "sales":
         print(record["employee_id"])
         print("========")


print()
print("The id of all active staff:")
for record in data["records"]:
    if record["status"].lower().strip() == "active":
        print(record["employee_id"])


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
print("Department counts:")
for department, count in department_count.items():
    print(f"{department}: {count}")

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


departmental_role = {}
for record in data["records"]:
    department = record["department"].lower().strip()
    role = record["role"].lower().strip()
    if department in departmental_role:
        departmental_role[department].add(role)
    else:
        departmental_role[department] = {role}
    print(departmental_role)

for record in data["records"]:
    employee_id = record["employee_id"].lower().strip()
    status = record["status"].lower().strip()
    exit_date = record["exit_date"].lower().strip()
    if status == "Exited".lower().strip():
        print(employee_id,status,exit_date) 

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

for record in data["records"]:
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

slowest_department = None
highest_average = 0
for department in department_days:
    average = department_days[department] / department_count[department]
    if average > highest_average:
        highest_average = average
        slowest_department = department
print(f"Slowest department to hire: {slowest_department}")
print(f"Average time-to-offer: {highest_average} days")


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



 
app = FastAPI(docs_url="/docs")

@app.get("/employees")
def get_employees():
    data = fetch_people_ops()
    return data["records"]


def get_active_employees(records):
    active_employees = []
    for record in records:
        if record["status"] == "Active":
            active_employees.append(record)
    return active_employees
    
@app.get("/employees/active")
def get_active_employees_endpoint():
    data = fetch_people_ops()
    return get_active_employees(data["records"])


@app.get("/departments/{name}/employees")
def get_department_employees(name: str):
    data = fetch_people_ops()
    department_employees = []
    for record in data["records"]:
        if record["department"].lower().strip() == name.lower().strip():
            department_employees.append(record)
    if not department_employees:
        raise HTTPException(
            status_code=404,
            detail=f"No employees found for department '{name}'"
        )
    return department_employees
    



def calculate_headcount(records):
    department_count = {}
    for record in records:
        department = record["department"].lower().strip()
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1
    return department_count

@app.get("/stats/headcount")
def get_department_headcount():
    data = fetch_people_ops()
    return calculate_headcount(data["records"])

def calculate_status_summary(records):
    summary = {
        "blank": 0,
        "Active": 0,
        "Exited": 0,
        "Candidate": 0
    }
    for record in records:
        status = record["status"]
        if status == "":
            summary["blank"] += 1
        elif status in summary:
            summary[status] += 1
    return summary

@app.get("/stats/status-summary")
def get_department_status():
    data = fetch_people_ops()
    return calculate_status_summary(data["records"])


def calculate_exits(records):
    exited_employees = []
    for record in records:
        employee_id = record["employee_id"]
        start_date = record["start_date"]
        exit_date = record["exit_date"]
        if start_date and exit_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(exit_date, "%Y-%m-%d")
            tenure = (end - start).days
            exited_employees.append({
                "employee_id": employee_id,
                "tenure_days": tenure
            })
    return exited_employees

@app.get("/stats/exits")
def get_exited_employees_tenure():
    data = fetch_people_ops()
    return calculate_exits(data["records"])

def calculate_time_to_offer(records):
    department_days = {}
    department_count = {}
    for record in records:
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
    department_average = {}
    for department in department_days:
        department_average[department] = (
            department_days[department] / department_count[department]
        )
    return department_average


@app.get("/stats/time-to-offer")
def get_time_to_offer():
    data = fetch_people_ops()
    return calculate_time_to_offer(data["records"])



def calculate_hiring_by_month(records):
    monthly_hires = {}
    for record in records:
        start_date = record["start_date"]
        if start_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            month = start.strftime("%B")
            if month in monthly_hires:
                monthly_hires[month] += 1
            else:
                monthly_hires[month] = 1
    return monthly_hires

@app.get("/stats/hiring-by-month")
def get_hire_per_month():
    data = fetch_people_ops()
    return calculate_hiring_by_month(data["records"])

def calculate_data_quality(records):
    valid_records = []
    invalid_records = []
    for record in records:
        if is_valid(record):
            valid_records.append(record)
        else:
            invalid_records.append(record)
    return {
        "valid_records": valid_records,
        "invalid_records": invalid_records
    }

@app.get("/data-quality")
def get_data_quality():
    data = fetch_people_ops()
    return calculate_data_quality(data["records"])