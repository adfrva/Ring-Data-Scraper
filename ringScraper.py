import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thePage = urllib.request.urlopen(url)
    soupData = BeautifulSoup(thePage, "html.parser")
    return soupData

fighterDataSaved = ""
div = []
divInd = 0
helper = 1
for year in range(1928, 2017):
    soup = make_soup("http://boxrec.com/media/index.php/The_Ring_Magazine%27s_Annual_Ratings:_" + str(year))

    for divisions in soup.findAll('th'):
        div.append(divisions.text.lstrip())
    for record in soup.findAll('td'):
        for index, data in enumerate( record.findAll('li') ):
            fighterData = ""
            ind = (index % 10) + 1
            fighterData = str(year) + "," + div[divInd].rstrip().lstrip() + "," + str(ind) + "," + data.text.rstrip().lstrip()
            fighterDataSaved = fighterDataSaved + "\n" + fighterData

            helper += 1
            if helper == 11:
                helper = 1
                divInd += 1
            #print(fighterData)

header="Year,Division,Position,Name"
file = open(os.path.expanduser("boxingRankings.csv"), "wb")
file.write(bytes(header, encoding="ascii", errors='ignore'))
file.write(bytes(fighterDataSaved, encoding="ascii", errors = 'ignore'))
#print(fighterDataSaved)
