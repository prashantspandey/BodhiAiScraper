from django.db import models
from django.db.models.signals import post_save, pre_save
from home.articleProcess import *
from django.utils.text import slugify
from random import randint
from home.tweetsim import *
from home.tweets import *
# Create your models here.

class Post(models.Model):
    category_choices = (('0', 'Sports'), ('2', 'World-News'), ('1', 'India-News'), ('3', 'Entertainment and Movies'),
                        ('5', 'Uncategorized'), ('4', 'Science and Technology'))
    headline = models.CharField(max_length=500)
    body = models.TextField()
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=100, choices=category_choices, default='4')
    headslug = models.SlugField()
    source = models.CharField(max_length=500, null=True, blank=True)
    summary = models.CharField(max_length=1000, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.headslug:
            ranin = randint(0, 1000)
            self.headslug = slugify(self.headline[:45] + str(ranin))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.headline[:50]


class Tags(models.Model):
    posttag = models.ForeignKey(Post)
    tag = models.CharField(max_length=10)

class Tweets(models.Model):
    emotion_choices = (('-1','Negative'),('0','Neutral'),('1','Positive'))
    posttweet = models.ForeignKey(Post)
    tweet = models.CharField(max_length=400)
    emotion = models.CharField(max_length= 50,choices = emotion_choices)
    relavent = models.FloatField()
#def save_tweets(sender, instance, created, *args, **kwargs):
#    if created:
#        try:
#            tweets = find_tweets(instance.tag)
#            print(tweets)
#            for n, i in enumerate(tweets):
#                name = eval('"tweet"+str(n)')
#                name = Tweets(posttweet=instance.posttag, tweet=str(i))
#                name.emotion = '0'
#                name.relavent = sim(str(instance.posttag.headline),str(i))
#                name.save()
#        except Exception as e:
#            print(str(e))
#
#
#post_save.connect(save_tweets, sender=Tags)


def save_tags(sender, instance, created, *args, **kwargs):
    if created:
        tags = find_tags(instance.body)
        for n, i in enumerate(tags):
            name = eval('"tag"+str(n)')
            name = Tags(posttag=instance, tag=str(i))
            name.save()


post_save.connect(save_tags, sender=Post)


def save_category(sender, instance, *args, **kwargs):
    fet = sample_to_features(instance.body)

    category = predict_category(fet)
    print(category)
    if category == 0:
        instance.category = '0'
    elif category == 1:
        instance.category = '1'
    elif category == 2:
        instance.category = '2'
    elif category == 3:
        instance.category = '4'
    elif category == 4:
        instance.category = '3'
    else:
        instance.category = '5'


pre_save.connect(save_category, sender=Post)

