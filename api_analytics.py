import requests

try:
    response = requests.get("https://week2-people-ops-api.vercel.app/api/people-ops")
    response.raise_for_status()
except Exception as e:
    print(f"Error: {e}")
else:
    print(response)
    data = response.json()
    print(type(data["records"]))
    # print(data)

   
#     # print(len(data["records"]))

#     # count = 0
#     # for record in data["records"]:
#     #   count = count + 1
#     # print(count)



#     employees_with_blanc_status = 0
#     for record in data["records"]: 
#         if record["status"] == "":   
#             print(record["employee_id"])
#             print(record["status"])
#             employees_with_blanc_status =  employees_with_blanc_status + 1
#     print(employees_with_blanc_status)



#     # After running this code, a 200 OK response was displayed, which means the request succeeded.
#     print("The id of staff in the sales department:")
#     for record in data["records"]:
#         if record["department"].lower().strip() == "sales":
#               print(record["employee_id"])
           

#     print()
#     print("The id of all active staff:")
#     for record in data["records"]:
#         if record["status"].lower().strip() == "active":
#             print(record["employee_id"])


#     departmental_role = {}
#     for record in data["records"]:
#         department = record["department"].lower().strip()
#         role = record["role"].lower().strip()
#         if department in departmental_role:
#             departmental_role[department].add(role)
#         else:
#             departmental_role[department] = {role}
#     print(departmental_role)

               
                
   
  
        
#     department_exits = {}
#     highest_count = 0
#     highest_department = ""
#     for record in data["records"]:
#         department = record["department"].lower().strip()
#         status = record["status"].lower().strip()
#         if department not in department_exits:
#             department_exits[department] = 0
#         if status == "Exited".lower().strip():
#             department_exits[department] += 1
#     for department in department_exits:
#         print(department, department_exits[department])
#     for department in department_exits:
#         if department_exits[department] > highest_count:
#             highest_count = department_exits[department]
#             highest_department = department
#     print()
#     print(f'Department with the most exits:', highest_department)
#     print()
#     print(f'Number of exits:', highest_count)
#     print()
#     print("Departments with no exits:")
#     for department in department_exits:
#         if department_exits[department] == 0:
#             print(department, "has no exits")



#     for record in data["records"]:


# import datetime
# now = datetime.datetime.now()
# print(now)


# for record in data["records"]:
#     application_date = record.get("application_date")
#     offer_accepted_date = record.get("offer_accepted_date")
#     if offer_accepted_date:
#         print(f'Employee {record.get("employee_id")} applied on {application_date}')
#         print(f"Employee {record.get("employee_id")} accepted offer on {offer_accepted_date}")
#         application_date_obj = datetime.datetime.strptime(application_date, "%Y-%m-%d")
#         offer_accepted_date_obj = datetime.datetime.strptime(offer_accepted_date, )        
#         print(application_date_obj)
      
       