from candlestick import candlestick
import pandas as pd
import requests
import json
from datetime import datetime


def getActiveCandleStick(output):
    data = output.to_json()

    python_obj = json.loads(data)
    mydict = dict(python_obj["T"])

    if len(mydict) == 0:
        return False

    now = datetime.now()
    timestamp = int(datetime.timestamp(now))
    lastDate = int(list(mydict.values())[-1]) / 1000
    if lastDate >= (timestamp - 3600):
        return True
    else:
        return False

def runner(symbol, interval):
    candles = requests.get('https://api.binance.com/api/v1/klines?symbol='+symbol+'&interval='+interval)
    candles_dict = candles.json()
    candles_df = pd.DataFrame(candles_dict,
                            columns=['T', 'open', 'high', 'low', 'close', 'V', 'CT', 'QV', 'N', 'TB', 'TQ', 'I'])

    candles_df['T'] = pd.to_datetime(candles_df['T'], unit='ms')

    listIndicators = []

    target = 'InvertedHammer'
    candles_df = candlestick.inverted_hammer(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'DojiStar'
    candles_df = candlestick.doji_star(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'BearishHarami'
    candles_df = candlestick.bearish_harami(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'BullishHarami'
    candles_df = candlestick.bullish_harami(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'DarkCloudCover'
    candles_df = candlestick.dark_cloud_cover(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'Doji'
    candles_df = candlestick.doji(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'DragonflyDoji'
    candles_df = candlestick.dragonfly_doji(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'HangingMan'
    candles_df = candlestick.hanging_man(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'GravestoneDoji'
    candles_df = candlestick.gravestone_doji(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'BearishEngulfing'
    candles_df = candlestick.bearish_engulfing(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'BullishEngulfing'
    candles_df = candlestick.bullish_engulfing(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)   

    target = 'Hammer'
    candles_df = candlestick.hammer(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'MorningStar'
    candles_df = candlestick.morning_star(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'MorningStarDoji'
    candles_df = candlestick.morning_star_doji(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'PiercingPattern'
    candles_df = candlestick.piercing_pattern(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'RainDrop'
    candles_df = candlestick.rain_drop(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'RainDropDoji'
    candles_df = candlestick.rain_drop(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'Star'
    candles_df = candlestick.star(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    target = 'ShootingStar'
    candles_df = candlestick.shooting_star(candles_df, target=target)
    output = candles_df[candles_df[target] == True][['T']]
    if getActiveCandleStick(output):
        listIndicators.append(target)

    return listIndicators