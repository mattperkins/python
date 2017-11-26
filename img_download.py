import urllib.request

def img_dl(url, file_path, file_name):
    full_path = file_path + file_name
    urllib.request.urlretrieve(url, full_path)

url = input('Enter URL of image you wish to download: ')
file_name = input('What do you wish to name this file, including file type (i.e .jpg): ')

img_dl(url, './', file_name)

