import csv  #This Python module helps read and write csv files
from urllib import request  #for accessing files on the internet
import json #allow simplified use of json data
import csv #allow

URL_Apple = 'https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=zwzJQCDVUU-CXGCxSiY_&start_date=2014-01-01&end_date=2015-01-01'
URL_Boeing = 'https://www.quandl.com/api/v3/datasets/EOD/BA.json?api_key=zwzJQCDVUU-CXGCxSiY_&start_date=2014-01-01&end_date=2015-01-01'
URL_Chevron = 'https://www.quandl.com/api/v3/datasets/EOD/CVX.json?api_key=zwzJQCDVUU-CXGCxSiY_&start_date=2014-01-01&end_date=2015-01-01'
URL_Cisco = 'https://www.quandl.com/api/v3/datasets/EOD/CSCO.json?api_key=zwzJQCDVUU-CXGCxSiY_&start_date=2014-01-01&end_date=2015-01-01'
URL_AmericanExpress = 'https://www.quandl.com/api/v3/datasets/EOD/AXP.json?api_key=zwzJQCDVUU-CXGCxSiY_&start_date=2014-01-01&end_date=2015-01-01'
WriteCount = 0

class URL:
	def URLInput(self, URLInputJSON):
		global WriteCount #counter for keeping the heading proper
		response = request.urlopen(URLInputJSON)
		string = response.read().decode('utf-8') #This grabs all the data at once
		json_obj = json.loads(string) #This parses the json data
		JSONData = json_obj['dataset']

		csvwriter = csv.writer(fil) # create the csv writer object

		#Our data set has two important items in the json hierarchy: column_names and data
		DatasetCode = JSONData['dataset_code'] #store the dataset code for further use
		columnNames = JSONData['column_names'] #store the column_names element for further use
		data = JSONData['data'] #store the data element for further use
		 
		

		#Put the Headings into the csv file
		headings = []  #make a list to store the values
		for Heading in columnNames:  #Find each heading in the list
			headings.append(Heading)  #add each heading to the list
		headings.append('Stock Code') #manually inserts 'Stock Code' because it's not included in the column_names JSON
		if WriteCount == 0: #I don't want to have it spit out a heading each time, and rather than reformat the code, I just created a counter that if not true, then doesn't write a heading
			csvwriter.writerow(headings)  #Now that you have them all, write them in the file

		#Write the the data into the file, the data element has a list of lists
		# the csvwriter can be given a list or items which it sepearates by commas
		for Row in data:
			Row.append(DatasetCode) #adds the dataset code to each row of information
			csvwriter.writerow(Row) #each input row has multiple items

		#Demonstrate how to process each value: show the metadata
		for item in JSONData:
			if item != 'data' and item != 'columnNames':
				itemKey = item
				value = str(JSONData[itemKey])
				print(itemKey + ' : ' + value)
		WriteCount += 1 #adds to writecount to keep value above 1 so as to not add headings each time running through
				
		
			
		

fil = open('StockPrices.csv', 'w', newline='')	#Use Python's CSV object to write data
		# w opens an output file, newline='' protects against multiple newlines in windows
		 # open a file for writing
		 		 
	 			
URL = URL()
URL.URLInput(URL_Apple)
URL.URLInput(URL_Boeing)
URL.URLInput(URL_Chevron)
URL.URLInput(URL_Cisco)
URL.URLInput(URL_AmericanExpress)


fil.close()	#Close files after you are done to ensure all the data is written