import requests
from bs4 import BeautifulSoup as bs
import csv
from tqdm import tqdm

OUTPUT_FILENAME = "ufc_fight_outcomes.csv"

def getEvents():
    """Scrapes the ALL directory on the ufc stats page. Returns a list of all the links to the ufc stat pages for every event """
    page = requests.get("http://www.ufcstats.com/statistics/events/completed?page=all")
    soup = bs(page.content, "html.parser")

    html = list(soup.children)[10]
    table = html.find_all("table")
    table = list(table)[0]
    table_body = table.find_all("tbody")
    table_body = list(table_body)[0]
    ufc_events = table_body.find_all('tr')


    list_of_events = []
    for event in ufc_events:
        links = event.find_all("a")
        img = event.find_all("img")
        hasLink = True if len(links) == 1 else False
        futureEvent = True if len(img) > 0 else False
        if hasLink and not futureEvent:
            a_tag = links[0]
            list_of_events.append(a_tag["href"])
    return list_of_events

def scrapePage(url, sample_set):
    """Scrapes the individual ufc stat page that is passed as URL """
    page = requests.get(url)
    soup = bs(page.content, "html.parser")
    #print([type(item) for item in list(soup.children)])
    html = list(soup.children)[10] #grabs the tag type because that allows us to naviaget through the html document and extract other tags and text
    #print([type(item) for item in list(html.children)])
    body = list(html.children)[5]

    table = soup.find_all("table")
    table = list(table)[0]
    tbody = list(table)[3]
    fights = tbody.find_all("tr")
    winner = []
    loser = []
    title_fight_image = "http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/belt.png"
    for fight in fights:
        badBatch = False
        winner,loser = [], []
        categories = fight.find_all("td")
        for i, stat in enumerate(categories):
            
            if i == 0:
                winner.append(1)
                loser.append(0)
            if i == 1:
                names = stat.find_all("p")
                for i, name in enumerate(names):
                    if i == 0: winner.append(name.get_text().strip())
                    else: loser.append(name.get_text().strip())
                #if want to keep track of winners and losers per sample
                # winner = winner[len(winner)-1]
                # loser = loser[len(loser)-1]
                # winner.append(loser)
                # loser.append(loser)
            if i == 2:
                knockdown = stat.find_all("p")
                for i, kd in enumerate(knockdown):
                    if kd.get_text().strip() != '--':
                        if i == 0: winner.append(int(kd.get_text().strip()))
                        else: loser.append(int(kd.get_text().strip()))
                    else:
                        badBatch = True
                    
            if i == 3:
                strikes = stat.find_all("p")
                for i, strike in enumerate(strikes):
                    if strike.get_text().strip() != '--':
                        if i == 0: winner.append(int(strike.get_text().strip()))
                        else: loser.append(int(strike.get_text().strip()))
                    else:
                        badBatch = True
            if i == 4:
                takedowns = stat.find_all("p")
                for i, td in enumerate(takedowns):
                    if td.get_text().strip() != '--':
                        if i == 0: winner.append(int(td.get_text().strip()))
                        else: loser.append(int(td.get_text().strip()))
                    else:
                        badBatch = True                        
            if i == 5:
                submissions = stat.find_all("p")
                for i, sub in enumerate(submissions):
                    if sub.get_text().strip() != '--':
                        if i == 0: winner.append(int(sub.get_text().strip()))
                        else: loser.append(int(sub.get_text().strip()))
                    else:
                        badBatch = True
            if i == 6:
                weight_class = stat.find_all('p')
                images = stat.find_all("img")
                title_fight = False
                for img in images:
                    if img["src"] == title_fight_image:
                        title_fight = True
                for i in weight_class:
                    weight_class = i.get_text().strip()
                    winner.append(weight_class)
                    loser.append(weight_class)
                if title_fight:
                    winner.append(1)
                    loser.append(1)
                else:
                    winner.append(0)
                    loser.append(0)
            if i == 7:
                method = stat.find_all('p')
                for i,mtd in enumerate(method):
                    if i == 0:
                        method = mtd.get_text().strip()
                        winner.append(method)
                        loser.append(method)
                        break
            if i == 8:
                final_round = stat.find_all('p')
                for i in final_round:
                    final_round = i.get_text().strip()
                    winner.append(int(final_round))
                    loser.append(int(final_round))
        #print(winner, loser)
        if not badBatch:
            sample_set.append(winner)
            sample_set.append(loser)
        # else:
        #     print(url)
        
            
    return sample_set

ufc_events = getEvents()
print("Scraping all {} ufc events...".format(len(ufc_events)))
samples = [["Fight Outcome","Name","Knockdowns","Strikes","Takedowns","Submission Attempts","Weight Class","Title Fight","Outcome Method","Number of Rounds"]]
for event in tqdm(ufc_events):
    samples = scrapePage(event, samples)

with open(OUTPUT_FILENAME, 'w',newline = '') as csvfile:
    writer = csv.writer(csvfile)
    for i in samples:
        writer.writerow(i)
    csvfile.close()





