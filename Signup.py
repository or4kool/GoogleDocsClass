import re
from User import Users


class Signup:
    def __init__(self, firstname = '', lastname ='', password = '', email ='', gender = '', birthday = '', phonenumber = '', location = ''):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.phonenumber = phonenumber
        self.location = location
        
    
    def collect_user_info(self):
        user_data = {}
        user_info = ['first name', 'last name', 'username', 'password', 'birthday', 'gender', 'phone number', 'email', 'location']
        for get_user in user_info:
            user_data[get_user] = input("Please enter your {}: ". format(get_user))
        print(user_data)
        return user_data
