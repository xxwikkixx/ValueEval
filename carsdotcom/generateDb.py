import pandas as pd
import bs4 as bs
import urllib.request
import sqlite3
from sqlite3 import Error
from pathlib import Path


def getMakes():
    carsdotcom = "https://www.cars.com/"
    # Source is the URL of the website that will be scraped
    source = urllib.request.urlopen(carsdotcom)
    # Soup stores the raw html page being scraped
    soup = bs.BeautifulSoup(source, 'lxml')

    # Finds the "select" drop down tag
    # select has the attribute of "name":"makeId"
    # Options variable is a list
    option = soup.find("select", {"name":"makeId"}).findAll('option')
    for val in option[1:]:
        print(val.get('value'), val.text)


def createConnection(dbFile):
    """
    create a database connection to the SQLite database specified by db_file
    :param dbFile: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


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


# TO-DO:
# Change the path to be generated without being hardcoded
if __name__ == "__main__" :
    dbPath = "../Databases/carsdotcom.db"

    