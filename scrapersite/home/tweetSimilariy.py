#!/usr/bin/python3
from sklearn.feature_extraction.text import TfidfVectorizer
from models import Post
po = Post.objects.all()
kk = 0
while kk<2:
    for i in po:
        print(i)
        kk +=1
