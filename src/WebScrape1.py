from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

# Connect to SQL
connection = pymysql.connect(host='127.0.0.1', user='root', passwd='5565',
                             db='mysql', charset='utf8')

crs = connection.cursor()
crs.execute('USE wiki')


# Insert page into database if page does not already exist
def insPage(url):
    crs.execute('SELECT * FROM pages WHERE url = %s', (url))
    if crs.rowcount == 0:
        crs.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        connection.commit()
        return crs.lastrowid
    else:
        return crs.fetchone()[0]

# Load all pages currently in database
def ldPages():
    crs.execute('SELECT * FROM pages')
    pages = [row[1] for row in crs.fetchall()]
    return pages

# Insert a link from one webpage to another
def insLink(fromPageId, toPageId):
    crs.execute('SELECT * FROM links WHERE fromPageId = %s ' 'AND toPageId = %s', (int(fromPageId), int(toPageId)))
    if crs.rowcount == 0:
        crs.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)',
                    (int(fromPageId), int(toPageId)))
    connection.commit()

# Browse wikipedia links up to a link of 5
def browseLinks(pageUrl, recursionLevel, pages):
    if recursionLevel > 3:
        return

    pageId = insPage(pageUrl)
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]

# After finding new links we add and search them
    for link in links:
        insLink(pageId, insPage(link))
        if link not in pages:
            pages.append(link)
            browseLinks(link, recursionLevel + 1, pages)

# Execute search on Canada
browseLinks('/wiki/Computer_science', 0, ldPages())
crs.close()
connection.close()
