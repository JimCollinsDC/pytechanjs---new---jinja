import os
import requests
# https://iexcloud.io/docs/api/#technical-indicators
# GET /stock/{symbol}/indicator/{indicator-name}
# /stock/twtr/indicator/sma?range=6m
# https://cloud.iexapis.com/stable/
# https://stackoverflow.com/questions/53075939/calling-rest-api-with-an-api-key-using-the-requests-package-in-python
# https://sandbox.iexapis.com/stable/stock/intc/quote?token=Tpk_b1f9bcd4842846d3a955e868cb93be47
#  https://cloud.iexapis.com/stable/stock/intc/quote?token=pk_fa7d171d4b384f2b87a2a7ceed9ec4f8
# prices for one month
# https://cloud.iexapis.com/stable/stock/INTC/chart/1m?token=pk_fa7d171d4b384f2b87a2a7ceed9ec4f8
class IEXData:
    def headers(apikey):
        apikey = os.environ.get('SANDBOXAPIKEY')
        return {'Authorization': 'Bearer {}'.format(apikey),
            'Content-Type': 'application/json'}

    def getData(symbol):
        # real or sandbox
        # get data
        # request string
        symbol = 'intc'
        #apikey = os.environ.get('SANDBOXAPIKEY')
        apikey = 'Tpk_b1f9bcd4842846d3a955e868cb93be47'
        baseurl = 'https://sandbox.iexapis.com/stable/'
        myrequest = 'stock/' + symbol + '/quote?token=' + apikey
        print('url:' + baseurl + myrequest)
        response = requests.get(baseurl + myrequest)
        print('response:' + response.text)

        # get indicator data
        json = response.text
        #print(response)
        #help(response)
        return json
