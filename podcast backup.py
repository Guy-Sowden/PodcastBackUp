import internetarchive
import requests
import os
import xml.etree.ElementTree as etree

def parseXML(podcastFeed): 
    XML = requests.get(podcastFeed, stream=True)
    tree = etree.parse(XML.raw)
    root = tree.getroot()
    print(root)
    episodesMp3 = []
    ## find all episodes
    for episode in root.findall("channel/item/enclosure"):
        url = episode.get("url")
        episodesMp3.insert(0,url)
        print(url)
def DownloadShow(showname):
    file_path ="./feeds/" + showname.replace(" ", "_")
    if (os.path.isdir(file_path)) == False:
        os.mkdir(file_path)
    
    

parseXML("https://feeds.megaphone.fm/mysteryshow")
DownloadShow("reply all")
