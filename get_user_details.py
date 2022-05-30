import requests

resp = requests.get("https://gorest.co.in/public/v2/users")
id = 3363

if resp.status_code == 200:
    print("A successful request")
else:
    print("Encountered some problem, status code: {code}".format(code=resp.status_code))

print(resp.headers)

json_resp = resp.json()
print("Complete Data: \n{data}".format(data=json_resp))

a = 0
for i in json_resp:
    if i["id"] == id:
        print("Id found")
        a = 1
        break
if a != 1:
    print("Not found")