from bs4 import BeautifulSoup
import requests

#f = open('divedetails.txt', 'w')
#url_page_1 = "https://en.divelogs.de/log/Mark_Gosling"
#url_page_1 = url + "&page=" + int(2)
url_page_1 = "https://en.divelogs.de/log/Mark_Gosling"


def get_data_url(number_of_pages):
    for i in range(1, number_of_pages):
        if i == 1:
            print "exec %d" % i
        else:
            globals()['url_page_%d' % (i)] = ["https://en.divelogs.de/log/Mark_Gosling&page=%d" % (i)]
            print "exec %d" % (i)

        globals()['req_%d' % i] = ["requests.get(url_page_%d)" % i]
        print "req %d" % i

        globals()['soup_%d' % i] = ["BeautifulSoup(req%d.content)" % i]
        print "soup %d" % (i)

        globals()['g_data_%d' % i] = ["soup_%d.find_all('td', {'class': 'td2'})" % i]
        print "gdata %d" % (i)

"""

    for l in range(1, number_of_pages):
        globals()['req_%d' % (l)] = ["requests.get(url_page_%d)" % (l)]
        print "req %d" % (l)

    for k in range(1, number_of_pages):
        globals()['soup_%d' % i] = ["BeautifulSoup(req%d.content)" % k]
        print "soup %d" % i

    for m in range(1, number_of_pages):
        globals()['g_data_%d' % m] = ["soup_%d.find_all('td', {'class': 'td2'})" % m]
        print "gdata%d" % (m)

"""
get_data_url(5)

#depth = g_data_1[((9*1)-6)]

for item in g_data_1:
    try:
        item.contents.find_all('td', {'class': 'td2'}).text
    except:
        pass

print str(soup_1)
print str(g_data_1).replace('"', "")
location = "".join(eval(str(g_data_1)))
#loc2 = (location).text
print location
loc2 = eval(location)
print loc2
#(location.text)
#print loc2
#for j in range(1,5):
    #depth = eval("g_data_%d[((9*%d)-6)].text" % (j, j))
    #print str(depth)
"""
print url_page_2

to_print = []

#print get_data_url.soup_3

"""
#to_print = []

#for j in range(1, 5):
    #print "\nLocation:"
"""print g_data[((9*i)-7)].text
    location = (exec("(g_data_%d)[((9*%d)-7)].text" % (j, j))
    to_print.append(location)
    #print "\nDepth:"
    #print g_data[((9*i)-6)].text
    depth = exec("(g_data_%d)[((9*%d)-6)].text" % (j, j))
    to_print.append(depth)

print "\n\n\n\n******\n\n"

print to_print

print "\n\n***\n\n"
"""
