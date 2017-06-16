import re
import pickle
import string
from more_itertools import unique_everseen


def clean_article(main_list):
    li = []
    # main_list = main_dict[link]['Body']
    reg = re.compile(r'\!function(.*?)\)\;', re.DOTALL)
    reg2 = re.compile(r'new\sfunction\(d\)(.*?)\(document\)\;', re.DOTALL)
    reg3 = re.compile(r'\$\(\sdocument\s\)(.*?)\}\)\;', re.DOTALL)
    reg4 = re.compile(r'\$\((.*?)\}\)\;', re.DOTALL)
    reg5 = re.compile(r'var\scurrentPhotoId(.*?)\}\)\;', re.DOTALL)
    reg6 = re.compile(r'function(.*?)\}', re.DOTALL)
    reg7 = re.compile(r'd\.src(.*?)\)\;', re.DOTALL)
    reg8 = re.compile(r'\}\selse(.*?)\}', re.DOTALL)
    reg9 = re.compile(r'if(.*?)1\)\;', re.DOTALL)
    reg10 = re.compile(r'\(\"datalayer(.*?)\}', re.DOTALL)
    reg11 = re.compile(r'Article', re.DOTALL)
    reg12 = re.compile(r'function(.*?)\)\;', re.DOTALL)
    reg13 = re.compile(r'function(.*?)\)\)\;', re.DOTALL)
    reg14 = re.compile(r'googletag(.*?)\)\;', re.DOTALL)


    for i in main_list:
        i = reg.sub('', i)
        i = reg2.sub('', i)
        i = reg3.sub('', i)
        i = reg4.sub('', i)
        i = reg5.sub('', i)
        i = reg6.sub('', i)
        i = reg7.sub('', i)
        i = reg8.sub('', i)
        i = reg9.sub('', i)
        i = reg10.sub('', i)
        i = reg11.sub(' Article ', i)
        i = reg12.sub('', i)
        i = reg13.sub('', i)
        i = reg14.sub('', i)
        # i = i.replace('\n','')
        # i = i.replace('',' ')
        li.append(i)

    return li


def clean_article2(link, main_dict):
    li = []
    main_list = main_dict[link]['Body']
    reg = re.compile(r'\!function(.*?)\)\;', re.DOTALL)
    reg2 = re.compile(r'new\sfunction\(d\)(.*?)\(document\)\;', re.DOTALL)
    reg3 = re.compile(r'\$\(\sdocument\s\)(.*?)\}\)\;', re.DOTALL)
    reg4 = re.compile(r'\$\((.*?)\}\)\;', re.DOTALL)
    reg5 = re.compile(r'var\scurrentPhotoId(.*?)\}\)\;', re.DOTALL)
    reg6 = re.compile(r'function(.*?)\}', re.DOTALL)
    reg7 = re.compile(r'd\.src(.*?)\)\;', re.DOTALL)
    reg8 = re.compile(r'\}\selse(.*?)\}', re.DOTALL)
    reg9 = re.compile(r'if(.*?)1\)\;', re.DOTALL)
    reg10 = re.compile(r'\(\"datalayer(.*?)\}', re.DOTALL)
    reg11 = re.compile(r'Article', re.DOTALL)
    reg12 = re.compile(r'function(.*?)\)\;', re.DOTALL)
    reg13 = re.compile(r'function(.*?)\)\)\;', re.DOTALL)

    somethingelse = []
    for i in main_list:
        i = reg.sub('', i)
        i = reg2.sub('', i)
        i = reg3.sub('', i)
        i = reg4.sub('', i)
        i = reg5.sub('', i)
        i = reg6.sub('', i)
        i = reg7.sub('', i)
        i = reg8.sub('', i)
        i = reg9.sub('', i)
        i = reg10.sub('', i)
        i = reg11.sub(' Article ', i)
        i = reg12.sub('', i)
        # i = i.replace('\n','')
        # i = i.replace('',' ')
        li.append(i)
    main_dict[link]['Body'] = li
    return main_dict
    # return main_list
