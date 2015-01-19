# -*- coding: utf-8 -*-

from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print "copy from %s to %s" % (from_file, to_file)

# These two lines of code can be merged into one code. How can you do it?
indata = open(from_file).read()

#print "indata file is %d bytes." % len(indata)

#print "Does to_file exist? %r" % exists(to_file)
#print "Ready. Press return to proceed or CTRL-C to cancel."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

#print "Right. Everything's done."

out_file.close()


# make the entire code into one line code 
#open(to_file, 'w').write(open(from_file).read())
