# some rows (about 98 of several million) are broken. WTF. 

infile = open("data/8872_skedb.txt", 'r')
outfile = open("data/8872_skedb_fixed.txt", 'w')

# write header row:

header = infile.readline()
# ignore header
#outfile.write(header)

linenum = 0
problems = 0
counts = {}
while True:
    linenum += 1
    line = infile.readline()
    line = line.replace("\n","")
    line = line.replace("\\","")
    
    if not line:
        break
    
    count = line.count('|')
#    print count

    if count != 17:
        print linenum, count
        problems += 1
        difference = 17 - count
        bars = ['|']*difference
        filler = "".join(bars)
        line = line + filler

    
    
    outfile.write(line + "\n")


print "Total problems: %s" % (problems)
