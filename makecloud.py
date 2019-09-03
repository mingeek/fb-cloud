import os
from os import path
import json
from tqdm import tqdm as pbar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_json():
    text = ""
    for root, dirs, files in os.walk('messages/inbox'):
        for dir in pbar(dirs, desc='Converting messages:'):
            curr_dir = os.getcwd() + '/messages/inbox/' + dir
            for file in os.listdir(curr_dir):
                if file.endswith(".json"):
                    with open(curr_dir + '/' + file, "r") as message_file:
                        conversation = json.load(message_file)
                        participants = conversation['participants']
                        messages = conversation['messages']e
                        for message in messages:
                            if message['sender_name'] == "Mingee" and 'content' in message:
                                text += (message['content'])


        all_messages = " ".join(sorted(text.split()))
        with open('output.txt', 'w') as output:
            output.write(all_messages)
        return #only go to 2nd level of dirs

create_json()

text = open(path.join(os.getcwd(), 'output.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(collocations=False).generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()