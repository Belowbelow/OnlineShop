from bs4 import BeautifulSoup
from urllib.request import urlopen

def getSoup(url):
    return BeautifulSoup((urlopen(url), 'html.parser'))

def getFirstPage(url):
    soup = getSoup(url)

    bookpics = []
    bookname = []
    #bookscore = []
    bookauthor = []
    bookpublisher = []
    bookprice = []
    bookblocks = soup.select("ul[class='bang_list clearfix bang_list_mode']")

    for bookblock in bookblocks:
        bookpics.append(bookblock.select("div[class='pic']"))[0].a.get("href")
        bookname.append(bookblock.select("div[class='name']"))[0].a.get_text()
        #bookscore.append(bookblock.select("div[class='star']"))[0]
        bookauthor.append(bookblock.select("div[class='publisher_info']"))[0].a.get_text()
        bookpublisher.append(bookblock.select("div[class='publisher_info']"))[1].a.get_text()
        bookprice.append(bookblock.select("div[clas='price']"))[0].p.span.get_text()
    
    for (pic, name, author, publisher, price) in zip(bookpics, bookname, bookauthor, bookpublisher, bookprice):
        print(pic, name, author, publisher, price)

url = "http://bang.dangdang.com/books/enewhotbooks/98.01.00.00.00.00-recent7-0-0-1-1"
getFirstPage(url)