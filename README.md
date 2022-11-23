# JB_M04r
Apparatus to parse RSS feeds, and loop process episodes with Whisper.


# Things to Try

- parse RSS feeds to retrieve episodes
- generate transcripts with whisper
- try free player that supports live transcript playback
- import RSS and transcript content into Solr and see if it produces anything useful. 


#scratch space
crawl_feed.py - retrieves show feed, filters out fields into json in txt files, dumps URLs to MP3s that we could start to process

python crawl_feed.py -d ~/dev/working/linux-unplugged -f https://linuxunplugged.com/rss
