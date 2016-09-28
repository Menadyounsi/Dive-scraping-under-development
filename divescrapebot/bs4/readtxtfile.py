#This script will read through the scrapers output file of locations and depths

divedetails = open("divedetails.txt", "r")
dive_process = open("processed.txt", "w")

numentries = 0
divesite_list = []
depth_list = []

divesite = divedetails.readline().rstrip()

divesite_list.append(divesite)

while divesite != "":
    depth = divedetails.readline().rstrip()
    depth_list.append(depth)

    numentries += 1

    divesite = divedetails.readline().rstrip()
    divesite_list.append(divesite)

dive_process.write("\n".join(divesite_list))
dive_process.write("\n".join(depth_list))

divedetails.close()
dive_process.close()


print "You have %r dives in your list." % numentries

print divesite_list
