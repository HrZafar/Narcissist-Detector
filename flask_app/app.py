from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

app = Flask(__name__)


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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def my_form_post():
    try:
        html = request.form['text']
        r = requests.get(html)
        a = text_from_html(r)
        trait_yes = 0
        trait_no = 0
        for char in '.?"\':;,/()-_=+*%!@#~`|{}[]’':
            a = a.replace(char, " ")
        a = a.split(' ')
        for i in a:
            if i in ['i', 'I', 'me', 'Me', 'my', 'My', 'mine', 'Mine', 'we', 'We', 'us', 'Us', 'our', 'Our', 'ours',
                     'Ours']:
                trait_yes += 1
            elif i in ['you', 'You', 'your', 'Your', 'yours', 'Yours']:
                trait_no += 1
        narcissist_ratio = (trait_yes / (trait_yes + trait_no)) * 100
        narcissist_ratio = str(round(narcissist_ratio, 3))
        return 'narcissist ratio is ' + narcissist_ratio + '%'
    except Exception:
        return 'This URL is not available'


if __name__ == '__main__':
    app.run(debug=True)
