import csv
import simplejson
import urllib


for line in open('API_Key.txt', 'r'):
    API_Key = line

with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(
        csvfile, delimiter=';')
    for row in reader:
        orig_coord = row[0]
        dest_coord = row[1]
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}\
              &destinations={1}&key={2}&mode=driving&language=en-EN\
              &units=metric".format(str(orig_coord), str(dest_coord), str(API_Key))
        result = simplejson.load(urllib.urlopen(url))
        driving_distance = result['rows'][0][
            'elements'][0]['distance']['value']
        print driving_distance
