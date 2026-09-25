import requests


try:
    response = requests.get("https://example.com")
except Exception as e:
    print(f"Error: {e}")
else:
    print(response)
    data  = response.json()
    print(type(data))
    print(data)
       
    # if response.status_code == 200:
    #     print("Success!")
    # else:
    #     print("Something went wrong.")




def convert_dollar_naira(aid: float):
    ain = aid * 1500
    return ain
