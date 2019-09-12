import threading
import bs4 as bs
import urllib.request
import sqlite3
from sqlite3 import Error


# URL
carsdotcom = "https://www.cars.com/"
# Source is the URL of the website that will be scraped
source = urllib.request.urlopen(carsdotcom)
# Soup stores the raw html page being scraped
soup = bs.BeautifulSoup(source, 'lxml')

dbPath = "../Databases/carsdotcom.db"


"""
create a table from the create_table_sql statement
:param conn: Connection object
:param createTableSql: a CREATE TABLE statement
:return:
"""
def createTable(conn, createTableSql):
    try:
        c = conn.cursor()
        c.execute(createTableSql)
    except Error as e:
        print(e)


"""
Finds the "select" drop down tag
select has the attribute of "name":"makeId"
Options variable is a list
"""
def getMakes():
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


def getModels():
    # Query SQL Makes
    # Initialize counter for ID
    # First ID is first Make
    pass


def initSqlTables():
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
        print("Initialized SQL Tables " + sqlite3.version)
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
    initSqlTables()
    getMakes()