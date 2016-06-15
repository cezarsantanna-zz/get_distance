import csv
import simplejson
import urllib


for line in open('API_Key.txt', 'r'):
    API_Key = line

with open('data.csv', 'rb') as rcsvfile:
    with open('result.csv', 'wb') as wcsvfile:
        reader = csv.reader(
            rcsvfile,
            delimiter=';')
        writer = csv.writer(wcsvfile,
                            delimiter=';',
                            quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            orig01_coord = row[0]
            dest01_coord = row[1]
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}\
                  &destinations={1}&key={2}&mode=driving&language=en-EN\
                  &units=metric".format(str(orig01_coord),
                                        str(dest01_coord),
                                        str(API_Key))
            result = simplejson.load(urllib.urlopen(url))
            driving_distance01 = result['rows'][0][
                'elements'][0]['distance']['value']

            orig02_coord = row[1]
            dest02_coord = row[0]
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}\
                  &destinations={1}&key={2}&mode=driving&language=en-EN\
                  &units=metric".format(str(orig02_coord),
                                        str(dest02_coord),
                                        str(API_Key))
            result = simplejson.load(urllib.urlopen(url))
            driving_distance02 = result['rows'][0][
                'elements'][0]['distance']['value']
            driving_distance = (driving_distance01 + driving_distance02) / 2
            print orig01_coord, dest01_coord, driving_distance
            writer.writerow([orig01_coord, dest01_coord, driving_distance])
