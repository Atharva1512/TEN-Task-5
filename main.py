import requests
import time
from plyer import notification

data= requests.get("https://corona-rest-api.herokuapp.com/Api/")

dt=data.json()
dt1=dt["Success"][:5]
print(dt1)

if __name__ == "__main__":
    i=0
    while True:
        cases=dt1[i]["cases"]
        recovered=dt1[i]["recovered"]
        notification.notify(
            title = dt1[i]["country"],
            message = f"Total Cases: {cases}\nRecovered:{recovered}",
            app_icon="G:/Internship_TEN/task5/icon.ico",
            timeout=5   
        )
        time.sleep(20)
        i= i+1
        if i==5:
            i=0