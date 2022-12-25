import wget

print('Download favicon.ico')

url = 'https://wikipedia.org/'
wget.download(url+'/favicon.ico', './')

