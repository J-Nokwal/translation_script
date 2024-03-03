import requests
import csv
from time import sleep
import json

lang = [
   "hi",	
   "mr",	
   "gu",	
   "te",	
   "ta",	
   "ml",	
   "kn",	
   "bn",
]
f = open("response.csv", "a")

with open('input.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        text=lines[0]
        print("converting",text)
        for l in lang:
            # url = 'https://www.google.com/inputtools/request?text=you&ime=transliteration_en_hi&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi&uv=are%3Aअरे-0-1%3A%3B0%3B0&cb=_callbacks_._2ltbqjibk'
            url = 'https://www.google.com/inputtools/request?text='+text+'&ime=transliteration_en_'+l+'&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi&uv=are%3Aअरे-0-1%3A%3B0%3B0&cb=_callbacks_._2ltbqjibk'
            x=requests.post(url)
            if x.status_code == 200:
                try:
                    first_quote = x.text.index('(')
                    json_data = json.loads(x.text[first_quote+1:-1])
                    f.write(json_data[1][0][1][0]+",")
                except (json.JSONDecodeError, KeyError, IndexError) as e:
                    print("Error in parsing response:", e)
                    print("Error in request",x.status_code,x.text,l)

            else:
                print("Error in request",x.status_code,x.text,l)
            sleep(0.5)
        f.write("\n")
