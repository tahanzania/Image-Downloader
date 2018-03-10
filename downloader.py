import random

import urllib



def download_image(url):

    img_name = random.randrange(100, 500)

    full_name = str(img_name) + '.png'

    urllib.urlretrieve(url,full_name)



download_image('http://www.tahadharamsi.com/uploads/1/2/9/4/1294209/4920220_orig.jpg')
