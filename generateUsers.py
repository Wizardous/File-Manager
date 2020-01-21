from Framework.api.records import Records
import requests as req
import json

session = req.Session()

def getUser(count=1):
    url = f"https://randomuser.me/api/?results={count}"
    response = session.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        file_api = Records()
        for user in data['results']:
            new_data = {}
            new_data['username'] = user['login']['username']
            new_data['email'] = user['email']
            new_data['password'] = user['login']['sha256']
            print(new_data)
            file_api.addRecord(new_data)

def main():
    count = int(input("How many? : "))
    getUser(count)

if __name__ == "__main__":
    main()
    