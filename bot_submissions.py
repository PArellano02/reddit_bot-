import praw
import random
import datetime
import time
import argparse

reddit = praw.Reddit('PedroCS40BOT')

choices = ['text' , 'link']

count = 0
while True:
    random_choice = random.choice(choices)
    try:
        if random_choice == 'text':
            submission = random.choice(list(reddit.subreddit('politics').new(limit=25)))
            reddit.subreddit('cs40_2022fall').submit(submission.title, selftext = submission.selftext)
            count += 1
            print('count=',count)
        if random_choice == 'link':
            submission = random.choice(list(reddit.subreddit('politics').hot(limit=None)))
            reddit.subreddit('cs40_2022fall').submit(submission.title, url = submission.url)
            count += 1
            print('count=',count)
    except praw.exceptions.APIException:
        print ('print sleeping for a few')
        time.sleep(5)