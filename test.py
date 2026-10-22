import json

# import requests


# try:
#     response = requests.get("https://week2-people-ops-api.vercel.app/api/people-ops")
#     response.raise_for_status()
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print(response)
#     data = response.json()
#     print(type(data["records"]))
#     # print(data)


# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)


with open("data.json", "r") as f:
    data = json.load(f)

    



department_exits = {}
highest_count = 0
highest_department = set()
exited_count = 0
for record in data["records"]:
    if record["status"] == "Exited":
        exited_count += 1
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
    if department_exits[department] == highest_count:
        highest_department.add(department)

print()
print(f'Department with the most exits:', highest_department)
print()
for department in department_exits:
    if department_exits[department] == 0:
        print(f'The {department} department has no exits')

  