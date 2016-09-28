from bs4 import BeautifulSoup
import requests

f = open('divedetails.txt', 'w')
url_page_1 = "https://en.divelogs.de/log/Mark_Gosling"
r = requests.get(url_page_1)
#r = urllib.urlopen("https://en.divelogs.de/log/henri61").read()
soup = BeautifulSoup(r.content)

#print soup.prettify()[0:1000]

"""dives = soup.find_all("td", class_="td2")
for result in dives:
    print result.text
#print type(dives)

for i in range(0, 20):
    display = str(dives[i])
    print dives[i]
    f.write(display)

for link in soup.find_all("a"):
    link.get("href")"""

g_data = soup.find_all("td", {"class": "td2"})

print "\n\n\n**************\n*"

to_print = []
try:
    for i in range(0,1000):
        #print "\nLocation:"
        #print g_data[((9*i)-7)].text
        location = g_data[((9*i)-7)].text
        to_print.append(location)
        #print "\nDepth:"
        #print g_data[((9*i)-6)].text
        depth = g_data[((9*i)-6)].text
        to_print.append(depth)

except:
    pass

print "\n\n\n\n\nBreak\n\n\n"
print to_print
to_save = "\n".join(to_print)
f.write(to_save)
f.close()
print "\n\nFinished"


#for item in g_data:
    #out = item.contents[0].text
    #print item.contents[0].text

for name in dir():
    if name.startswith("url_page_2"):
        exec("print "+name)
