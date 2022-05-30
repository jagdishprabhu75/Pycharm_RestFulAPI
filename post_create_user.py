import requests

payload = {
    "name": "depika",
    "gender": "female",
    "email": "deepika@dace.com",
    "status": "inactive"
}

auth_token = "588ceab1d4ac0a11c7a38592815057c179c1a53644ec39a0c5b4ea8d6a084c04"
hed = {'Authorization': 'Bearer ' + auth_token}

result = requests.post("https://gorest.co.in/public/v2/users", data=payload, headers=hed)
if result.status_code == 201:
    json_resp = result.json()
    print(json_resp)
    #assert json_resp['id'] is None, "User not created"
else:
    print("Error")