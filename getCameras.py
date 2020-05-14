import requests
from bs4 import BeautifulSoup

URL = 'https://www.vegvesen.no/trafikkinformasjon/reiseinformasjon/Trafikkmeldinger/Webkamera'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('a', onclick=True)

ids = []
fails = []

for result in results:
    camId = result['onclick'].split("'")[1]
    try:
        camIdNum = int(camId)
        ids.append(camIdNum)
    except:
        fails.append(result['onclick'])

ids.sort()

print('fail example', fails[0])
print('id example', ids[0])

seen = set()
uniq = []
dupes = []

for id in ids:
    if id not in seen:
        uniq.append(id)
        seen.add(id)
    else:
        dupes.append(id)

print('duplicats:', len(dupes))
print('unique:', len(uniq))

print('webcams found:', len(ids))
print('failed to store', len(fails), 'webcams')

for id in ids:
    print('https://www.vegvesen.no/trafikkinformasjon/reiseinformasjon/Trafikkmeldinger/Webkamera?kamera='+str(id))
