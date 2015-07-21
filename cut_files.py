""" For processing IRS 8872 records from here: http://forms.irs.gov/politicalOrgsSearch/search/datadownload.jsp?ck 
Note that 8871 are records that say a committee has been formed (or changed?) whereas 8872 are the regular reports.

"""

from irs_configs import *


# the first value is record type. Possible record types are:
# 'H' for a generic header ? 

# '1' for the 8871 form header
# 'D' for director records
# 'R' for related entities
# 'E' for election authority id (?)

# '2' for the 8872 form header

line2_header = "Record Type|Form Type|Form ID Number|PERIOD Begin Date|PERIOD End Date|Initial Report Indicator|Amended Report Indicator|Final Report Indicator|Change of Address Indicator|ORGANIZATION NAME|EIN|MAILING ADDRESS 1|MAILING ADDRESS 2|MAILING ADDRESS CITY|MAILING ADDRESS STATE|MAILING ADDRESS ZIP CODE|MAILING ADDRESS ZIP EXT|E_MAIL ADDRESS|ORG FORMATION DATE|CUSTODIAN NAME|CUSTODIAN ADDRESS 1|CUSTODIAN ADDRESS 2|CUSTODIAN ADDRESS CITY|CUSTODIAN ADDRESS STATE|CUSTODIAN ADDRESS ZIP CODE|CUSTODIAN ADDRESS ZIP EXT|CONTACT PERSON NAME|CONTACT ADDRESS 1|CONTACT ADDRESS 2|CONTACT ADDRESS CITY|CONTACT ADDRESS STATE|CONTACT ADDRESS ZIP CODE|CONTACT ADDRESS ZIP EXT|BUSINESS ADDRESS 1|BUSINESS ADDRESS 2|BUSINESS ADDRESS CITY|BUSINESS ADDRESS STATE|BUSINESS ADDRESS ZIP CODE|BUSINESS ADDRESS ZIP EXT|QTR INDICATOR|MONTHLY RPT MONTH|PRE ELECT TYPE|PRE or POST ELECT DATE|PRE or POST ELECT STATE|SCHED_A_IND|TOTAL_SCHED_A|SCHED_B_IND|TOTAL_SCHED_B|INSERT_DATETIME\n"


# 'A' 8872 schedule A line

lineA_header = "Record Type|Form ID Number|SCHED A ID|ORG NAME|EIN|CONTRIBUTOR NAME|CONTRIBUTOR ADDRESS 1|CONTRIBUTOR ADDRESS 2|CONTRIBUTOR ADDRESS CITY|CONTRIBUTOR ADDRESS STATE|CONTRIBUTOR ADDRESS ZIP CODE|CONTRIBUTOR ADDRESS ZIP EXT|CONTRIBUTOR EMPLOYER|CONTRIBUTION AMOUNT|CONTRIBUTOR OCCUPATION|AGG CONTRIBUTION YTD|CONTRIBUTION DATE\n"
# 'B' 8872 schedule B line

lineB_header = "Record Type|Form ID Number|SCHED B ID|ORG NAME|EIN|RECIPIENT NAME|RECIPIENT ADDRESS 1|RECIPIENT ADDRESS 2|RECIPIENT ADDRESS CITY|RECIPIENT ADDRESS ST|RECIPIENT ADDRESS ZIP CODE|RECIPIENT ADDRESS ZIP EXT|RECIPIENT EMPLOYER|EXPENDITURE AMOUNT|RECIPIENT OCCUPATION|EXPENDITURE DATE|EXPENDITURE PURPOSE\n"

# 'F' for file footer -- with record count!

data_file = IRS_FILE_OUTPUT
infile = open(data_file, 'r')

outfile = open(HEADERS_8872, "w")
outfile.write(line2_header)

outfilea = open(SKEDA_8872, "w")
outfilea.write(lineA_header)

outfileb = open(SKEDB_8872,"w")
outfileb.write(lineB_header)

linecount = 0


for line in infile: 
    linecount += 1
    
    line = line.replace("\r","")
    line = line.replace("\n","")
    if (linecount % 10000 == 0):
        print "processed %s lines" % (linecount)
    values = line.split("|")
    linetype = values[0]
    
    if linetype == '2':
        outfile.write(line)
        outfile.write("\n")
            
    elif linetype == 'A':
        outfilea.write(line)
        outfilea.write("\n") 
            
    elif linetype == 'B':
        outfileb.write(line)
        outfileb.write("\n")
