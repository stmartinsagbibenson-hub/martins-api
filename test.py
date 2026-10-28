import json

# import requests


# try:
#     response = requests.("https://week2-people-ops-api.vercel.app/api/people-ops")
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


# with open("data.json", "r") as f:
#     data = json.load(f)

    



# department_exits = {}
# highest_count = 0
# highest_department = set()
# exited_count = 0
# for record in data["records"]:
#     if record["status"] == "Exited":
#         exited_count += 1
#     department = record["department"].lower().strip()
#     status = record["status"].lower().strip()
#     if department not in department_exits:
#         department_exits[department] = 0
#     if status == "Exited".lower().strip():
#         department_exits[department] += 1

# for department in department_exits:
#     print(department, department_exits[department])

# for department in department_exits:
#     if department_exits[department] > highest_count:
#         highest_count = department_exits[department]
#     if department_exits[department] == highest_count:
#         highest_department.add(department)

# print()
# print(f'Department with the most exits:', highest_department)
# print()
# for department in department_exits:
#     if department_exits[department] == 0:
#         print(f'The {department} department has no exits')

  




from datetime import datetime
import os
from dotenv import load_dotenv
import requests
load_dotenv()

PEOPLE_OPS_URL = os.getenv("PEOPLE_OPS_URL")

if PEOPLE_OPS_URL is None:
    raise RuntimeError(
        "PEOPLE_OPS_URL is not set. Check your .env file."
    )

def make_request(url, method="GET"):
    import requests
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
     raise Exception(
         status_code=502,
         detail=f"People Ops API request failed: {e}"
     )

data = make_request(PEOPLE_OPS_URL)

print(type(data))

print(type(data["records"]))
# print(data)

print("The id of staff in the sales department:")
for record in data["records"]:
    if record["department"].lower().strip() == "sales":
         print(record["employee_id"])
         print("========")


print()