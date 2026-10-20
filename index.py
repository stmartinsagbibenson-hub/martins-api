import requests


try:
    response = requests.get("https://week2-people-ops-api.vercel.app/api/people-ops")
except Exception as e:
    print(f"Error: {e}")
else:
    print(response)
    data  = response.json()
    print(type(data["records"]))

    for record in data["records"]:
        print(record["employee_id"])
        print(record["department"])
        print(record["role"])
        print(record["status"])
        print("=====================================")
    # sales_department_count = 0
    # for employee in data["records"]:
    #     if employee["department"].lower().strip() == "sales":
    #         sales_department_count +=1

    # print(sales_department_count)



    # if response.status_code == 200:
    #     print("Success!")
    # else:
    #     print("Something went wrong.")




def convert_dollar_naira(aid: float):
    ain = aid * 1500
    return ain



def simple_interest_calculator(p: float, r: float, t: float):
    si = p * r * t
    return si