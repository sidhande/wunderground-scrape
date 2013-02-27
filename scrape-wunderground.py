# script to scrape temperature data from wunderground.com based on airport codes, years, months, and days
# currently set up to look at monthly data, but could be changed to daily by modifying the url


import csv
import time
import urllib2
from bs4 import BeautifulSoup

# set up airport code and city name dictionary
aircitydict = {
    'KBUF':'Buffalo',
    'KLGA':'New York',
    'KPHL':'Philadelphia',
    'KSFO':'San Francisco',
    'PAJN':'Juneau',
    'KSEA':'Seattle',
    'PHNL':'Honolulu',
    'KDEN':'Denver',
    'KIND':'Indianapolis',
    'KORD':'Chicago',
    'KHOU':'Houston',
    'KSTL':'St. Louis',
    'KTLH':'Tallahassee',
    'KLAX':'Los Angeles',
    'KPHX':'Phoenix',
    'KBOS':'Boston',
    'KICT':'Wichita',
    'KBOI':'Boise'
}

years = ['2012']
day = 10
weathnums = [range(2,11)]

# Iterate through airports, years, months, and day

for aircode, airname in aircitydict.iteritems():
    for y in years:
        for m in range(1, 13):

            timestamp = str(y) + str(m) + str(day)
            print "Getting data for " + aircode + " " + timestamp
            url = "http://www.wunderground.com/history/airport/" + str(aircode) + "/" + str(y) + "/" + str(m) + "/" + str(day) + "/MonthlyHistory.html"
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page)

            # Get weather info from page
            # soup = BeautifulSoup(page)
            # dayTemp = soup.body.nobr.b.string
            # dayTemp = soup.findAll(attrs={"class":"nobr"})[5].span.string


            # Format month for timestamp
            if (len(str(m)) < 2):
                mStamp = '0' + str(m)
            else:
                mStamp = str(m)

            # Format day for timestamp
            if (len(str(day)) < 2):
                dStamp = '0' + str(day)
            else:
                dStamp = str(day)

            # Build timestamp
            timestamp = y + "-" + mStamp

            # layout is: max max temp, avg max temp, min max temp, max mean temp, avg mean temp, min mean temp,
            # max min temp, avg min temp, min min temp
            weathdata = []
            weathdata = [airname, timestamp]
            for i in weathnums:
                for j in i:
                    weathdata.append(str(soup.findAll(attrs={"class":"nobr"})[j].span.string))

            # Write with CSV module
            f = csv.writer(open("wunder-data.csv","a"), delimiter=',')
            f.writerow(weathdata)

            # Close file
            # f.close()

            # Sleep for a moment to not overload wunderground
            time.sleep(2)
