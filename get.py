import requests, json

def getvideodata(channelid):
    channeldata = json.loads(requests.get(f"https://pipedapi.kavin.rocks/channel/{channelid}").text)
    return channeldata
