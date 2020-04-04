#! python
# This program downloads all the links to the jobs you are searching for and stores them in a text file

import sys
import pyinputplus as pyip
import requests, bs4
import datetime
import time

job = pyip.inputStr("What job are you looking for?\n")

location = pyip.inputStr("What location in Canada would like to search for jobs?\n")

# https://ca.indeed.com/jobs?q=POSITION+TITLE&l=LOCATION&jt=fulltime&start=PAGE
# Page goes up in 10s

jobSearch = open("jobSearch.txt", 'a')

for i in range(0, 10, 10):

    site = requests.get('https://ca.indeed.com/jobs?q=' + job + '&l=' + location + '&jt=fulltime&start=' + str(i))

    try:
        site.raise_for_status()
    except Exception as exc:
        print(f"There was a problem: {exc}")

    result = bs4.BeautifulSoup(site.text, 'html.parser')

    company = result.select("div.jobsearch-SerpJobCard.unifiedRow.row.result > div.sjcl > div > span.company")
    for i in range(len(company)):
        if '<a>' in company[i]:
            company[i] = [result.select("div.jobsearch-SerpJobCard.unifiedRow.row.result > div.sjcl > div > span.company > a")][i]
        else:
            continue

    position = result.select("div.jobsearch-SerpJobCard.unifiedRow.row.result > div.title a")
    link = result.select("div.jobsearch-SerpJobCard.unifiedRow.row.result > div.title a")

    for i in range(len(company)):
        lis = []
        lis.append(company[i].getText())
        lis.append(position[i].getText())
        lis.append(link[i].get("href"))
        lis = '\n'.join(lis)
        jobSearch.write(lis)
        jobSearch.write("\n")

jobSearch.close()

