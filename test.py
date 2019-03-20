import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import matplotlib.pyplot as plt


def word_occurences(text):
    counts = dict()
    words = text.split(' ')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return len(counts)


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body.text, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def count_score(text, word):
    score = 0
    for i in word:
        score += text.count(i)
    return score


type1 = [' we ', ' me ', ' i ', ' us ', ' our ']

type2 = [' you ', ' yours ']

positive = ['because', 'imagine', 'now', 'please', 'thank you', 'names', 'control', 'free', 'instantly',
            'new', 'suddenly', 'now', 'announcing', 'introducing', 'improvement', 'amazing', 'sensational',
            'remarkable', 'revolutionary', 'startling', 'miracle', 'magic', 'offer', 'quick', 'easy',
            'wanted', 'challenge', 'compare', 'bargain', 'hurry']

negative = ['don’t']

coherence = ['but', 'therefore', 'so', 'as a result', 'that is why', 'consequently', 'accordingly',
             'because', 'caused by', 'consequently', 'due to', 'for this reason', 'since', 'therefore', 'thus']

exclusivity = ['members only', 'login required', 'class full', 'membership now closed', 'ask for an invitation',
               'apply to be one of our beta testers', 'exclusive offers', 'become an insider', 'be one of the few',
               'get it before everybody else', 'be the first to hear about it', 'only available to subscribers']

scarcity = ['limited offer', 'supplies running out', 'get them while they last', 'sale ends soon', 'today only',
            'only 10 available', 'only 3 left', 'only available here', 'double the offer in the next hour only']

safe = ['anonymous', 'authentic', 'backed', 'best-selling', 'cancel anytime', 'certified', 'endorsed', 'guaranteed',
        'ironclad', 'lifetime', 'moneyback', 'no obligation', 'no questions asked', 'no risk', 'no strings attached',
        'official', 'privacy', 'protected', 'proven', 'recession-proof', 'refund', 'research', 'results', 'secure',
        'tested', 'try before you buy', 'verify', 'unconditional']

shareable = ['secret', 'tell us', 'inspires', 'take', 'help', 'promote', 'increase', 'create', 'discover']

power = ['improve', 'trust', 'immediately', 'discover', 'profit', 'learn', 'know', 'understand', 'powerful', 'best',
         'win', 'hot special', 'more', 'bonus', 'exclusive', 'extra', 'you', 'free', 'health', 'guarantee', 'new',
         'proven', 'safety', 'money', 'now', 'today', 'results', 'protect', 'help', 'easy', 'amazing', 'latest',
         'extraordinary', 'how to', 'worst', 'ultimate', 'hot', 'first', 'big', 'anniversary', 'premiere', 'basic',
         'complete', 'save', 'plus', 'create']

r = requests.get('https://medium.com/s/story/reflecting-on-my-failure-to-build-a-billion-dollar-company-b0c31d7db0e7')
a = text_from_html(r).lower()

words = a.count(' ') + 1
unique_words = word_occurences(a)
ttr = unique_words / words
positive_score = count_score(a, positive)
negative_score = count_score(a, negative)
coherence_score = count_score(a, coherence)
exclusivity_score = count_score(a, exclusivity)
scarcity_score = count_score(a, scarcity)
shareable_score = count_score(a, shareable)
power_score = count_score(a, power)

print('total words=', words)
print('unique_words=', unique_words)
print('ttr=', ttr)
print('positive_score=', positive_score)
print('negative_score=', negative_score)
print('coherence_score=', coherence_score)
print('exclusivity_score=', exclusivity_score)
print('scarcity_score=', scarcity_score)
print('shareable_score=', shareable_score)
print('power_score=', power_score)

names = ['positive', 'negative', 'coherence', 'exclusivity', 'scarcity',
         'shareable', 'power']
values = [positive_score, negative_score, coherence_score, exclusivity_score, scarcity_score, shareable_score,
          power_score]
plt.bar(names, values)
plt.show()
