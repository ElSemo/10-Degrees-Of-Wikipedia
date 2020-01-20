import pymysql

# SQL Database connection
connection = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='5565', db='mysql', charset='utf8')
crs = connection.cursor()
crs.execute('USE wiki')

# Retrieve URL from SQL table
def getUrl(pageId):
    crs.execute('SELECT url FROM pages WHERE id = %s', (int(pageId)))
    return crs.fetchone()[0]

# Retrieve the associated links a given URL can access in a list of table ID's
def getLinks(fromPageId):
    crs.execute('SELECT toPageId FROM links WHERE fromPageId = %s',
                (int(fromPageId)))
    if crs.rowcount == 0:
        return []
    return [links[0] for links in crs.fetchall()]

#Input source ID and target ID for a breadth first search in under 6 links.

def BFS(targetPageId, paths=[[1]]):
    newPaths = []
    for path in paths:
        links = getLinks(path[-1])
        for link in links:
            if link == targetPageId:
                return path + [link]
            else:
                newPaths.append(path+[link])
    return BFS(targetPageId, newPaths)

def stagesOfWikipedia(sourceId, targetId):
    paths = [[sourceId]]
    return BFS(targetId, paths)