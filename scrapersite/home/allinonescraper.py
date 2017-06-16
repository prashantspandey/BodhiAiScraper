import requests
import sys, os
import pickle
import json
from home.textsummarization import *
from more_itertools import unique_everseen
from home.datacleanndtv import *
from home.models import Post
from django.utils import timezone
from bs4 import BeautifulSoup

def start_posting(my_url,append_url,headDiv,headName,bodyDiv,bodyName):
    #my_url = 'http://zeenews.india.com/'
    #append_url = 'http://zeenews.india.com'
    print(my_url)
    print(append_url)
    print(headDiv,headName)
    print(bodyDiv,bodyName)

    all_sites = {}
    try:
        if os.path.exists('/home/prashant/Desktop/programming/projects/scrapewebsite/scrapewebsite/scrapersite/home/NewsData.json'):
            with open('/home/prashant/Desktop/programming/projects/scrapewebsite/scrapewebsite/scrapersite/home/NewsData.json','r') as rea:
                all_sites = json.load(rea)
        else:
            pass
    except Exception as e:
        print("Pickle doesn't exist")
    r = requests.get(my_url)
    soup = BeautifulSoup(r.content, "lxml")
    atags = soup.findAll('a')
    all_data = {}
    first_page_links = []
    spl = []
    for i in atags:
        try:
            link = i['href']
            if re.match(r'^/',link):
                link = append_url + link
            print('Looking at :'+link)
            first_page_links.append(link)
            secondr = requests.get(link)
            secondSoup = BeautifulSoup(secondr.content, "lxml")
            hTags = secondSoup.findAll('h1', {headDiv:headName})
            bodyTags = secondSoup.findAll('div', {bodyDiv:bodyName})
            head = []
            bodylist = []
            if hTags and bodyTags:
                for headline in hTags:
                    print(headline.text.strip())
                    head.append(headline.text.strip())
                for body in bodyTags:
                    bodylist.append(body.text.strip())
                bod = clean_article(bodylist) # cleans out all the html data 
                if link not in all_sites.keys() and link not in all_data.keys():
                    all_data[link] = {'Headline': head, 'Body': bod}
                    newPost = Post()
                    hh = all_data[link]['Headline']
                    bb = all_data[link]['Body']
                    summary = summarize_article(bod) #summarizes the article
                    summ = map(str, summary)
                    final_summary = ','.join(summ)
                    newPost.headline = ''.join(head) #save into database
                    newPost.body = ''.join(bod)
                    newPost.pub_date = timezone.now()
                    newPost.source = link
                    newPost.summary = final_summary
                    newPost.save()
                    all_data[link] = {'Headline': head, 'Body': bod, 'Summary': final_summary, 'Source': link}
                    try:
                        with open('/home/prashant/Desktop/programming/projects/scrapewebsite/scrapewebsite/scrapersite/home/NewsData.json', 'w') as fi:
                            json.dump(all_data, fi)
                            print('dumping')
                    except Exception as e:
                        print(str(e))



                else:
                    pass
        except Exception as e:
            #print(str(e))
             exc_type, exc_obj, exc_tb = sys.exc_info()
             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
             print(exc_type, fname, exc_tb.tb_lineno)

    first_page_links = list(unique_everseen(first_page_links))
    for i in first_page_links:
        if re.match(r'^/',i):
            i = append_url+i
            spl.append(i)
        else:
            spl.append(i)
    for j in spl:
        try:

            second_page = requests.get(j)
            second_page_soup = BeautifulSoup(second_page.content, "lxml")
            second_link = second_page_soup.findAll('a')
            for k in second_link:
                try:
                    link2 = k['href']
                    third_page = requests.get(link2)
                    third_page_soup = BeautifulSoup(third_page.content, "lxml")
                    h_second_Tags = third_page_soup.findAll('h1', {headDiv:headName})
                    body_second_Tags = third_page_soup.findAll('div', {bodyDiv:bodyName})

                    head = []
                    bodylist = []

                    if h_second_Tags and body_second_Tags:
                        for headline in h_second_Tags:
                            print('second page' + headline.text.strip())
                            head.append(headline.text.strip())
                        for body in body_second_Tags:
                            bodylist.append(body.text.strip())
                        bod = clean_article(bodylist)
                        if k not in all_sites.keys() and k not in all_data.keys():
                            newPost = Post()
                            summary = summarize_article(bod)
                            summ = map(str, summary)
                            final_summary = ','.join(summ)
                            newPost.headline = ''.join(head)
                            newPost.body = ''.join(bod)
                            newPost.pub_date = timezone.now()
                            newPost.source = str(k)
                            newPost.summary = final_summary
                            all_data[k] = {'Headline': head, 'Body': bod,
                                           'Summary': final_summary, 'source': k}
                            newPost.save()

                            # with open('NdtvJSONData.pkl','a') as fi:
                            #    pickle.dump(all_data,fi)
                            with  open('/home/prashant/Desktop/programming/projects/scrapewebsite/scrapewebsite/scrapersite/home/NewsData.json',
                                 'w') as fi2:
                                json.dump(all_data, fi2)


                        else:
                            pass
                except Exception as e:
                    print(str(e))
        except Exception as e:
            print(str(e))
