#This is a beginner web scrape that you can try on websites you frequently visit.


from bs4 import BeautifulSoup as bs
import urllib



#AlJazeera
web_page = urllib.urlopen('http://www.aljazeera.com/topics/country/iraq.html').read()
soup = bs(web_page, "lxml")
print("________________Al Jazeera_______________")
def loop():
    for title in soup.find_all('h2'):
        print(("-")+title.get_text().encode("utf-8"))
AlJazeera_Data = loop()
print(AlJazeera_Data)
