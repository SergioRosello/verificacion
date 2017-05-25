from flask import Flask
from text_analyzer import TextAnalyzer
from db_connection import DBConnection
from flask import render_template, request
from url_scrapper import Scrapper

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == "POST":

        # TODO: Menuda mierda!! (a ver si se puede hacer mejor (por ahora funciona))
        if request.form['text-box'] == '':
            return '', 204

        # get text that the person has entered
        text = request.form['text-box']

        # Scrapping web
        print 'hola'
        scrapper = Scrapper(text)
        scrapper.parse_xml()


        # text processing
        print scrapper.string_of_articles
        print scrapper.list_of_articles
        analyzer = TextAnalyzer(scrapper.string_of_articles)
        result = analyzer.text_analyzer()
        phrase = result[1]
        for word in sorted(phrase, key=phrase.get, reverse=True):
            aux = []
            aux.append(word)
            aux.append(phrase[word])
            results.append(aux)

        try:
            dbconnection = DBConnection()
            dbconnection.save_in_database(result[0])
            dbconnection.query()
        except:
            print "Unable to add item to database."

    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run()
