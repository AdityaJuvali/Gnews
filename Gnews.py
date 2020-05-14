"""
Created on Mon Feb 24 14:39:30 2020

@author: Aditya Juvali

Title: Google news search --> API
Description: Google news API has a search method that searches
            Google news top 10 articles using specific key word, start and end date
            to filter the search.
"""

# Import packages
from urllib import request
from bs4 import BeautifulSoup as soup
import datetime



class Gnews:
    def __init__(self):
        '''
        Description: Initialize instance by setting browser and user agents.
        '''
        self.time=[]
        self.ug="Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"
        self.hd={'User-Agent': self.ug}
        
        
    def search(self, key, startdate = None, enddate = None):
        '''
        Input:
        key[str] - Desired search string separated by spaces only.
        startdate[str] - Default None. Format YYYY-MM-DD. Startdate of the News article (not mandatory).
        enddate[str] - Default None. Format YYYY-MM-DD. Enddate of the News article (not mandatory).
        Description: 
        Uses request API to search on google.com with keyword and data range.
        Scrapes the 10 search links on Page 1 of the google news search and stores them.
        Returns: 
        links - list of upto 10 links of the google news search
        '''
        key = '+'.join(key.split(" "))
        if startdate != None:
            startdate=datetime.datetime.strptime(startdate, "%Y-%m-%d")
            st_mm=str(startdate.month)
            st_dd=str(startdate.day)
            st_yyyy=str(startdate.year)
        else:
            st_mm=''
            st_dd=''
            st_yyyy=''
            
        if enddate != None:
            enddate=datetime.datetime.strptime(enddate, "%Y-%m-%d")
            en_mm=str(enddate.month)
            en_dd=str(enddate.day)
            en_yyyy=str(enddate.year)
        else:
            en_mm=''
            en_dd=''
            en_yyyy=''
            
        # https://www.google.com/search?q=turkeycoup&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F2016%2Ccd_max%3A8%2F8%2F1%2F2016&tbm=nws    
        if (startdate == None) and (enddate != None):
            gnws_by_time="&tbs=cdr%3A1%2Ccd_min%3A" + "%2Ccd_max%3A" + en_mm + "%2F" + en_dd + "%2F" + en_yyyy
            gnws_url="https://www.google.com/search?q=" + key + gnws_by_time + "&tbm=nws"
            print("Pinging address: ", gnws_url)
        elif (startdate != None) and (enddate == None):
            gnws_by_time="&tbs=cdr%3A1%2Ccd_min%3A" + st_mm + "%2F" + st_dd + "%2F" + st_yyyy + "%2Ccd_max%3A"
            gnws_url="https://www.google.com/search?q=" + key + gnws_by_time + "&tbm=nws"
            print("Pinging address: ", gnws_url)
        elif (startdate != None) and (enddate != None):
            gnws_by_time="&tbs=cdr%3A1%2Ccd_min%3A" + st_mm + "%2F" + st_dd + "%2F" + st_yyyy + \
            "%2Ccd_max%3A" + en_mm + "%2F" + en_dd + "%2F" + en_yyyy
            gnws_url="https://www.google.com/search?q=" + key + gnws_by_time + "&tbm=nws"
            print("Pinging address: ", gnws_url)
        elif (startdate == None) and (enddate == None):
        # https://www.google.com/search?q=turkeycoup&tbm=nws&start=0
            gnws_url="https://www.google.com/search?q=" + key + "&tbm=nws&start=0"
            print("Pinging address: ", gnws_url)
           
        req=request.Request(gnws_url, headers=self.hd)
        self.open=request.urlopen(req)
        self.page=self.open.read()
        self.content = soup(self.page, "html.parser")
        result=self.content.find_all("div", class_="dbsr")
        
        links = []
        for item in result:
            links.append(item.find("a").get("href"))
            self.time
        self.open.close()
        return links