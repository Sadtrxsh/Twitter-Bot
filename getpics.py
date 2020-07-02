# model scraping for themodelbot

from bs4 import BeautifulSoup as bs
import os
import cfscrape

# website with model images
url = 'https://www.istockphoto.com/photos/shirtless-old-man?mediatype=photography&phrase=shirtless%20old%20man&sort=mostpopular'

scraper = cfscrape.create_scraper()

# download page for parsing
page = scraper.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('oldman'):
    os.makedirs('oldman')

# move to new directory
os.chdir('oldman')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = scraper.get(url)
        if response.status_code == 200:
            with open('oldman-' + str(x) + '.jpg', 'wb') as f:
                f.write(scraper.get(url).content)
                f.close()
                x += 1
    except:
        pass






