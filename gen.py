from feedgen.feed import FeedGenerator

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
    fd.logo(feed['avatarUrl'])
    fd.title(feed['name'])
    fd.link( href=f"https://kavins.rocks/channel/{feed['id']}")#get channel link
    fd.description(feed['description'])
    for item in feed['relatedStreams']:#relatedStreams = Videos on the channel
        fe = fd.add_entry()
        fe.title(item['title'])
        fe.link(href=item['url'])
        vidid = item['url'].split('v=')[1].split('&')[0]#get video id
        fe.description(makeDescription(description=item['shortDescription'],authors=item['uploaderName']))
        fe.enclosure(f"https://invidious.kavin.rocks/latest_version?id={vidid}&itag=140&listen=1",str(item['duration']),'audio/m4a') #get direct audio link
    return fd

def savefeed(feed):
    feed.rss_file('feed.rss')
