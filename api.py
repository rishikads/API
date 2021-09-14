import requests
import pprint
def age(name):
    url='https://api.agify.io/'
    parameters= {'name': name}
    response= requests.get(url, params= parameters)
    return (response.json())
name= str(input("Enter the name: "))
age= age(name)
print (age)


