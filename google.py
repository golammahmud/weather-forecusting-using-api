import requests
import json

api_key='AIzaSyB_iVu9R21lptilpuxhaDgNvwJrn7ZYOgg'
address='banani,dhaka'
params={
    'key':api_key,
    'address':address
}
base_url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
response=requests.get(base_url,params=params)
r=response.json()
print(r)