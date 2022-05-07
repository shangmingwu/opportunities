import csv
import re
import pandas as pd

def process_city(area):
    with open(area + '.csv') as opps:
        # read the opportunities spreadsheet file
        opp_reader = csv.reader(opps, delimiter=',')
        line = 0
        for row in opp_reader:
            if line == 0:
                # skip first line, which is only headers
                line += 1
            else:
                # string anything that isn't alphanumeric for file name
                slug_name = re.sub(r'[^\w]', '', row[1])
                with open(slug_name+'.mdx','w') as output:
                    output.write('---\n')
                    output.write('postingName: "'+row[1]+'"\n')
                    output.write('tags: ["'+row[2]+'"]\n')
                    output.write('orgName: "'+row[3]+'"\n')
                    output.write('linkTo: "'+row[4]+'"\n')
                    output.write('city: "'+row[5]+'"\n')
                    output.write('postedDate: '+row[6]+'\n')
                    output.write('orgImages: /resource/opportunities/'+row[7]+'\n')
                    output.write('---\n')
                    output.write(row[8])

# format so far (subject to change)
# | 0            |  1                |  2           |   3    |  4    |  5    |  6         | 7
# | PROGRAM NAME |  OPPORTUNITY TYPE |  INSTITUTION |   LINK |  CITY |  DATE |  LOGO NAME | DESCRIPTION

data = pd.read_excel('opportunities.xlsx', sheet_name=None)

cities = []

for sheet_name, df in data.items():
    df.to_csv(f'{sheet_name}.csv')
    cities.append(sheet_name)

for city in cities:
    process_city(city)