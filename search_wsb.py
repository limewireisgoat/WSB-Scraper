import psaw

from psaw import PushshiftAPI
api = PushshiftAPI()

import datetime

start_time=int(datetime.datetime(2020, 1, 1).timestamp())

submissions = (api.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter = ['title', 'selftext', 'num_comments']
                            ))
for submission in submissions:
    words = submission.selftext.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith("$"), words)))

    if len(cashtags) > 0:
        print(submission.description)
        print("Title :" + submission.title)
        print("# Comment: {}".format(submission.num_comments))
        print(cashtags)
    
   


    
