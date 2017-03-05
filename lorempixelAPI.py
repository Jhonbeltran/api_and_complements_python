from urllib.request import urlopen

url = "http://lorempixel.com/640/480/sports/"
placeholder = urlopen(url)
content = placeholder.read()
file = open("holder.jpg", "wb")
file.write(content)
file.close()