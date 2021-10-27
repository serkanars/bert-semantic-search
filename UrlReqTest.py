from gazpacho import get, Soup
import time


productTitle = list()

def get_article(url):

    """
    This function return title list.
    """
    
    urls = url
    html = get(urls)
    soup = Soup(html)
    titles = soup.find('h3', {'class': 'pn_v8'}, partial=True)

    titleList = list()

    for title in titles:
        titleList.append(title.text)


    return titleList

for i in range(1,51):
    print(f"{i}. sayfa için scrape işlemi başladı.")
    time.sleep(1)
    #if page number is one we write the main page for the machine
    if i == 1:
        productTitle.append(get_article("akakce.com/ocak.html"))
    #if page number is not one
    else:
        page = "akakce.com/ocak,"+str(i)+".html"
        productTitle.append(get_article(page))

    print(f"{i}. sayfa için scrape işlemi bitti.")

with open("./titles.txt", "a", encoding = "utf-8") as file:
    for k in productTitle:
        for l in k:
            try:
                file.write(str(l)+"\n")
            except:
                print("error")
    file.close()

