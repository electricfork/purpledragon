from sys import exit
import random
from optparse import OptionParser, OptionValueError

__author__ = "ben, twitter.com/electricfork"
__version__ = 'a1'
__date__ = "October 27, 2011"


"""
completely goofy but occasionally handy
"""

if __name__ == "__main__":

    usage = "usage %prog [options]"
    parser = OptionParser(description="Purple Dragon was the code name for a military research project that developed the idea of \"operations security\".  purpledragon.py creates random identifiers based on two file dictionaries to allow casual reference to a various event between two parties.  This could also be used to generate a challenge/response pair though that hasn't been added as an option")
    #parser.add_option("--name", "-n", action="store_true", dest="name", \
        #default=False, help="do a regex based on entity name")
    parser.add_option("--adjective", "-a", action="store", dest="adjective", \
        default=False, help="adjective file to use")
    parser.add_option("--noun", "-n", action="store", dest="noun", \
        default=False, help="noun file to use")
    parser.add_option("--quantity", "-q", action="store", dest="quantity", \
        type=int, default=1, help="output X number of identifiers")
    (options, args) = parser.parse_args()

    #if options.name:

if options.adjective:
    adjectivefile = open(options.adjective, 'rb')
    adjectives = adjectivefile.readlines()
else:       #lazy while programing.
    print "must declare an adjective file"
    exit(0)
if options.noun:
    nounfile = open(options.noun, 'rb')
    nouns = nounfile.readlines()
else:       #lazy while programing.
    print "must declare a noun file"
    exit(0)
"""
Take a random line, remove the new line, and use that as the 
adjective / noun
"""
while options.quantity:
	adjective = adjectives[random.randrange(0, len(adjectives)-1)].strip()
	noun = nouns[random.randrange(0, len(nouns)-1)].strip()
	print "%s %s\n" % (adjective.capitalize(), noun.capitalize())
	options.quantity = options.quantity - 1
