import unicodedata

import requests, time
from bs4 import BeautifulSoup as BS
from selenium import webdriver

videos = {'VideoName':'','SubscriberCount': '', 'ChanelName':'','Views':''}

#url1  = input("Введите ссылку на канал: ")
url = 'https://www.youtube.com/c/PythonToday/videos'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)  # Можно ждать до загрузки страницы, но проще подождать 10 секунд, их хватит с запасом
html = driver.page_source
soup = BS(html, "html.parser")
id = 0

# def findChanelName(videos):
#     print("...Парсинг имени канала...")
#     ag1 = soup.find('yt-formatted-string',{'id':'text'}).text
#     videos['ChanelName'] = ag1
#     print(videos)


# def findsubscriberCount(videos):
#     print("...Парсинг числа подписечников...")
#     ag = soup.find("yt-formatted-string", {"id":'subscriber-count'}).text
#     clean_text = unicodedata.normalize('NFKC', ag)
#     videos['SubscriberCount'] = clean_text
#     print(videos)
#
# def find_first_video(videos):
#     all_videos = soup.find("a", {'id':'video-title'}).text
#     print(all_videos)
#     videos['VideoName'] = all_videos
#     print(videos)


def parse(videos, id):
    for videos["id"] in range(5):
        id = id + 1
        videos["id"] = id
        print(videos)


def main():
    try:
        parse(videos, id)
        # findChanelName(videos)
        # findsubscriberCount(videos)
        # find_first_video(videos)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()


