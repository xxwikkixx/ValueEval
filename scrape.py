import bs4 as bs
import urllib.request

# Video tutorial to follow
# https://www.youtube.com/watch?v=aIPqt-OdmS0

source = urllib.request.urlopen('https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId=21392&mkId=20005&page=1&perPage=20&rd=99999&searchSource=SORT&sort=price-highest&zc=19002').read()

soup = bs.BeautifulSoup(source, 'lxml')

print(soup)

