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
            orig_coord = row[0]
            dest_coord = row[1]
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}\
                  &destinations={1}&key={2}&mode=driving&language=en-EN\
                  &units=metric".format(str(orig_coord),
                                        str(dest_coord),
                                        str(API_Key))
            result = simplejson.load(urllib.urlopen(url))
            driving_distance = result['rows'][0][
                'elements'][0]['distance']['value']
            writer.writerow([orig_coord, dest_coord, driving_distance])
