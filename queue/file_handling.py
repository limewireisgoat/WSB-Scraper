import os
import json

def check_for_dir():
    results = './results'
    posts = './posts'
    scores = './scores'
    if not os.path.exists(results):
        os.makedirs(results)
    if not os.path.exists(posts):
        os.makedirs(posts)
    if not os.path.exists(scores):
        os.makedirs(scores)

def write_json(filetype, dictionary, directory, day, month):
    filename = directory + filetype + str(month) + '-' + str(day) + '.json'
    with open(filename, 'w') as fp:
        json.dump(dictionary, fp, indent=1)

def write_csv(num_results, time):
    filename = 'times.csv'
    with open(filename, 'a') as fp:
        fp.write(str(num_results) + ',' + str(time) + '\n')