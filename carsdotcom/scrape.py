import bs4 as bs
import urllib.request

# Generates a dynamic URL for cars.com
def generateURL(makeId, modelId, perPage, radius, sort, zipCode):
    # MakeID = BMW = 20005
    # ModelID = M3 = 21392
    # PerPage = 100
    # Sort = year-newest
    # ZipCode = 19002
    # Radius = 99999 for max range
    carUrl = "https://www.cars.com/for-sale/searchresults.action/?dealerType=all&mdId="+modelId+"&mkId="+makeId+"&page=1&perPage="+perPage+"&rd="+radius+"&searchSource=PAGINATION&sort="+sort+"&zc="+zipCode

    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(carUrl.read())
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')

    return soup

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
    # for div in soup.find_all('div', class_='shop-srp-listings__inner'):
    #     print(div.text)

    for url in soup.find_all('a', class_='shop-srp-listings__listing'):
        print(url.get('href'))


if __name__ == "__main__" :
    pass