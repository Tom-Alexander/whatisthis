from whatisthis import create_server

def emitter(image, tag):
    print(image, tag)

images = ['../data/img_001.jpg', '../data/img_002.jpg', '../data/img_003.jpg']
categories = ['cat', 'dog']

create_server(
    emitter=emitter,
    images=images,
    categories=categories)
