import bs4 as bs
import urllib.request
import carsdotcom




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


def getlistiingURL():
    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(
        "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId=21392&mkId=20005&page=1&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&zc=19002")
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')
    for url in soup.find_all('a', class_='shop-srp-listings__listing'):
        print(url.get('href'))

def getBasics():
    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(
        "https://www.cars.com/vehicledetail/detail/786646952/overview/")
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')
    for div in soup.find_all('ul', class_='vdp-details-basics__list'):
        print(div.text)

def getFeatures():
    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(
        "https://www.cars.com/vehicledetail/detail/786646952/overview/")
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')
    # test = soup.find('div', class_='cui-accordion-section__content')
    # print(test.text)
    for div in soup.find_all('ul', class_='vdp-details-basics__features-list'):
        print(div.text)

def getPrice():
    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(
        "https://www.cars.com/vehicledetail/detail/786646952/overview/")
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')
    test = soup.find('div', class_='vehicle-info__price')
    print(test.text)


if __name__ == "__main__" :
    # test = carsdotcom.Car()
    # print(test)
    # print(carsdotcom.generateURL('1','1','1','1','1','1'))

    # getlistiingURL()

    for i in range(10):
        print(i)


