from candlestick import candlestick
import pandas as pd
import requests
import json
import helper
from datetime import datetime
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"

@app.route('/candlestick-patterns/<symbol>/<interval>')
def candlestick(symbol, interval):
    return json.dumps(helper.runner(symbol, interval))


if __name__ == '__main__':
    app.debug = True
    app.run()