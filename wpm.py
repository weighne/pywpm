import os
import datetime
import random
import json


def gen_phrase():
    with open('words.json','r') as in_file:
        words = json.load(in_file)
    x = 0
    phrase = []
    while x <= 10:
        wlist = words[random.choice(list(words.keys()))]
        index = random.randint(0, len(wlist)-1)
        phrase.append(wlist[index])
        x+=1
    return phrase


def calc_wpm(total_time, user_string, phrase):
    wpm = total_time * 6
    mistakes = 0
    user_words = user_string.split(' ')
    for x in range(len(phrase)):
        if user_words[x] == phrase[x]:
            continue
        else:
            mistakes+=1
    return wpm, mistakes


# with open('words.json','r') as in_file:
#     words = json.load(in_file)
phrase = gen_phrase()
print((' ').join(phrase))

input('Press any key to begin... Press \'Enter\' when complete\n')
start_time = datetime.datetime.now()
entry = str(input())
end_time = datetime.datetime.now()
total_time = (end_time - start_time).total_seconds()
wpm, mistakes = calc_wpm(total_time, entry, phrase)
print(f"WPM: {wpm}\nMistakes: {mistakes}")

# words[random list from dict][random value from list]
# print(words[random.choice(list(words.keys()))][random.randint(0, len(words[random.choice(list(words.keys()))])-1)])
