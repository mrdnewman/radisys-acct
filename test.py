import fileinput


#file = '/home/radisys/dev/onlab_develop_pod.yml'
import sys

myip = 'foobar'
rep = {'zero': 0,'temp': 'bob','garbage': 'nothing'}

for line in sys.stdin:
    for k, v in rep.iteritems():
        line = line.replace(k, v)
    print line

x = fileinput.input('file.txt',inplace=1)
for line in x:
    line = line.replace('10.1.1.1','%s') % myip
    print line

x.close()

for k, v in rep:
    print k, v


myseed = '12.12.12.133'
myfabip = '1.1.1.1'
boo = '123'
foo = '456'
doo = '789'

myconfig = 'onlab_develop_pod.yml'

rep = {'myseedip':'%s' % myseed,
       'myfrabricip':'%s' % myfabip,
       'mymanip':'%s' % boo,
       'myextip':'%s' % foo,
       'myextiface':'%s' % doo}

#for key, value in sorted(rep.keys()):
#    print key, value

#sorted(mydict.iterkeys()):


textfile = open("%s" % myconfig,'rb')



for lines in textfile.xreadlines():
    for eachkey in rep.keys():
        if eachkey in lines:
            print lines
        else:
            continue

# Close text.txt file
textfile.close()


with open(myconfig, 'r+') as freplace:
#x = fileinput.input('%s' % myconfig, inplace=1)

    for lines in freplace.readlines():
        for eachkey in rep.keys():
            if eachkey in lines:
                # print lines
                # print rep[eachkey]
                text = lines.replace(eachkey, rep[eachkey])
                   # print (eachkey, rep[eachkey])
                freplace.write(text)

            else:
                continue

# Close text.txt file
freplace.close()

### This WORKS!!!!!
import os
import sys
import fileinput

os.system('clear')

myseed = '12.12.12.133'
myfabip = '1.1.1.1'
boo = '123'
foo = '456'
doo = '789'

myconfig = 'onlab_develop_pod.yml'

rep = {'myseedip':'%s' % myseed,
       'myfrabricip':'%s' % myfabip,
       'mymanip':'%s' % boo,
       'myextip':'%s' % foo,
       'myextiface':'%s' % doo}



with open(myconfig, 'r+') as fd:

    # read in all the data
    text = fd.read()

    fd.seek(0)
    fd.truncate()


    # seek to the start of the file and truncate so file will be edited inline

    for key in rep.keys():
        text = text.replace(key, rep[key])

    fd.write(text)




