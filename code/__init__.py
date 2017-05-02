from text_analyzer import TextAnalyzer
from db_connection import DBConnection
import operator
from flask import Flask, render_template, request
import sys
import pymongo

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get text that the person has entered
        text = request.form['text-box']
        # text processing
        analyzer = TextAnalyzer(text)
        phrase = analyzer.text_analyzer()
        # save the results
        results = sorted(phrase.items(),key=operator.itemgetter(1),reverse=True)
        try:
            dbconnection = DBConnection()
            dbconnection.save_in_database(phrase)
            dbconnection.query()
        except:
            errors.append("Unable to add item to database.")
    return render_template('index.html', errors=errors, results=results)


if __name__ == "__main__":
    app.run()
    """
    analyzer = TextAnalyzer(sys.argv[1])
    phrase = analyzer.text_analyzer()
    dbconnection = DBConnection()
    dbconnection.save_in_database(phrase)
    dbconnection.query()
    print dbconnection.next_result()
    """
