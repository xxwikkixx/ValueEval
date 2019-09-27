import bs4 as bs
import urllib.request


def tutorialTest():
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
    # for div in soup.find_all('div', class_='vdp-details-basics'):
    #     print(div.text)
    pass

# Generates a dynamic URL for cars.com
def generateURL(makeId, modelId, perPage, radius, sort, zipCode):
    '''
    :param makeId: MakeID = BMW = 20005
    :param modelId: ModelID = M3 = 21392
    :param perPage: PerPage = 100
    :param radius: Sort = year-newest
    :param sort: ZipCode = 19002
    :param zipCode: Radius = 99999 for max range
    :return: carUrl
    '''
    carUrl = "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId=" \
             + modelId + "&mkId=" + makeId + "&page=1&perPage=" + perPage + "&rd=" \
             + radius + "&searchSource=PAGINATION&sort=" + sort + "&zc=" + zipCode
    return carUrl

def getlistiingURL():
    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(
        "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId=21392&mkId=20005&page=1&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&zc=19002")
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')
    for url in soup.find_all('a', class_='shop-srp-listings__listing'):
        print(url.get('href'))


def getFullCar():
    source = urllib.request.urlopen(
        "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&" \
        "mdId=21392&" \
        "mkId=20005&" \
        "page=1&perPage=100&" \
        "rd=99999&" \
        "searchSource=GN_REFINEMENT&sort=relevance&yrId=20199&zc=19002")
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')

    StockType = []
    Title = []
    Price = []
    Miles = []
    Info = []
    Dealer = []

    infs = []

    for cars in soup.find_all('div', attrs={'id':'srp-listing-rows-container'}):
        stocktype = cars.find('div', class_='listing-row__stocktype')
        title = cars.find('h2', class_='listing-row__title')
        price = cars.find('span', class_='listing-row__price')
        miles = cars.find('span', class_='listing-row__mileage')
        for inf in soup.find_all('ul', class_='listing-row__meta'):
            infs.append(inf.text)
        dealer = cars.find('div', class_='listing-row__dealer__basic-details')

        StockType.append(stocktype.text.strip())
        Title.append(title.text.strip())
        Price.append(price.text.strip())
        Miles.append(miles.text.strip())
        Info.append(infs)
        Dealer.append(dealer.text.strip())
    print(StockType, Title, Price, Miles, Info, Dealer)


if __name__ == "__main__" :
    getFullCar()
