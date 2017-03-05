import string

def anonymous_letter(article, message):
    catalog = dict()

    for word in article:
        print ('%s' % word)


if __name__ == '__main__':
    
    path = input('Path or file_name: ')
    file = open(path, "r+")
    read_file = file.read().translate(str.maketrans('',
                                        '', string.whitespace))
    file.close()
    

    message = input('Message: ')
    message_clear = message.translate(str.maketrans('',
                                        '', string.whitespace))
    

    print (anonymous_letter(read_file, message_clear))
