import feedparser as fp
from feedgen.feed import FeedGenerator

def getvidId(link):
    return link.split("v=")[1].split("&")[0]

def makeDescription(link="", authors="unknown", description="description unavailable"):
    Desc = str(f" <a href='{link}'>link</a>\
            </br><b> {authors} </b> </br>\
            </br>{description}</br>\
            <i>\
            </br> fetched using Invidous and Piped. </br> \
            ytrss - a hack by <a href='mailto:tusharhero@sdf.org'>tusharhero</a>\
            </i>\
            ")
    return Desc

def createfeed(feed):
    fd = FeedGenerator()
    fd.logo(feed['feed']['icon'])
    fd.title(feed['feed']['title'])
    fd.link( href='http://example.com')
    fd.description("localhost")
    for item in feed['entries']:
        fe = fd.add_entry()
        fe.title(item['title'])
        fe.link(href=item['link'])
        vidId = getvidId(item['link'])
        fe.description(makeDescription(link=item['link'],authors=item['authors'][0]['name']))
        fe.enclosure(f"https://invidious.kavin.rocks/latest_version?id={vidId}&itag=140&listen=1",0,'audio/m4a')
    return fd
