## Script to generate a randomized chat.txt file for analysis ##

import os
import string
import random
import datetime
from emoji.unicode_codes import EMOJI_UNICODE
from faker import Faker


# Parameters for message generation
num_messages = 100000
num_emojis = 30
date_format = "[%Y-%m-%d, %I:%M:%S %p]"
date_start = "[2018-12-21, 2:55:51 AM]"
date_end = "[2020-04-04, 10:57:52 PM]"
resource_path = os.path.join("resources", "lorem-ipsum.txt")

# Create list of users (2 users currently supported)
list_users = ["User 1", "User 2"]


# Extract complete list of words from lorem ipsum text file
list_lorem_raw = []
with open(resource_path, "r") as f:
    for line in f:
        list_lorem_raw.extend(line.split())

# Ensure lorem ipsum text consists of unique words
list_lorem = list(set(list_lorem_raw))

# Get list of punctuation characters (excluding square bracket chars for less risk of datetime parse errors)
list_punc = [punc for punc in string.punctuation if (punc != "[" and punc != "]")]

# Create list of randomly-selected unicode emojis
list_emojis = random.sample(list(EMOJI_UNICODE.values()), num_emojis)

# Create basic list of slang words
list_slang = ['lool', 'looool', 'lmao', 'lmaoooo', 'lmaooo' 'wow', 'woooow', 'woowww', 'ha', 'hah', 'haha']

# Create list for image / video / link messages
list_msgtypes = ['\n\u200Eimage omitted\n', '\n\u200Evideo omitted\n', '\nhttps://www.google.com/\n',
                 '\nhttps://github.com/shenal-siri\n']

# Create basic list of stopwords
list_stopwords = ['a', 'am', 'are', 'but', 'for', 'I', 'it' ,'is', 'on', 'that', 'the', 'you', 'was', 'were']

# Create master list from which messages will be generated
list_master = list_lorem + list_punc + list_emojis + list_slang + list_msgtypes + list_stopwords


# Function to generate specified number of randomly distributed datetimes between start and end datetimes
def random_times(start, end, n, frmt):
    dt_start = datetime.datetime.strptime(start, frmt)
    dt_end = datetime.datetime.strptime(end, frmt)
    dt_delta = dt_end - dt_start
    return [(random.random() * dt_delta + dt_start) for _ in range(n)]

# Generate list of timestamp strings for output to text
timeseries = random_times(date_start, date_end, num_messages, date_format)
timeseries.sort()
timeseries = [dt.strftime(date_format) for dt in timeseries]


# Create Faker object to generate a random sentence using words from the master list
fake = Faker()

# Create the chat.txt file in the root folder
# Chat is generated line-by-line, matching the WhatsApp chat export format (for iOS)
with open("chat.txt", "w", encoding="utf-8") as f:
    for i in range(num_messages):

    	if i == 0:
    		output_msg = "Messages to this chat and calls are now secured with end-to-end encryption."
    	else:
    		output_msg = str(fake.sentence(ext_word_list=list_master, nb_words=10))

    	output_user = list_users[random.randint(0, len(list_users)-1)]
    	f.write(timeseries[i] + " " + output_user + ": " + output_msg + '\n')

print("Chat Generation Complete!")
