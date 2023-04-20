
# requests - HTTP library
# trzeba zainstlować moduł 'requests' : pip install requests
import requests

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def monhtly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'bad response'
