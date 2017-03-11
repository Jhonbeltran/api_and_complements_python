#Este codigo lo puedo poner en la view que quiero que use el json 

import json
from urllib.request import urlopen

url = 'http://localhost:8000/api/v1/answers/?format=json'
placeholder = urlopen(url)

data = json.loads(placeholder.read())

answer = data["results"][0]["change_pass_answer"]

string = json.dumps(answer)

print(answer)

print(string)

print(type(answer))

print(type(string))
