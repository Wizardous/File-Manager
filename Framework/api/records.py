import json
import os

class Records:
    def __init__(self):
        self.file_path = "./Files/"
        self.file_name = "records.json"
        try:
            if not os.path.exists(self.file_path+self.file_name):
                if not os.path.exists(self.file_path):
                    os.mkdir(self.file_path)

                with open(self.file_path+self.file_name,"w") as file:
                    file.write("[]")
        except Exception as e:
            print(e)

    def readRecords(self):
        try:
            with open(self.file_path+self.file_name, 'r') as file:
                data = json.loads(file.read())
                records_list = [tuple([v for v in r.values()]) for r in data]
            return True, records_list

        except Exception as e:
            return False, e

    def addRecord(self, new_data):
        try:
            with open(self.file_path+self.file_name, 'r') as file:
                data = json.loads((file.read()))
                data.append(new_data)
            with open(self.file_path+self.file_name, 'w') as file:
                file.write(json.dumps(data))
            return True

        except Exception as e:
            return False, e

    def searchRecords(self, key,mode='username'):
        try:
            if key == "" or mode not in ('username', 'email'):
                raise KeyError

            if mode == 'username':
                status, data = self.readRecords()
                if status:
                    results = [r for r in data if key == r[0]]
                    return True, results
                else:
                    raise LookupError

            elif mode == 'email':
                status, data = self.readRecords()
                if status:
                    results = [r for r in data if key == r[1]]
                    return True, results
                else:
                    raise LookupError

        except LookupError:
            return False, 404
        except Exception as  e:
            return False, e

    def deleteRecord(self, key, mode='username'):
        try:
            if key == "" or mode not in ('username', 'email'):
                raise KeyError

            with open(self.file_path+self.file_name, 'r') as file:
                data = json.loads(file.read())

            new_data = [r for r in data if key != r[mode]]

            if len(data) != len(new_data):
                with open(self.file_path+self.file_name, 'w') as file:
                    file.write(json.dumps(new_data))
                return True, "Deleted!"
            else:
                raise LookupError

        except LookupError:
            return False, 404
        except Exception as e:
            return False, e

    def updateRecord(self, key, new_data):
        try:
            with open(self.file_path+self.file_name, 'r') as file:
                data = json.loads(file.read())

            new_data_list = []
            found = False
            for r in data:
                if r['username'] != key:
                    new_data_list.append(r)
                else:
                    found = True
                    new_data_list.append(new_data)

            if found:
                with open(self.file_path+self.file_name, 'w') as file:
                    file.write(json.dumps(new_data_list))
                return True, None
            else:
                raise  LookupError

        except LookupError:
            return False, 404
        except Exception as e:
            return False, e

def main():
    r = Records()
    print(r.readRecords())

if __name__ == "__main__":
    main()