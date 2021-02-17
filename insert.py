import json
from regions.models import *
import csv

algeria=Country.objects.get(name="Algeria")

f = open('wilayas_list.csv', 'r')

with f:

    reader = csv.DictReader(f)

    for row in reader:
        # try:
        #     wilaya=Region.objects.get(name=row['wilaya_name'])
        # except:
        #     wilaya=Region.objects.create(name=row['wilaya_name'],arabic_name=row['wilaya_name_ar'],code=row['wilaya_code'],country=algeria)



        #
        # try:
        #     daira=Daira.objects.get(name=row['daira_name'])
        # except:
        #     daira=Daira.objects.create(name=row['daira_name'],wilaya=wilaya)

        # region=Region.objects.get(code=row['wilaya_code'])
        # postal="{:03d}".format(len(City.objects.filter(region=region))+1)
        #
        # try:
        #     commune=City.objects.get(name=row['commune_name'],region=region)
        # except:
        #     commune=City.objects.create(name=row['commune_name'],arabic_name=row['commune_name_ar'],region=region,postal_code=f'{region.code}{postal}')
        #     print(f'{commune.name} {commune.postal_code}')

        # exec(open('insert.py').read())

#
# with open('regions.json') as json_file:
#     data = json.load(json_file)
#     for wilaya in data['wilayas']:
#         wil=Wilaya.objects.create(name=wilaya['name'])
        # for daira in wilaya['dairas']:
        #     # dai=Daira.objects.create(name=daira['name'],wilaya=wil)
        #     for commune in daira["communes"]:
        #         try:
        #             print(commune)
        #         except:
        #             pass
                # Commune.objects.create(name=commune['name'],daira=dai)
