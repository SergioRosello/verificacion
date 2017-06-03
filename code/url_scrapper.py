import urllib2
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self, url):
        self.url = url
        self.list_of_articles = []
        self.string_of_articles = ''
        self.xml = self.get_rss()

    def check_date(self):
        soup = BeautifulSoup(self.xml,'html.parser')
        pubDate = soup.find('pubdate').string.strip()
        return pubDate

    def parse_xml(self):
        soup = BeautifulSoup(self.xml,'html.parser')
        for link in soup.find_all('item'):
            for article in link.find_all('content:encoded'):
                article = article.string.strip().encode("utf-8")
                article = BeautifulSoup(article, "html.parser")
                article = article.find('p').text
                self.list_of_articles.append(article.strip().encode("utf-8"))
                self.string_of_articles = self.string_of_articles + article.strip().encode("utf-8")
    """
    def save_to_file(self, output_file):
        with open(output_file, "w+") as text_file:
            for x in self.list_of_articles:
                text_file.write(x)
                text_file.write('\n')
    """

    def get_rss(self):
        return urllib2.urlopen(self.url).read()


"""
if __name__ == '__main__':
    url = 'http://ep00.epimg.net/rss/elpais/portada.xml'
    print 'Scrapping ' + url
    scrapper = Scrapper(url)
    print 'Parsing XML'
    scrapper.parse_xml()
    print 'Generating output: result.txt'
    scrapper.save_to_file("result.txt")
    update = scrapper.check_date()
"""