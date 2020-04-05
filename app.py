import pandas as pd
import pandas_datareader.data as web
import os
from extensions.candlestick import CandleStickExtension
from extensions.css import ImportCSSExtension
from datetime import datetime
from flask import Flask, render_template
from models.iex import IEXData
from flask import send_from_directory

# opening page displays overall market conditions
# dropdown of stock symbols or type one in
# service runs in background with buy/sell triggers
# paper trading
# backtester for strategy


app = Flask(__name__)
ALPHAVANTAGE_API_KEY='TOX9MEB3CYTJU3LK'
@app.route('/')
def index():
    df=web.DataReader("^DJI", 'av-daily', datetime(2019,1,1),api_key=os.getenv('ALPHAVANTAGE_API_KEY'))
    df.set_index( pd.to_datetime(df.index), inplace=True )
    df['Date'] = df.index
    df['Date'] = df['Date'].dt.strftime("%d-%b-%y")
    print(df.columns)
    df = df[['Date', 'open', 'high', 'low', 'close','volume']]
    df.columns = map(str.capitalize, df.columns)
    print(df.columns)
    print(df)
    s = '\\n'.join(','.join("%s" % x for x in y) for y in df[['Date', 'Open','High','Low','Close','Volume']].values)
    s = "Date,Open,High,Low,Close,Volume\\n" + s
    #s = df.to_csv()
    return render_template('index.html', symbol="Dow Jones Index", s=s)

@app.route('/iex')
def iex():
    result = IEXData.getData('intc')
    return(result)

@app.route('/<symbol>')
def draw(symbol):
    df=web.DataReader(symbol, 'av-daily', datetime(2019,1,1),api_key=os.getenv('ALPHAVANTAGE_API_KEY'))
    df.sort_index(ascending=False)
    df['Date'] = df.index
    df['Date'] = df['Date'].dt.strftime("%d-%b-%y")
    # call indicator/system analysis here
    #
    # df[['Open','High','Low','Close','Volume']].to_csv("static/data.csv", date_format="%d-%b-%y")
    s = '\\n'.join(','.join("%s" % x for x in y) for y in df[['Date', 'Open','High','Low','Close','Volume']].values)
    s = "Date,Open,High,Low,Close,Volume\\n" + s
    return render_template('index.html', symbol=symbol, s=s)

@app.route('/test/')
@app.route('/test/<symbol>')
def test(symbol=''):
    return render_template('stock.html', symbol=symbol)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


app.jinja_env.add_extension(CandleStickExtension)
app.jinja_env.add_extension(ImportCSSExtension)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
