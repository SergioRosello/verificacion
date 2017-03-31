from text_analyzer import TextAnalyzer
from db_connection import DBConnection
import sys
import pymongo


if __name__ == "__main__":
    analyzer = TextAnalyzer(sys.argv[1])
    phrase = analyzer.text_analyzer()
    dbconnection = DBConnection()
    dbconnection.save_in_database(phrase)
    dbconnection.query()
    print DBConnection.next_result()
