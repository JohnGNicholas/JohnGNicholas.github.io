#!/usr/bin/env python3

import feedparser
import bs4

# Download and parse the RSS document
feed = feedparser.parse("https://news.ycombinator.com/rss")

# Open the frame document in BeautifulSoup
with open("feedTemplate.html") as fin:
  txt = fin.read()
  soup = bs4.BeautifulSoup(txt,"html.parser")

# Insert new links into the file for each link in the RSS document
for i in list(range(len(feed.entries))):
  entry = feed.entries[i]
  # Create a new paragraph
  paragraph = soup.new_tag("p")
  # Create a new hyperlink with our information
  hyperlink = soup.new_tag("a", href=entry.link)
  hyperlink.append(entry.title)
  # Place the link into the paragraph and the paragraph into the body
  paragraph.append(hyperlink)
  soup.body.append(paragraph)

# Print the BeautifulSoup object into the desired file to be displayed on the site
with open("feed.html", "w") as fout:
  # Write the entire document
  fout.write(str(soup.prettify()))
