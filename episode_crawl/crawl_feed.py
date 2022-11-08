import argparse
import requests
from requests.auth import HTTPBasicAuth
import feedparser
import os
import json
import hashlib
from datetime import datetime
from pprint import pprint
import ipdb

def main(args):
    #FILE_PATH = os.path.dirname(os.path.abspath(__file__))  #fine for development, but change to http pub dir
    file_path = args.destination
    rss_feed_url = args.feed

    feed = feedparser.parse(rss_feed_url)
    pprint(feed.keys())
    url_list = []
    if len(feed["entries"]) > 0:
      for episode in feed["entries"]:
            export_fields = {}
            export_fields["show"] = feed["feed"]["title"]
            export_fields["ep_title"] = episode["title"]
            export_fields["summary"] = episode["summary"]
            export_fields["published"] = episode["published"]
            export_fields["links"] = episode["links"]
            export_fields["episode"] = episode["link"].split('/')[-1]

            pprint(export_fields)
            filename = feed["feed"]["title"].lower() + '_' + str(export_fields["episode"])
            with open(file_path + '/' + filename + '.txt', 'w') as f:
                json.dump(export_fields, f, ensure_ascii=False)
            
            for link in export_fields["links"]:
                if link["type"] == "audio/mp3":
                    url_list.append(link["href"])

    else:
      print("Found nothing in feed.  That's kinda weird.")

    filename = feed["feed"]["title"].lower() + '_whisper_list'
    with open(file_path + '/' + filename + '.txt', 'w') as f:
                json.dump(url_list, f, ensure_ascii=False)
    ipdb.set_trace()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download latest feed and generate local copy of info')
    parser.add_argument('-d', '--destination', type=str, default=os.path.dirname(os.path.abspath(__file__)), help='Destination Directory', required=False)
    parser.add_argument('-f', '--feed', type=str, required=True)
    args = parser.parse_args()
    main(args)