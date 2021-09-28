import os
import datetime
import random
import json


def gen_phrase():
    with open('words.json','r') as in_file:
        words = json.load(in_file)
    x = 0
    phrase = []
    while x <= 20:
        wlist = words[random.choice(list(words.keys()))]
        index = random.randint(0, len(wlist)-1)
        phrase.append(wlist[index])
        x+=1
    return phrase


def calc_wpm(total_time, user_string, phrase):
    wpm = 60/total_time * len(phrase)  # extremely broken math
    mistakes = 0
    user_words = user_string.split(' ')
    for x in range(len(phrase)):
        try:
            if user_words[x] == phrase[x]:
                continue
            else:
                mistakes+=1
        except IndexError:
            mistakes+=1
            continue
    return wpm, mistakes


phrase = gen_phrase()
print((' ').join(phrase))

input('Press any key to begin... Press \'Enter\' when complete\n')
start_time = datetime.datetime.now()
entry = str(input())
end_time = datetime.datetime.now()
total_time = (end_time - start_time).total_seconds()
wpm, mistakes = calc_wpm(total_time, entry, phrase)
print(f"WPM: {wpm}\nMistakes: {mistakes}\nTime: {total_time}")

# words[random list from dict][random value from list]
# print(words[random.choice(list(words.keys()))][random.randint(0, len(words[random.choice(list(words.keys()))])-1)])
