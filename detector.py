import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


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


r = requests.get('https://medium.com/s/story/reflecting-on-my-failure-to-build-a-billion-dollar-company-b0c31d7db0e7')
a = text_from_html(r)
trait_yes = 0
trait_no = 0
for char in '.?"\':;,/()-_=+*%!@#~`|{}[]’':
    a = a.replace(char, " ")
a = a.split(' ')
for i in a:
    if i in ['i', 'I', 'me', 'Me', 'my', 'My', 'mine', 'Mine', 'we', 'We', 'us', 'Us', 'our', 'Our', 'ours', 'Ours']:
        trait_yes += 1
    elif i in ['you', 'You', 'your', 'Your', 'yours', 'Yours']:
        trait_no += 1
narcissist_ratio = (trait_yes / (trait_yes + trait_no)) * 100
narcissist_ratio = round(narcissist_ratio, 3)
print(narcissist_ratio)
