import threading
import platform
import bs4 as bs
import urllib.request
import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


# URL
carsdotcom = "https://www.cars.com/"
# Source is the URL of the website that will be scraped
source = urllib.request.urlopen(carsdotcom)
# Soup stores the raw html page being scraped
soup = bs.BeautifulSoup(source, 'lxml')

dbPath = "../Databases/carsdotcom.db"


def createTable(conn, createTableSql):
    """
    create a table from the create_table_sql statement
    :param conn: Connection object
    :param createTableSql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(createTableSql)
    except Error as e:
        print(e)


def getMakes():
    """
    Finds the "select" drop down tag
    select has the attribute of "name":"makeId"
    Options variable is a list
    """
    value = []
    make = []
    option = soup.find("select", {"name":"makeId"}).findAll('option')
    for val in option[1:]:
        value.append(val.get('value'))
        make.append(val.text)
        # print(val.get('value'), val.text)
        # print(dict(zip([val.get('value')], [val.text])))

    dic = zip(value, make)

    try:
        conn = sqlite3.connect(dbPath)
        print(sqlite3.version)
        c = conn.cursor()
    except Error as e:
        print(e)

    # Insert new Data into table Makes
    c.executemany("INSERT INTO Makes VALUES(NULL,?,?) ", dic)
    conn.commit()
    c.close()
    conn.close()


def getModels(carMake):
    """
    Function takes each Car Make
    Gets started on its own thread for each Make
    Scrapes all the models for that Make
    Saves it to the SQL db in Models with their primary key of each Make
    :param carMake:
    :return:
    """
    options = Options()
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
    options.add_experimental_option("prefs", prefs)

    if platform.system() == "Windows":
        driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=options)
    elif platform.system() == "Linux" or platform.system() == "Linux2":
        driver = webdriver.Chrome(options=options)

    driver.get(carsdotcom)

    select = Select(driver.find_element_by_name('makeId'))
    select.select_by_value(carMake)
    modl = driver.find_element_by_name("modelId")

    value= []
    model = []
    selectModl = Select(modl)
    dropdown_options = selectModl.options
    for option in dropdown_options[1:]:
        value.append(option.get_attribute('value'))
        model.append(option.text)
    print(value)
    print(model)
    driver.quit()


def initSqlTables():
    """
    Initializes tables in the SQLite db
    :return:
    """
    # sql_create_makes_table = """
    #                         CREATE TABLE IF NOT EXISTS Makes (
    #                         "makeId"	INTEGER NOT NULL,
    #                         "name"	TEXT NOT NULL,
    #                         PRIMARY KEY (makeId)
    #                     ); """

    sql_create_makes_table = """
                            CREATE TABLE IF NOT EXISTS Makes(
                            "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                            "makeId"	INTEGER NOT NULL,
                            "name"	TEXT NOT NULL
                        ); """

    sql_create_model_table = """
                            CREATE TABLE IF NOT EXISTS Models(
                            "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                            "makeId"	INTEGER NOT NULL,
                            "modelId"	INTEGER NOT NULL,
                            "name"	TEXT NOT NULL
                        );"""

    try:
        conn = sqlite3.connect(dbPath)
        print("Initialized SQL Tables Makes, Models")
        c = conn.cursor()
    except Error as e:
        print(e)

    # Delete all Data from the tables
    c.execute("DROP TABLE Makes")
    conn.commit()
    c.execute("DROP TABLE Models")
    conn.commit()

    if conn is not None:
        createTable(conn, sql_create_makes_table)
        createTable(conn, sql_create_model_table)
    else:
        print("Failed to create db tables")


if __name__ == "__main__" :
    # initSqlTables()
    # getMakes()

    getModels("20001")