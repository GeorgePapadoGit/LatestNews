import requests
from bs4 import BeautifulSoup
import xlsxwriter
import sys


def make_dictionary(dict_title, dict_summary, dict_link):
    dict_news = {
        "title": dict_title,
        "summary": dict_summary,
        "link": dict_link
    }
    return dict_news


user_choice = input('Hello! Tell me a topic you wanna see some news \n')

site = requests.get('https://www.in.gr/latestnews/').text
soup = BeautifulSoup(site, 'html.parser')
all_news = soup.find('div', class_='flexgrid flexwrap rowlr').find_all('a')
list_news = []

for news in all_news:
    title = news.h3.text
    paragraph = news.p.text
    link = news.get('href')
    if user_choice in title.lower():
        list_news.append(make_dictionary(title, paragraph, link))


workbook = xlsxwriter.Workbook("latestNews.xlsx")
sheet = workbook.add_worksheet()

cell_format = workbook.add_format({'bold': True})
sheet.write('A1', 'Title', cell_format)
sheet.write('B1', 'Summary', cell_format)
sheet.write('C1', 'Link', cell_format)


for item in range(len(list_news)):
    sheet.write(item + 1, 0, list_news[item].get('title'))
    sheet.write(item + 1, 1, list_news[item].get('summary'))
    sheet.write(item + 1, 2, list_news[item].get('link'))
print('Great! Your excel file is ready !')
workbook.close()


