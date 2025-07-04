import simplejson
import webbrowser
import pytagcloud

tag = [
    ('school', 30),
    ('rainbos', 70),
    ('cloud', 12),
    ('world', 300),
    ('peach', 130),
    ('pink', 39),
    ('image', 110),
    ('python', 70),
    ('computer', 60),
    ('game', 210),
    ('한글', 210),
]
taglist = pytagcloud.make_tags(tag, maxsize=50)
print(taglist)
pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(600,600), 
                            fontname='Korean', rectangular=True)
webbrowser.open('wordcloud.jpg')


# import os
# os.startfile('wordcloud.jpg')