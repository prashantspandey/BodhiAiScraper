from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from home.articleProcess import *
from home.allinonescraper import *
from home.tweetsim import *
from home.tweets import *
from threading import Thread
from home.updateTweets import *
import threading
from multiprocessing import Queue
# Create your views here.

def index(request):
    at_home = True
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    websites = {}
    try:
        po = paginator.page(page)
    except PageNotAnInteger:
        po = paginator.page(1)
    except EmptyPage:
        po = paginator.page(paginator.num_pages)
    context = {'posts': po,'page':page, 'at_home': at_home}
    # add_post()
    #start_posting()
    return render(request, 'home/home.html', context)


def individual_post(request, slug):
    p = get_object_or_404(Post, headslug=slug)
    website = add_website()
    for i in website.keys():
        #start_posting(i,website[i]['Append_url'],website[i]['headDiv'],website[i]['headName'],website[i]['bodyDiv'],website[i]['bodyName'])
        #print(website[i],website[i]['Append_url'],website[i]['headDiv'],website[i]['headName'],website[i]['bodyDiv'],website[i]['bodyName'])
        print(i)


        context = {'post': p}
    return render(request, 'home/detail.html', context)


def sports_section(request):
    at_sports = True
    sports_articles = Post.objects.filter(category='0').order_by('-pub_date')
    context = {'sports_articles': sports_articles, 'at_sports': at_sports}
    return render(request, 'home/sports_section.html', context)


def worldNews_section(request):
    at_worldNews = True
    worldNews_articles = Post.objects.filter(category='2').order_by('-pub_date')
    context = {'worldNews_articles': worldNews_articles, 'at_worldNews': at_worldNews}
    return render(request, 'home/worldNews_section.html', context)


def indiaNews_section(request):
    at_indiaNews = True
    indiaNews_articles = Post.objects.filter(category='1').order_by('-pub_date')
    paginator = Paginator(indiaNews_articles, 5)
    pa = request.GET.get('indNew')
    try:
        po = paginator.page(pa)
    except PageNotAnInteger:
        po = paginator.page(1)
    except EmptyPage:
        po = paginator.page(paginator.num_pages)
    context = {'posts': po,'page':pa, 'at_indiaNews': at_indiaNews}
    return render(request, 'home/indiaNews_section.html', context)


def movies_section(request):
    at_movies = True
    movies_articles = Post.objects.filter(category='3').order_by('-pub_date')
    context = {'movies_articles': movies_articles, 'at_movies': at_movies}
    return render(request, 'home/movies_section.html', context)
def scienceandtech_section(request):
    at_scienceandtech = True
    scienceandtech_articles = Post.objects.filter(category='4').order_by('-pub_date')
    context = {'scienceTech_articles': scienceandtech_articles, 'at_scienceandtech': at_scienceandtech}
    return render(request, 'home/scienceandtech_section.html', context)

def add_website():
    website ={}
    website['http://zeenews.india.com/'] = {'Append_url':
                                            'http://zeenews.india.com','headDiv':'class','headName':'article-heading'
                                            ,
                                            'bodyDiv':'class','bodyName':'field-items'}
    website['http://www.ndtv.com/'] = {'Append_url':'http://www.ndtv.com','headDiv':'itemprop','headName':'headline','bodyDiv':'itemprop','bodyName':'articleBody'}
    #website['http://www.bbc.com/'] ={'Append_url':'http://www.bbc.com','headDiv':'class','headName':'story-body__h1','bodyDiv':'class','bodyName':'story-body'}
    return website
    



