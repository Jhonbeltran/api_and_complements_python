from urllib.request import urlopen

url = 'http://lorempixel.com'
categories = ['abstract', 'animals','business',
            'cats','city','food', 'night','life',
            'fashion','people','nature','sports',
            'technics','transport',]

width = input('Width: ')
heigth = input('Height: ')
category = input('Category: ')


for img in range(10): 
    url_req = '%s/%s/%s/%s/%d' % (url,
                            width,
                            heigth,
                            categories[int(category)], img)

    placeholder = urlopen(url_req)
    content = placeholder.read()
    file = open('holder_%d.jpg' % img, 'wb')
    file.write(content)
    file.close()