import datetime
import os
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def calculate():
    # wunderground always starts from sunday
    today = datetime.date.today()
    lastweek = today - datetime.timedelta(days=7)
    result = compute_result([lastweek, today])

    return result


def compute_result(dts):
    # get rainfall in multiple dates and combine them
    times = []
    rainfalls = []
    for dt in dts:
        print('calculating rainfall for the week of', dt)
        date_str = dt.strftime('%Y-%m-%d')
        html = get_html(date_str)
        times_current, rainfalls_current = get_rainfall(html)
        times = times+times_current
        rainfalls = rainfalls+rainfalls_current

    # only reserve X days
    days = int(os.getenv('DAYS'))
    times = times[-days:]
    rainfalls = rainfalls[-days:]

    # combine to result
    result = ''
    for time, rainfall in zip(times, rainfalls):
        result = result+'{} : {} \n'.format(time, rainfall)

    return result


def get_html(date_str):
    # get html as BeautifulSoup object
    url_base = 'https://www.wunderground.com/history/weekly/us/nc/morrisville/KRDU/date/{}'
    url = url_base.format(date_str)

    # create a new browser session
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-default-apps')
    options.add_argument('--user-data-dir=/tmp')
    options.add_argument('--enable-automation=false')
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.get(url)

    delay = int(os.getenv('PAGE_LOADING_DELAY'))
    # wait x seconds until element is loaded
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'observation-table')))
    except TimeoutException:
        print('Weather page cannot load')
        sys.exit(1)

    # Selenium hands the page source to Beautiful Soup
    html = BeautifulSoup(driver.page_source, 'lxml')

    return html


def get_rainfall(html):
    # return date and rainfall for each day
    div = html.find('div', {'class': 'observation-table'})
    table = div.table
    headers = [td.text for td in table.thead.find_all('td')]

    # each header has a sub-table
    columns = table.tbody.tr.find_all('td')
    data = [[[td.text.strip() for td in tr.find_all('td')]
             for tr in column.find_all('tr')] for column in columns]
    # remove empty list
    data = [d for d in data if d]

    # get date
    times = [time[0] for index, time in enumerate(data[0]) if index != 0]
    # get rainfall
    rainfalls = [time[1] for index, time in enumerate(data[-1]) if index != 0]

    return times, rainfalls
