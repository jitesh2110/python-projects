import requests
import datetime

App_Id = "your api id"
App_Key = "your api key"
Api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_api_endpoint ='your endpoint'
headers = {"content-type": "application/json",
           "x-app-id": App_Id,
           "x-app-key": App_Key}
work = input("what did you did today?:")

parameters = {"query": work}

response = requests.post(url=Api_endpoint,
                         headers=headers,
                         json=parameters)

print(response.status_code)
response = response.json()['exercises']
len =len(response)
print(len)



today = datetime.datetime.now()
date = str(today.date())
tim = str(today.time())
for i in range(0,len):
    cal = response[i]['nf_calories']
    duration = response[i]['duration_min']
    type = response[i]['name']

    body = {
        "sheet1": {
            'date': date,
            'time': tim,
            'exercise': type,
            'duration': duration,
            'cal': cal,
            
        }
    }

    resp = requests.post(url=sheet_api_endpoint, json=body)
    resp = resp.json()
    print(resp)
