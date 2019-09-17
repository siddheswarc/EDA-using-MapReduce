#!/usr/bin/env python2

import requests
import argparse
import time
import json
import StringIO
import gzip
import csv
import codecs
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

domain_list = ["https://www.medium.com/",
               "machinelearnings.co",
               "http://news.mit.edu/topic/artificial-intelligence2",
               "https://ai.google/research",
               "https://www.artificial-intelligence.blog/news/",
               "https://openai.com/blog/",
               "https://www.aitrends.com/",
               "https://machinelearningmastery.com/blog/"]

# list of available indices

index_list = [ "2019-04", "2019-09","2019-13"]
keyword_list = [
    ["machine", "learning"],
    ["artificial", "intelligence"],
    ["deep", "learning"],
    ["reinforcement", "learning"],
    ["self", "driving", "car"]
]

# Searches the Common Crawl Index for a domain.
def search_domain(domain):

    record_list = []

    print "[*] Trying target domain: %s" % domain

    for index in index_list:
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain

        response = requests.get(cc_url)
        if response.status_code == 200:

            records = response.content.splitlines()
            for record in records:
                rec = json.loads(record)
                rec_url = rec['url'].lower()
                for keywords in keyword_list:
                    if all([ 1 if key in rec_url else 0 for key in keywords ]):
                        record_list.append(rec)
                        break

    print "[*] Found a total of %d hits." % len(record_list)

    with open("hits.txt","a") as nhits:
        nhits.write(str(len(record_list)) + "\n")
    return record_list


# Downloads a page from Common Crawl
def download_page(record):

    offset, length = int(record['offset']), int(record['length'])
    offset_end = offset + length - 1
    prefix = "https://commoncrawl.s3.amazonaws.com/"

    resp = requests.get(
        prefix + record['filename'],
        headers={'Range': 'bytes={}-{}'.format(offset, offset_end)}
    )

    raw_data = StringIO.StringIO(resp.content)
    f = gzip.GzipFile(fileobj=raw_data)

    data = f.read()
    response = ""
    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass
    return response


# Extract links from the HTML
def extract_external_links(html_content):
    soup = BeautifulSoup(html_content)
    with open("links.txt","a") as links:
        para_tag = soup.find_all('p')
        for tag in para_tag:
            links.write(str(tag.prettify().encode("utf8"))+"\n")

record_list = []
for domain in domain_list:
    record_list.append(search_domain(domain))

for records in record_list:
    for record in records:
        html_content = download_page(record)
        extract_external_links(html_content)
