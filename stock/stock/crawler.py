import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import os
import traceback
import re
from datetime import datetime
import csv


stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
base_url = 'https://gupiao.baidu.com/api/stocks/stockdaybar?'


def getHTMLText(url, code='utf-8'):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = code
        return response.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a') # Return a list of tag a
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockInfo(stockCode):
    url = 'https://gupiao.baidu.com/stock/' + stockCode + '.html'
    headers = {
        'Host': 'gupiao.baidu.com',
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) \
            AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
        'X-Requested-With': 'XMLHttpRequest',
    }
    params = {
        'from': 'pc',
        'os_ver': '1',
        'cuid': 'xxx',
        'vv': '100',
        'format': 'json',
        'stock_code': stockCode,
        'step': '3',
        'start': '20161223',
        'count': '320',
        'fq_type': 'no',
        'timestamp': int(datetime.timestamp(datetime.now()))
    }
    try:
        requestURL = base_url + urlencode(params)
        response = requests.get(requestURL, headers=headers)
        if response.status_code == 200:
            return response.json() # return the json form of response
    except Exception as e:
        print(e)


def parse_response(json):
    data = json.get('mashData')
    infolist = []
    if data:
        for item in data:
            stockinfo = []
            kline = item.get('kline')
            stockinfo.append(item.get('date'))
            stockinfo.append(kline.get('open'))
            stockinfo.append(kline.get('close'))
            stockinfo.append(kline.get('high'))
            stockinfo.append(kline.get('low'))
            infolist.append(stockinfo)
        # print(infolist)
        return infolist
    else:
        pass


def main():
    slist = [] # a list of all stock code
    stockinfo = []
    getStockList(slist, stock_list_url)
    for stock in slist:
        print(stock)
        try:
            json = getStockInfo(stock)
            stockinfo = parse_response(json)
            if stockinfo is None:
                continue
        except KeyboardInterrupt as e:
            break
        with open(stock + '.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            for piece in stockinfo:
                writer.writerow(piece)


if __name__ == '__main__':
    main()
