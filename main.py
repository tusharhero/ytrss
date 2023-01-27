import feedparser as fp
from feedgen.feed import FeedGenerator

def getvidId(link):
    return link.split("v=")[1].split("&")[0]

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
        fe
        vidId = getvidId(item['link'])
        fe.enclosure(f"https://invidious.kavin.rocks/latest_version?id={vidId}&itag=140&listen=1",0,'audio/m4a')
    return fd


feed = fp.parse("https://pipedapi.kavin.rocks/feed/unauthenticated/rss?channels=UCPxMZIFE856tbTfdkdjzTSQ")
createfeed(feed).rss_file("ranveer.rss")
