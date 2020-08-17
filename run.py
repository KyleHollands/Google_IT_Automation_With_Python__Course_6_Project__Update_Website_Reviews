#!/bin/usr/env python3

import requests
import os
import re

from requests.models import Response

# Follow structure:

# 1) List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the website
# 2) Loop through each file
# 3) Post the dictionary that's created from the reviews to the website

class run:
    def __init__(self):
        # Create review keys (labels) Format that will be used for all reviews.
        self.keys = ["title", "name", "date", "feedback"]
        
        # Set file pattern to look for (3 digits followed by an extension.)
        self.pattern = r'([0-9]{3}[.][a-z][.txt]+)'
        
        # Set origin of reviews in .txt files
        # self.origin = r"C:\Users\KyleHollands\OneDrive\Education\Coursera\Google IT Automation with Python\Automating Real-World Tasks with Python\Week 2\Resources\Process Text Files with Python Dictionaries and Upload to Running Web Service\data\feedback/"
        self.origin = r"/data/feedback/"
        
    def post_reviews(self):

        # Loop through each .txt review and convert it to a dictionary with key, value pairs associated with keys outlined above.
        for review in os.listdir(self.origin):
                if re.search(self.pattern, review):
                    key_count = 0
                    feedback = {}
                
                    with open(self.origin + review) as f:
                        for line in f:
                            value = line.strip()
                            feedback[self.keys[key_count]] = value
                            key_count += 1
                    print(feedback)
                
                # Post the reviews to the website django API.
                response = requests.post("http://35.202.51.144/feedback/", json = feedback)
        
        print(Response.request.body)
        print(Response.status_code)
        
run().post_reviews()