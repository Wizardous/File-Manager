import re
import os

class Record_manger:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def __check_email(self, email):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.search(regex, email)
    
    def __check_password(self, password):
        if len(password) < 8:
            return False
        else:
            return True
    
    def search_record(self, keyword):
        try:
            read_data = self.read_record()
            search_list = []
            for sr, element in enumerate(read_data):
                if keyword in element[0] or keyword in element[1]:
                    search_list.append((sr,element))

            return search_list
        except Exception as e:
            print(e)
            return False 

    def insert_record(self, data_list):
        if not self.__check_email(data_list[1]):
            print("[ERROR] : Entered Email is INVALID!")
            return False
        elif not self.__check_password(data_list[2]):
            print("[ERROR] : Password combination too small!")
            return False
        else:
            data_string = "\n".join(data_list) + "\n\n"
        try:
            with open(self.file_name, 'a+') as file_writer:
                file_writer.write(data_string)
            return True

        except Exception as e:
            print(e)
            return False
        
    def read_record(self, _id=None):
        if _id == None:    # <-- Read all records
            try:
                with open(self.file_name, 'r') as file_reader:
                    file_string = file_reader.read()   # <-- Read the whole file data to a string
                    
                    if len(file_string) == 0:
                        return 0
                    
                    final_data = []
                    record_chunks = file_string.split("\n\n")
                    for record in record_chunks[:-1]:
                        chunk_lines = record.split("\n")
                        final_data.append((chunk_lines[0], chunk_lines[1], chunk_lines[2]))
                    
                    return final_data
            except Exception as e:
                print(e)
                return False
    
    def delete_record(self, serial_no):
        original_data = self.read_record()
        if original_data == 0:
            print("Records File already Empty!")
            return True
        elif not original_data:
            print("[ERROR] Problem in Deletion!")
            return False
        else:
            with open(self.file_name, 'w') as temp_file:
                deleted = False
                for sr, record in enumerate(original_data):
                    if sr == serial_no-1:
                        continue
                        deleted = True
                    else:
                        data_string = "\n".join(record) + "\n\n"
                        temp_file.write(data_string)
            if deleted:
                return True
            else:
                print("Specified Record not found in the file!")
                return False
    
    def update_record(self, serial_no, update_record):
        original_data = self.read_record()
        if original_data == 0:
            print("Records File is Empty!")
            return True
        elif not original_data:
            print("[ERROR] Problem in Problem!")
            return False
        else:
            with open(self.file_name, 'w') as temp_file:
                updated = False
                for sr, record in enumerate(original_data):
                    if sr == serial_no-1:
                        data_string = "\n".join(update_record) + "\n\n"
                        temp_file.write(data_string)
                        update = True
                    else:
                        data_string = "\n".join(record) + "\n\n"
                        temp_file.write(data_string)
            if updated:
                return True
            else:
                print("Specified Record not found in the file!")
                return False

def main():
    
    file_name = "Records.txt"
    fm = Record_manger(file_name)
    choice = None
    while True:
        print("\n1. Insert a record")
        print("2. View all record")
        print("3. Delete a record")
        print("4: Update a record")
        print("5. Search Records")
        print("0: Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            name = input("\nEnter a name : ")
            email = input("\nEnter a email : ")
            password = input("\nEnter password : ")

            if fm.insert_record([name, email, password]):
                print("\nData Inserted Successfully!")
            else:
                print("Some Problem occured, Record insertion Aborted.")

        elif choice == "2":

            data = fm.read_record()

            if data == 0:
                print("\nNo records found!")
            elif not data:
                print("\n[ERROR]")
            else:
                print("\n:: All Records ::\n")
                for index, elem in enumerate(data):
                    print("\nSerial No : " + str(index+1))
                    print("\tName : " + elem[0])
                    print("\tEmail : " + elem[1])
                    print("\tPassword : " + elem[2] + "\n")

        elif choice == "3":
            sr = int(input("Enter the serial No. of record to delete : "))
            result = fm.delete_record(serial_no=sr)
            if result:
                print("Record Deleted Successfully!")
            else:
                print("Deletion Failed!")

        elif choice == "4":
            sr = int(input("Enter the serial No. of record to update: "))
            name = input("Updated Name :")
            email = input("Updated Email : ")
            password = input("Updated Password : ")
            result = fm.update_record(serial_no=sr, update_record=[name, email, password])
            if result:
                print("Record Updated Successfully!")
            else:
                print("Updation Failed!")

        elif choice == "5":
            Keyword = input("Enter the keyword to search : ")

            search_result = fm.search_record(keyword=Keyword)
            if len(search_result) == 0:
                print("No Search Results!")
            else:
                print("\n\n",len(search_result), "Search Result(s)\n")
                for result in search_result:
                    print("Serial No. : ", result[0] + 1)
                    print("\tName :", result[1][0])
                    print("\tEmail :", result[1][1])
                    print("\tPassword :", result[1][2], end="\n\n")

        elif choice == "0":
            break

if __name__ == "__main__":
    main()