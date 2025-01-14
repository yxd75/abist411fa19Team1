# Project: Project Diamond
# Purpose Details: Retrieve a JSON payload from the internet
# Course: IST 411
# Author: Team 1
# Date Developed: 10/9/2019
# Last Date Changed:10/13/2019
# Rev:


import sys, urllib.request, json, config, datetime
from MongoSend import MongoSend
from mongo import MongoDB

class PayloadRetriever:
    # Default constructor declaring URL and PARAM going to be used
    def __init__(self):
        self.url = config.URL
        self.param = config.PARAM

    # Gets JSON payload using URL and PARAM
    def readAndDecodeJSON(self):
        try:
            with urllib.request.urlopen(self.url + self.param) as payload:
                jsonPayload = json.loads(payload.read().decode('utf-8'))
                # Log to App5 Success

                MongoDB.mongoInstance("Test", "Got Payload")
                return jsonPayload


        except Exception as e:
            print("error: %s" % e)
            # Log to App5 Failure
            MongoDB.mongoInstance("Test", "Failed to get Payload")
