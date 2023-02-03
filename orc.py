import get, gen
import tomlkit

def loadconfig(config="./config.toml"):
    f = open(config).read()
    configuration = tomlkit.parse(f)
    return configuration

def main():
    config = loadconfig()
    for channel in config['channels']:
        videodata = get.getvideodata(channel['channelid'])
        feed = gen.createfeed(videodata)
        gen.savefeed(feed)
