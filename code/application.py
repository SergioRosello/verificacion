from flask import Flask
from text_analyzer import TextAnalyzer
from db_connection import DBConnection
from flask import render_template, request
from url_scrapper import Scrapper
from pymongo.errors import ConnectionFailure
import urllib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None
    if request.method == "POST":

        # TODO: Menuda mierda!! (a ver si se puede hacer mejor (por ahora funciona))
        if request.form['text-box'] == '':
            return '', 204

        # get text that the person has entered
        URL = request.form['text-box']

        # Check if the URL is acceptable.
        valid_URL = False

        web = urllib.urlopen(URL)
        if web.getcode() < 400:
            valid_URL = True

        if valid_URL:

            scrapper = Scrapper(URL)

            # Retrieving Date
            long_date = str(scrapper.check_date())
            short_date = long_date.split(' ')
            short_date = str(short_date[1] + ' ' + short_date[2] + ' ' + short_date[3])
            conn = DBConnection.mongodb_conn()

            if conn is not None:
                try:
                    dbconnection = DBConnection()
                    if dbconnection.check_date_in_db(short_date, long_date):
                        phrase = dbconnection.get_data_from_database(short_date, long_date)

                        results = phrase

                    else:
                        # Scrapping web
                        scrapper.parse_xml()

                        # text processing
                        analyzer = TextAnalyzer(scrapper.string_of_articles)
                        result = analyzer.text_analyzer()
                        phrase = result[1]

                        for word in sorted(phrase, key=phrase.get, reverse=True):
                            aux = []
                            aux.append(word)
                            aux.append(phrase[word])
                            results.append(aux)

                        if conn is not None:
                            try:
                                # Generating dict.
                                parsed_result = []
                                parsed_result.append(str(short_date))
                                parsed_result.append(str(long_date))
                                parsed_result.append(results)

                                dbconnection = DBConnection()

                                dbconnection.save_in_database(parsed_result)
                                dbconnection.query()
                            except ConnectionFailure:
                                error = "Unable to add item to database."
                                print error
                        else:
                            error = "Database is down."
                            print error

                except ConnectionFailure:
                    error = "Unable to check if item is in database."
                    print error
            else:


                # Scrapping web
                scrapper.parse_xml()

                # text processing
                analyzer = TextAnalyzer(scrapper.string_of_articles)
                result = analyzer.text_analyzer()
                phrase = result[1]
                # print phrase
                for word in sorted(phrase, key=phrase.get, reverse=True):
                    aux = []
                    aux.append(word)
                    aux.append(phrase[word])
                    results.append(aux)

                if conn is not None:
                    try:
                        # Generating dict.
                        parsed_result = []
                        parsed_result.append(str(short_date))
                        parsed_result.append(str(long_date))
                        parsed_result.append(results)


                        dbconnection = DBConnection()

                        dbconnection.save_in_database(parsed_result)
                        dbconnection.query()
                    except ConnectionFailure:
                        error = "Unable to add item to database."
                        print error
                else:
                    error = "Database is down."
                    print error

        else:
            error = 'URL not valid'
            print error

    return render_template('index.html', results=results, error=error)

if __name__ == "__main__":
    app.run()
