import bs4 as bs
import urllib.request
import os
import numpy as np
import csv
import pandas as pd
## scriptVersion: 0.12
## OPEN THE OUTPUT FILE WITH NO DELMINITER DO NOT CHOOSE ANY CHARACTER INSTEAD COPY THE WHOLE EXCEL FILE TO A TXT FILE AND RE-OPEN INTO A EXCEL FILE 
## FOR PROPER COMMA (",") DELIMINATED CSV FILE !!!

##SOME LIBs ARE REDUNDANT NEXT VERSIONS WILL CLEAN THE CODE



##Developed by: DOMTEAM




def get_city_data():
	df = pd.read_csv("city_name_links.csv")
	names=[]
	for name in range(0, len(df) ):
		names.append(df.iloc[name,0]);




	part_1s =[]
	for part_1 in range(0, len(df) ):
		
		part_1s.append(df.iloc[part_1,1])



	part_2s =[]
	for part_2 in range(0, len(df) ):
		
		part_2s.append(df.iloc[part_2,2])
		
		
		
	return names,part_1s,part_2s
	
	
	
	
	
start =1 # day 1 is 01.01.2007
number_of_loot_days = 3756   #3746 #number of days after 01.01.2007
def get_data(start_Date):
	names,part1s,part2s = get_city_data()
	counter =0
	for i in range(0,len(names)):
		myfile= open(names[i]+".csv", 'w') # enter the output file name
		wr = csv.writer(myfile,delimiter=',') 
			
		web_link_date=1	
		
		for web_link_date in range( start_Date,number_of_loot_days): ##loops the days
		##manages weblink name
		##change the URL link for each location becareful to connotate weblink correctly
			web_link = part1s[i]+str(web_link_date)+part2s[i]
			sauce= urllib.request.urlopen(web_link).read()
			soup = bs.BeautifulSoup(sauce,'lxml')
			body = soup.body
			date = soup.find("h2", { "class" : "history-date" })
			date_fixed_text = date.text.replace("," , "")
		
			## date.txt gets the text from h2 with date
			## the original date has "," character so next code gets ride of "," for csv delimination
			
			
			print("Getting: " +names[i]+" data for : "+date.text)
			## finds the table with id obsTable
			table = soup.find("table" , {"id" : "obsTable"})
			try:
				table_head = table.find("thead")
				#loops the thead for the header of the table
				for th in table_head:
					th = table_head.find_all('th')
					row = [i.text for i in th]
				## ads a date coloumn and the found cell names from thead 
				## this is done to match the number of coloumn with the data
				wr.writerow(["Date"]+row)
			


				cell_data=""
				cell_saved_data =""
				table_body = table.find("tbody")
				cell_data = []
				#tr = table_body.find_all("tr", {"class" : "no-metars"})
				body_row_no = 0 ##not used
				cell_col_no =0  ##not used

			
			##loops the table body for rows
				for body_row in table_body.find_all("tr", {"class" : "no-metars"}):
					line=""
					##loops individual cells in a row
					for cell in body_row.find_all("td"):
						
						##finds the cell text and goes through 3 functions to remove excess characters
						cell.text1=cell.text.replace("\n", "")
						cell.text2=cell.text1.replace("\xa0","")
						cell.text3 = cell.text2.replace("\t","")
						## adds each cell value to a line var
						line=line+cell.text3+","

					## after finding the cell text for each cell and creating a line date of the measurement is also added to the first row
					wr.writerow([date_fixed_text]+[line])
					cell_data.append(line)## for debugging purposes


				start = web_link_date
				one_day = row + cell_data##not used
			except:
				print ('NO DATA FOUND: TRYING NEXT DAY')
				wr.writerow([date_fixed_text])
				get_data(web_link_date+1)
		
##change the name of each measurement location with a propername


try:
	get_data(start)
except:
	get_data(start)
print("####DONE####")





