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

                        if os.path.exists(os.getcwd() + '/me.txt'):
                            with open('me.txt', "r") as my_name:
                                name = my_name.read()
                        else:
                            participants = conversation['participants']
                            counter = 0
                            print("- Setting Parameters -")
                            for participant in participants:
                                print("[%s] %s" % (counter, participant['name']))
                                counter += 1
                            index = input("Which of the participants are you?:\n")

                            if index.isdigit() and int(index) > 0 and int(index) < len(participants):
                                name = participants[int(index)]['name']
                                with open('me.txt', "w") as my_name:
                                    my_name.write(name)
                            else:
                                print("Invalid input")
                                break

                        participants = conversation['participants']
                        messages = conversation['messages']
                        for message in messages:
                            if message['sender_name'] == name and 'content' in message:
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
plt.show()
