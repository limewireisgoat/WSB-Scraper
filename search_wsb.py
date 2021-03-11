import json
import psaw

from psaw import PushshiftAPI
api = PushshiftAPI()

import datetime

start_time=int(datetime.datetime(2020, 1, 1).timestamp())

submissions = (api.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter = ['title', 'selftext', 'num_comments', 'score'],
                            limit = 50))


dict = {"Title": None, "#Comments": None, "Score": None, "Symbols": None}
wsb_dict = {"Data":[]}


for submission in submissions:
    words = submission.selftext.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith("$"), words)))

    if len(cashtags) > 0:
        
        dict["Title"] = submission.title
        dict["#Comments"] = submission.num_comments
        dict["Score"] = submission.score
        dict["Symbols"]=cashtags
        wsb_dict["Data"].append(dict)



#JSON DATA DUMPING
with open('wsb.json', 'w') as fp:
    json.dump(wsb_dict, fp, indent=1)
    