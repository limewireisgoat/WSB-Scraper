import json
import psaw
from heapsort import MaxHeap
import time

from psaw import PushshiftAPI
api = PushshiftAPI()

import datetime
tz_utc = datetime.timezone.utc
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
for month in range(1,13):
    for day in range(1,days_in_month[month-1]+1):
        start_time=int(datetime.datetime(2021, month, day, 0, 0, 0, 0, tz_utc).timestamp())
        end_time=int(datetime.datetime(2021, month, day, 23, 59, 59, 99, tz_utc).timestamp())

        submissions = (api.search_submissions(after=start_time,
                                    before=end_time,
                                    subreddit='wallstreetbets',
                                    filter = ['title', 'selftext', 'num_comments', 'score']))


        wsb_dict = {"Data":[]}
        # make empty dictionary to hold key:value, cashtag:score
        daily_scores_dict = {}

        #initialize heap here
        heap = MaxHeap()

        start_time = 0

        for submission in submissions:
            if hasattr(submission, 'selftext'):
                not_del = "[deleted]" not in submission.selftext
                not_rm = "[removed]" not in submission.selftext
                not_emp = len(submission.selftext) != 0
                if not_del and not_rm and not_emp:
                    # ts = int(submission.created_utc)
                    # post_time = datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    dict = {"Title": None, "#Comments": None, "Score": None, "Symbols": None, "Selftext": None}
                    words = submission.selftext.split()
                    for word in submission.title.split():
                        words.append(word)
                    cashtags = list(set(filter(lambda word: word.lower().startswith("$"), words)))
                    cashtags = list(set(filter(lambda word: word[1:].isalpha(), cashtags)))
                    cashtags = list(map(lambda x:x.upper(), cashtags))
                    if len(cashtags) > 0:
                        dict["Title"] = submission.title
                        dict["#Comments"] = submission.num_comments
                        dict["Score"] = submission.score
                        dict["Symbols"]=cashtags
                        dict["Selftext"]=submission.selftext
                        wsb_dict["Data"].append(dict)

                        submission_score = 3 + submission.num_comments + submission.score

                        #Add a symbol to the dictionnary or update the symbol's score
                        start_time = time.time()
                        for symbol in cashtags:
                            if symbol not in daily_scores_dict:
                                daily_scores_dict[symbol] = submission_score
                            elif symbol in daily_scores_dict:
                                daily_scores_dict[symbol] += submission_score

        # start_time = time.time()
        # insert finalized values into the max heap through a for loop
        for symbol in daily_scores_dict:
            heap.push(daily_scores_dict[symbol])
        #then search for top 3 values                
        for i in range(1, 4):
            # print(heap.peek())
            value = heap.pop()
            for symbol in daily_scores_dict:
                if daily_scores_dict[symbol] == value:
                    print(symbol , ":" , value)
        print("--- %s seconds ---" % (time.time() - start_time))


        # print(heap.peek()) ## testing
        # JSON DATA DUMPING 
        filename = 'wsb' + str(month) + '-' + str(day) + '.json'
        with open(filename, 'w') as fp:
            json.dump(wsb_dict, fp, indent=1)
            json.dump(daily_scores_dict, fp, indent = 1)

    # print(cashtags_dict)

