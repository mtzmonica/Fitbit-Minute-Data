import json, csv
import fitbit
import os.path
import sys
from datetime import date
 
if len(sys.argv) > 1:
	BASE_DATE = sys.argv[1]
	START_TIME = sys.argv[2]
	END_TIME = sys.argv[3]
else:
	BASE_DATE = str(date.today().isoformat())

#Insert personal info here
consumer_key = ''
consumer_secret = ''
user_key = ''
user_secret = ''
uid=''

authd_client = fitbit.Fitbit(consumer_key, consumer_secret, 
	resource_owner_key=user_key, 
	resource_owner_secret=user_secret)

step_stats = authd_client.intraday_time_series('activities/steps', 
	base_date=BASE_DATE, 
	detail_level ='1min', 
	start_time = START_TIME, end_time = END_TIME)


#day = str(BASE_DATE)
testdata = str(BASE_DATE) + ".json"
file = open(testdata,'w+')


for key,value in step_stats.iteritems():
	#for date in value:
		json.dump(value, file, indent=2)

#Attempted export to csv 
'''
with open('testdata.csv', 'w+') as file:
	writer = csv.writer(file)
	file.readline()
	for key,value in step_stats.iteritems():
	#writer.writeheader()
		for x in  [key, value]:	
			writer.writerow([x])
'''

file.close()


