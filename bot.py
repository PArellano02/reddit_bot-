import praw
import random
import datetime
import time
import argparse 


parser = argparse.ArgumentParser(prog = 'reddit bot',description = 'Post random stuff',)
parser.add_argument('bot_term')
args = parser.parse_args()

# FIXME:
# copy your generate_comment function from the madlibs assignment here



# FIXME:
# connect to reddit 
reddit = praw.Reddit(args.bot_term)
madlibs = [
    "If [Everyone] in the [World] was [nicer] the [World] would be a [better] place. I would [Love] it if [Everyone] could be [nicer] to [others]!! <3",
    "I think [Everyone] should try [climbing]! [My best friend] told me to that [climbing] is [better1] than [volleyball] and he was [right]",
    "[Nike] is the the [best] brand for any [running] you want to do. I used [Nike] shoes for a [Marathon] and they worked [great]. I did not get any [injuries]",
    "If you go [climbing] three times every [week] you wont regret it. Your meantal health will [increase], and your phisical health will [increase]. [Everyone] should try it",
    "The first time [My best friend] took me [climbing], my life [changed]. Since then,  I have been [obsessed]. I can't go more than [week] without [climbing].",
    "[climbing] is the best sport ever! It is a lot [better1] than [volleyball]. [Everyone] should try it, do it alt least once a [week] and you will be [changed]"
    ]

replacements = {
    'Everyone' : ['everyone', 'people', 'everybody', 'every person' 'each person'],
    'World' : ['world', 'planet', 'globe'], 
    'better' :['better' , 'more pleasant' , 'happier'],
    'nicer' : ['nicer','kinder', 'warmer'],
    'Love' : ['love' , 'adore' , 'like' ,],
    'others' : ['others', 'other people', 'people around them'],
    'climbing' : ['climbing', 'running' , 'hiking', 'backpacking', 'swimming'],
    'My best friend' : ['my best friend', 'my coach', 'my sibling'],
    'better1' : ['beter','more fun', 'healthier'],
    'running' : ['running', 'jogging'],
    'volleyball' : ['volleyball', 'basketball' ,'tennis', 'soccer'],
    'right' : ['rioght', 'correct' , 'speaking the truth'], 
    'Nike' : ['Nike', 'Asics' , 'New Balance' , 'Adidas'],
    'best' : ['best' , 'greatest' , 'top'],
    'week' : ['week', 'couple of weeks', 'month' ],
    'increase' : ['increase', 'improve' ,'get better'],
    'changed' : ['changed', 'improved drastically', 'got a lot better'], 
    'obsessed' : ['obsedsed' , 'addicted', 'completely dependent on it'], 
    'injuries' : ['injuries', 'shin splints','hip injuries'], 
    'Marathon' : ['marathon' , '5K', '10K', 'halfm marathon'],
    'great' : ['great', 'awesome' ,'super duper awesome']
    }

 
def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
    '''
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace ('['+replacement+']', random.choice(replacements[replacement]) )

    # madlib = random.choice(madlibs)
    # madlib = madlib.replace('PYTHON', random.choice(replacements['PYTHON']))
    return madlib

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/yx0xm8/masterfulcoolbots_zone/'
submission = reddit.submission(url=submission_url) #or reddit[1].submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

submission_list= list(reddit.subreddit('cs40_2022fall').hot(limit=100))
for i in range(23) :# while True:
    submission_list= list(reddit.subreddit('cs40_2022fall').hot(limit=100))
    try:
        
        submission = random.choice(submission_list)
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        all_comments = []
        submission.comments.replace_more(limit=None)
        all_comments=submission.comments.list()

        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        for comment in all_comments:
            if comment.author != str(args.bot_term):
                not_my_comments.append(comment)

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (your bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)

        if has_not_commented:
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # a top level comment is created when you reply to a post instead of a message
            print(datetime.datetime.now(), 'top level comment made')
            submission.reply(body=generate_comment())
        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                bot_reply = False
                comment.replies.replace_more(limit=None)
                for reply in comment.replies:
                    if reply.author == str(args.bot_term):
                        bot_reply=True
                        break
                if not bot_reply:
                    comments_without_replies.append(comment)
                    comment.reply(body=generate_comment())
                
            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly;
            # many students struggle with getting a large number of "valid comments"
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # these will not be top-level comments;
            # so they will not be replies to a post but replies to a message
            try:
                selected_comment = random.choice(comments_without_replies)
                try:
                    selected_comment.reply(body=generate_comment())
                    
                except praw.exceptions.APIException:
                    print('deleted comment')
                    pass
            except IndexError:
                print('you replied to all the comments dawg')
                pass

        # FIXME (task 5): select a new submission for the next iteration;
        # your newly selected submission should be randomly selected from the 5 hottest submissions
        submission = random.choice(list(reddit.subreddit('cs40_2022fall').hot(limit=100)))

        pass

        # We sleep just for 1 second at the end of the while loop.
        # This doesn't avoid rate limiting
        # (since we're not sleeping for a long period of time),
        # but it does make the program's output more readable.
        time.sleep(5)
    
    except praw.exceptions.RedditAPIException as e:
        sleep_count = 0
        for exception in e.items:
            if exception.error_type == 'RATELIMIT':
                error_note = str(exception)
                print(error_note)

                if 'minute' in error_note:
                    delay = error_note.split('for ')[-1].split(' minute')[0]
                    delay_time = int(delay) * 60

                elif 'second' in error_note:
                    delay = error_note.split('for ')[-1].split(' second')[0]
                    delay_time = int(delay) * 60
            print('delay=', delay)
            time.sleep(delay_time)
            sleep_count +=1
            print('counter=', sleep_count)
    pass
