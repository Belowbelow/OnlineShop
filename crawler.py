from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import chardet, random
import io, sys, codecs

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def getSoup(url):
    try:
        page = urlopen(url, timeout=10).read()
        if page[:3] == codecs.BOM_UTF8:
            page = page[3:]
        return BeautifulSoup(page, "html.parser")
    except BaseException as e:
        print(e)

def change(authors):
    a = ''
    for i in authors:
        a = a + i
    return(a)

#print(change(['aa', 'bb', 'cc']))

def change1(info):
    return ("'" + info + "'").replace(' ', '')

def save(num, bookname, price, author, introduction):
    f_path = "book.txt" 
    content = []
    with open(f_path, 'a', encoding='utf-8') as f:
        b_type = '计算机科学'
        store = random.randint(12, 15)
        sold = random.randint(2, 10)
        pic = "./pic/book_" + str(num) + ".jpg"

        data = change1(str(num)) + ',' + change1(bookname) + ',' + change1(str(price)) + ',' + change1(b_type) + ',' + change1(str(store)) + ',' + change1(str(sold)) + ',' + change1(change(author)) + ',' + change1(str(introduction)) + ',' + change1(pic)
        f.write(data + '\n')

def getFirstPage(url, num=1001):
    soup = getSoup(url)
    books = soup.select('div[class="xians-list"]')[0].select('ul')[0].select("li")
    book_images = []
    book_name = []
    book_author = []
    book_publisher = []
    book_price = []

    for book in books:
        images = book.table.select('tr')[0].td.a.img.get('file')
        book_images.append(images)

        name = book.table.select('tr')[1].td.a.get_text().replace('[按需印刷]', '').replace('[即时配发]', '')
        book_name.append(name)

        authors = []
        for i in book.table.select('tr')[2].td.select('a'):
            authors.append(i.get_text() + ' ')
        book_author.append(authors[:-1])

        book_publisher.append(authors[-1])

        price = book.table.select('tr')[4].select('td')[1].get_text().replace('\n', '').replace('\r', '').replace(' ', '')
        book_price.append(price.replace('定价：￥', ''))

    for x, y, z, p, l in zip(book_name, book_price, book_author, book_publisher, book_images):
        save(num, x, y, z, p)
        print(l)
        r = requests.get(l)
        imgPath = './pic/book_' + str(num) + '.jpg'
        with open(imgPath, 'wb') as p:
            p.write(r.content)
        num = num + 1


urls = ["http://product.china-pub.com/cache/rank3/ebook/day/rank_day_7_59_1.html",
        "http://product.china-pub.com/cache/rank3/ebook/day/rank_day_7_59_2.html",
        "http://product.china-pub.com/cache/rank3/ebook/day/rank_day_7_59_4.html",
        "http://product.china-pub.com/cache/rank3/ebook/day/rank_day_7_59_5.html"]

nums = [1001, 1021, 1041, 1061]

def main():
    for (url, num) in zip(urls, nums):
        try:
            print("Get info......")
            getFirstPage(url, num)
        except BaseException as e:
            print("Error: ", e)

def check():
    fPath = './book.txt'
    with open(fPath, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print('('+line+')')

main()
#check()