import requests
import json
import time


response = requests.get("https://b-signupactivity.ntub.edu.tw/api/Activity/TestGetActivity")

contents = response.text
contents = json.loads(contents)
ActivityId = []
ActivityName = []
ApplyStartDate = []
ApplyStartTime = []
ApplyEndDate = []
ApplyEndTime = []

# print(contents)

nowTime = int(time.time())

for item in contents:
    # print(item)
    start_struct_date = time.strptime(ApplyStartDate, "%Y-%m-%dT%H:%M:%S")
    start_time_stamp = int(time.mktime(start_struct_date))
    stop_struct_time = time.strptime(ApplyEndDate, "%Y-%m-%dT%H:%M:%S")
    stop_time_stamp = int(time.mktime(stop_struct_time))

    if '學生' in item['ApplyQualificationList']:
        if nowTime > start_time_stamp and nowTime < stop_time_stamp:
            ActivityId.append(item['ActivityId'])
            ActivityName.append(item['ActivityName'])
            ApplyStartDate.append(item['ApplyStartDate'])
            ApplyStartTime.append(item['ApplyStartTime'])
            ApplyEndDate.append(item['ApplyEndDate'])
            ApplyEndTime.append(item['ApplyEndTime'])

print(ActivityName)
