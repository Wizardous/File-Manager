import requests as req

class Login:

    def __init__(self):
        self.__api_url = 'https://sam123.pythonanywhere.com/examfiles/login/authenticate/'
        self.__session1 = req.Session()

    def __get_request(self):
        response = self.__session1.get(self.__api_url)
        return response.json()

    def authenticate(self, username, password):
        response = self.__get_request()
        if response['email'] == username and response['pass'] == password:
            return True
        else:
            return False



def main():
    # l = Login()
    pass

if __name__ == "__main__":
    main()