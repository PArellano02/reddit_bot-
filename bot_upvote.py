import praw
import random
import datetime
import time
from textblob import TextBlob

reddit = praw.Reddit('PedroCS40BOT')

submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/yx0xm8/masterfulcoolbots_zone/'
submission = reddit.submission(url=submission_url)

submission_list= list(reddit.subreddit('cs40_2022fall').hot(limit=50))
while True:
    try:
        submission = random.choice(submission_list)

        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        all_comments = []
        submission.comments.replace_more(limit=None , threshold=0)
        all_comments=submission.comments.list()

        print('len(all_comments)=',len(all_comments))
        count = 0
        for comment in all_comments:
            print(comment.body)
            if 'Trump' in comment.body:
                blob = TextBlob(comment.body)
                for sentence in blob.sentences:
                    print(sentence.sentiment.polarity)
                    if (sentence.sentiment.polarity) > 0.0:
                        comment.upvote()
                        count += 1
                        print(count)


    except Exception as e:
        pass