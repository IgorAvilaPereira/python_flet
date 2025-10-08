import feedparser

# Replace with the actual URL of the RSS feed you want to read
rss_feed_url = "https://ifrs.edu.br/riogrande/feed/" 

feed = feedparser.parse(rss_feed_url)

print(f"Feed Title: {feed.feed.title}\n")

for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    if hasattr(entry, 'summary'):
        print(f"Summary: {entry.summary}")
    if hasattr(entry, 'published'):
        print(f"Published: {entry.published}")
    print("-" * 30)
