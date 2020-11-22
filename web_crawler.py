import requests
from bs4 import BeautifulSoup
import re

#make the core spider
def trade_spider(max_pages):
    page =1
    count =1
    title_list=[]
    url_list=[]
    while page <= max_pages:
        # build the basic URL 
        print(page)
        
        if page >= 2:
            pagenumber = "/+" + str((page-1)*30)

        else:
            pagenumber = ""
            
        url = 'https://forum.lowyat.net/MusicPlayersandAudioAccessoriesGarageSales' + str(pagenumber)
        # print(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        # need to convert to beautiful soup object  
        soup = BeautifulSoup(plain_text,features="html.parser")#pass source code from the website, soup object can sort through

        for link in soup.findAll('a', {'href': re.compile("/topic/")}) : #attrs=
            #a means take attribute, in id unique, we have forum_topic_title
            #take everything inside the id: Forum_topic_title
            if len(str(link.get('href')))<15:
                href = "https://forum.lowyat.net"+link.get('href')
                title = link.string
                if (title == None):
                    for thing in link:#check this later, cannot extract info from the wts tag one.
                        title=thing.string
                    if (title == None):
                        for thing2 in thing:
                            title = thing2.string
                title_list.append(title)
                url_list.append(href)
                print(count)
                print(href)
                print(title)
                # get_single_item_data(href)
                count +=1

        page +=1
    return title_list,url_list

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    # need to convert to beautiful soup object  
    soup = BeautifulSoup(plain_text,features="html.parser")#pass source code from the website, soup object can sort through
    #change all html to text

    for item_name in soup.findAll('div',{"class":"maintitle"}):
        print(item_name)
        title=item_name.string
        if (title == None):
            for thing in item_name:#check this later, cannot extract info from the wts tag one.
                title=thing.string
            if (thing == None):
                for thing2 in thing:
                    title = thing2.string
        print(title)

all=[]
all = trade_spider(1)
print(all[0])
print(all[1])