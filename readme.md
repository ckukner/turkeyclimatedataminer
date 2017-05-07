READ ME FOR MINING DATA OF WEATHER FORECAST ADDING DAY INFORMATION AND PARSING FOR MACHINE LEARNING ALGORTIHM

1- Run download_data.py
2- this will create .csv files 
3- manually clean the data and save it as xlsx file
4- remove monday-sunday text from each xlsx file -- FURTHER IMPOREVEMENTS WILL BE MADE TO AUTOMIZE
5- please make sure the format in the xlsx file and holiday_adder.py parser are EXACTLY the same, a simple white space can break the rundown of the script
	5a-the exampla data should be "January 1 2007" 
	5b- variants like " January 1 2007" (notice the white space infront of January) will break the format
	5c- holiday.adder.py parses '%B %d %Y' in this exact format
	5d-improvements will be done in further releases
	IMPORTANT: Depending on tablesheet software you use I have experienced that TIME coloumn may be converted to a number so a manual reformat to date might be required
	
6-run the holiday_adder.py this will add the weekday value of the day and also the add if the date is a national holiday
	6a- this has been done for turkish calender so please modify for your own use

7-run the attr_reducer.py this code will reduce the number of attributes just required for the machine learning algorithm, also reduced values are saved to a different folder because the original data might be needed for a different model
8- remove any none numeric value eg.  '°C '
9- the most crucial part of the for machine learning is to have the data of all the cities in the same frequeny. unfortunately the data mined does is not in this format so we have to create a script
10 -convert the xlsx to csv
11- run the aggregate.py
	11a- note that aggregate.py does one aggregation at a time so for each file you need to change the code and run it again
	11b- automization will be added later
	11c-the script takes the average of the data of the same hour
	11d- there are "-" characters in temp. data so make sure you change the data, the logical step is to take the previous hours temp. data as the missing data
	



