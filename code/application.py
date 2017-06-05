from flask import Flask
from text_analyzer import TextAnalyzer
from db_connection import DBConnection
from flask import render_template, request
from url_scrapper import Scrapper
from pymongo.errors import ConnectionFailure
from collections import Counter
import urllib

app = Flask(__name__)


def process_text(string_of_articles):
    analyzer = TextAnalyzer(string_of_articles)
    result = analyzer.text_analyzer()
    return result


def upload_results_to_database(conn, short_date, long_date, result):
    error = None
    if conn is not None:
        try:
            # Generating dict.
            parsed_result = []
            parsed_result.append(str(short_date))
            parsed_result.append(str(long_date))
            parsed_result.append(result)

            dbconnection = DBConnection()

            dbconnection.save_in_database(parsed_result)
            dbconnection.query()
        except ConnectionFailure:
            error = "Unable to add item to database."
            print error
    else:
        error = "Database is down."
        print error
    return error


def create_results(phrase):
    results = []
    for word in sorted(phrase, key=phrase.get, reverse=True):
        aux = []
        aux.append(word)
        aux.append(phrase[word])
        results.append(aux)
    return results


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

        date = URL.split(' ')
        date[0] = str(date[0].lstrip('0'))

        if date[0].isdigit():
            date = str(date[0] + ' ' + date[1] + ' ' + date[2])
            print date

            conn = DBConnection.mongodb_conn()

            if conn is not None:
                dbconnection = DBConnection()
                if dbconnection.is_in_database(date) > 0:
                    dates = dbconnection.get_all_data_of_a_date_from_database(date)
                    aux_counter = Counter()
                    for element in dates.values():
                        aux = Counter(element)
                        aux_counter += aux
                    results = create_results(aux_counter)

                else:
                    error = 'Date not found on database.'
                    print 'error: ' + error
            else:
                error = "Database is down."
                print error
        # if data is a URL:
        else:
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
                short_date = str(short_date[1] + ' ' + short_date[2].lower() + ' ' + short_date[3])
                conn = DBConnection.mongodb_conn()

                if conn is not None:
                    dbconnection = DBConnection()
                    if dbconnection.check_date_in_db(short_date, long_date):
                        phrase = dbconnection.get_data_from_database(short_date, long_date)

                        results = create_results(phrase)

                    else:
                        # Scrapping web
                        scrapper.parse_xml()

                        # text processing
                        phrase = process_text(scrapper.string_of_articles)

                        results = create_results(phrase)

                        # upload results to database
                        error = upload_results_to_database(conn, short_date, long_date, phrase)

                        print 'error: ' + str(error)
                else:
                    error = "Unable to check if item is in database."
                    print error

                    # Scrapping web
                    scrapper.parse_xml()

                    # text processing
                    phrase = process_text(scrapper.string_of_articles)

                    results = create_results(phrase)

                    # upload results to database
                    error = upload_results_to_database(conn, short_date, long_date, phrase)

                    print 'error: ' + str(error)
            else:
                error = 'URL not valid'
                print error

    return render_template('index.html', results=results, error=error)

if __name__ == "__main__":
    app.run(host='localhost', port=8000)
