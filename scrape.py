import bs4 as bs
import urllib.request

# Video tutorial to follow
# https://www.youtube.com/watch?v=aIPqt-OdmS0

# Source is the URL of the website that will be scraped
source = urllib.request.urlopen(
    'https://www.cars.com/for-sale/searchresults.action/?mdId=21392&mkId=20005&rd=99999&searchSource=QUICK_FORM&zc=19002').read()
# Soup stores the raw html page being scraped
soup = bs.BeautifulSoup(source, 'lxml')

# Output the Title(title) of the website with the name(string or text)
# print(soup.title.text)

# Finds all the HTML tags from the html
# print(soup.find_all('p'))

# Itterates through all the p tages and adds them to paragraph
# outputs the p tags in text form
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# Gets all the text tags from the webpage
# print(soup.get_text)

# Find the URLS in the html
# for url in soup.find_all('a'):
#     print(url.get('href'))

# Finds the Nav on the website
# nav = soup.nav
# Finds custom tag if required
# nav = soup.find('nav')
# # Navigates through the nav tag and outputs all the links
# for url in nav.find_all('a'):
#     print(url.get('href'))

# Finds all the div tags with the class specified
# Prints out the all the text
# for div in soup.find_all('div', class_='shop-srp-listings__inner'):
#     print(div.text)
