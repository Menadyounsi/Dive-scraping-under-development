from bs4 import BeautifulSoup
import requests

#f = open('divedetails.txt', 'w')
#url_page_1 = "https://en.divelogs.de/log/Mark_Gosling"
#url_page_1 = url + "&page=" + int(2)
url_page_1 = "https://en.divelogs.de/log/Mark_Gosling"


def get_data_url(number_of_pages):
    for i in range(1, number_of_pages):
        if i == 1:
            #global url_page_1 = "https://en.divelogs.de/log/Mark_Gosling"
            print "exec %d" % i
        else:
            #exec('url_page_%d = "https://en.divelogs.de/log/Mark_Gosling&page=%d"' % (i, i)
            globals()['url_page_%d' % (i)] = ["https://en.divelogs.de/log/Mark_Gosling&page=%d" % (i)]
            print "exec %d" % (i)

    for l in range(1, number_of_pages):
        globals()['req_%d' % (l)] = ["requests.get(url_page_%d)" % (l)]
        #exec("req_%d = requests.get(url_page_%d)" % (l, l))
        print "req %d" % (l+1)

    for k in range(1, number_of_pages):
        globals()['soup_%d' % k] = ["BeautifulSoup(req%d.content)" % k]
        #exec("soup_%d = BeautifulSoup(req_%d.content)" % (k, k))
        print "soup %d" % (k)

    for m in range(1, number_of_pages):
        globals()['g_data_%d' % m] = ["soup_%d.find_all('td', {'class': 'td2'})" % m]
        #exec('g_data_%d = soup_%d.find_all("td", {"class": "td2"})' % (m, m))
        print "gdata %d" % (m)


get_data_url(5)
"""
print url_page_2

to_print = []

#print get_data_url.soup_3

"""
to_print = []

for j in range(1, 5):
    #print "\nLocation:"
    #print g_data[((9*i)-7)].text
    location = "(g_data_%d)[((9*%d)-7)].text" % (j, j)
    to_print.append(location)
    #print "\nDepth:"
    #print g_data[((9*i)-6)].text
    depth = "(g_data_%d)[((9*%d)-6)].text" % (j, j)
    to_print.append(depth)


print "\n\n\n\n******\n\n"

print to_print

print "\n\n***\n\n"

for name in dir():
    if name.startswith("url_page"):
        exec("print "+name)
