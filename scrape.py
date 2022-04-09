import csv
import re

# format so far (subject to change)
# | 0            |  1                |  2           |   3    |
# | PROGRAM NAME |  OPPORTUNITY TYPE |  INSTITUTION |   LINK |

with open('opportunities.csv') as opps:
    # read the opportunities spreadsheet file
    opp_reader = csv.reader(opps, delimiter=',')
    line = 0
    for row in opp_reader:
        if line == 0:
            # skip first line, which is only headers
            line += 1
        else:
            # string anything that isn't alphanumeric for file name
            slug_name = re.sub(r'[^\w]', '', row[0])
            with open(slug_name+'.mdx','w') as output:
                output.write('---\n')
                output.write('name: "'+row[0]+'"\n')
                output.write('type: "'+row[1]+'"\n')
                output.write('institution: "'+row[2]+'"\n')
                output.write('link: "'+row[3]+'"\n')
                output.write('---')