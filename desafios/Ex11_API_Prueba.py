# link = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&page=1'
# api_key = '&api_key=LxiLXqbPbbACk2VrKaeiisyDTa5c8xfiqg2P7anJ'

import requests
import json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&page=1&api_key='
api_key = 'LxiLXqbPbbACk2VrKaeiisyDTa5c8xfiqg2P7anJ'

def request(url, api_key):
    response = requests.request("GET", url + api_key)
    return json.loads(response.text)

def build_web_page(resp):
    html = "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<ul>\n"
    counter = 0
    for iter in resp['photos']:
        html += "\t\t\t<li><img src=\'{}\'></li>\n".format(resp['photos'][counter]['img_src'])
        counter += 1
    html += "\t\t</ul>\n\t</body>\n</html>\n"
    with open("output.html", "w") as f:
        f.write(html)

def photos_count(resp):
    new_dict = {}
    counter = 0
    for iter in resp['photos']:
        new_dict[resp['photos'][counter]['camera']['name']] = resp['photos'][counter]['rover']['total_photos']
        counter += 1
    print(new_dict)

resp = request(url, api_key)
build_web_page(resp)
photos_count(resp)
