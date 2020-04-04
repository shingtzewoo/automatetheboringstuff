#! python
# This program downloads all the links to the jobs you are searching for and stores them in a text file
# Usage: python3 jobSearcher.py

import sys
import pyinputplus as pyip
import requests, bs4
import datetime
import time

job = pyip.inputStr("What job are you looking for?\n")
location = pyip.inputStr("What location in Canada would like to search for jobs?\n")
jobSearch = open("jobSearch.txt", 'a')

# https://ca.indeed.com/jobs?q=POSITION+TITLE&l=LOCATION&jt=fulltime&start=PAGE
# Page goes up in 10s
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

    # checks whether you can apply for the job on the indeed portal or on the actual company's site, if it's the latter
    # it changes the link to go to company's site for that specific position
    link = result.select("div.jobsearch-SerpJobCard.unifiedRow.row.result > div.title a")
    for i in range(len(link)):
        link[i] = 'https://ca.indeed.com/' + link[i].get("href")

        jobSite = requests.get(link[i])

        try:
            jobSite.raise_for_status()
        except Exception as exc:
            print(f"There was a problem: {exc}")

        jobSiteSoup = bs4.BeautifulSoup(jobSite.text, 'html.parser')

        # checks whether it is Apply Now button or Apply on Company Site button
        if not jobSiteSoup.select("#viewJobButtonLinkContainers > div.icl-u-lg-block.icl-u-xs-hide.icl-u-lg-textCenter > a"):
            SoupElem = jobSiteSoup.select("#indeedApplyButtonContainer > span > div.jobsearch-IndeedApplyButton-buttonWrapper.icl-u-lg-block.icl-u-xs-hide > button > div")
        else:
            SoupElem = jobSiteSoup.select("#viewJobButtonLinkContainers > div.icl-u-lg-block.icl-u-xs-hide.icl-u-lg-textCenter > a")
        
        SoupElemText = SoupElem[0].getText()

        # checks whether the Apply button for the job links to the actual company's job application site
        if "Company" in SoupElemText:
            link[i] = SoupElem[0].get("href")
        else:
            continue

    for i in range(len(company)):
        lis = []
        lis.append(company[i].getText())
        lis.append(position[i].getText())
        lis.append(link[i])
        lis = '\n'.join(lis)
        jobSearch.write(lis)
        jobSearch.write("\n")

jobSearch.close()

