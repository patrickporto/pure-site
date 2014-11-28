from core.base import app
from core.shortcuts import render


@app.route(url='/hello')
def hello():
    context = {
        'text': 'Hello World'
    }
    return render('home.html', context)


@app.route(url='/')
def home():
    return '<button onclick="window.location=\'hello\'">Say Hello</button>'
