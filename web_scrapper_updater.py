import bs4 as bs
import urllib.request
import os
import numpy as np
import pandas as pd
import csv
import datetime

import time
from time import mktime
from datetime import datetime
from datetime import timedelta
from types import *
from openpyxl import Workbook
import openpyxl


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

def open_days():
	df=pd.read_excel(open("holidays.csv", 'rb'), sheetname="holidays")
	return df


def open_csv(city_name):
	dfs=[]
	print()
	
	for i in range (0,len(city_name) ): #####len(city_name)
		try:
			print("Fetchin data from: "+city_name[i]+".xlsx")
			df=pd.read_excel(open(city_name[i]+".xlsx",'rb'), sheetname="Sheet1")
		
			print('  SUCCESS')
			dfs.append(df)
		except:
			print("FILE CAN'T BE FOUND")
			pass
		
	return dfs	
	
def remove_weekdays(string):
	string = string.replace('Monday','')
	string = string.replace('Tuesday','')
	string = string.replace('Wednesday','')
	string = string.replace('Thursday','')
	string = string.replace('Friday','')
	string = string.replace('Saturday','')
	string = string.replace('Sunday','')
	return string

	
def update_excel(name,part1,part2,startDay,today,firstday,dataframe,index):
	if(today>startDay):
		for web_link_date in range( ((startDay-firstday).days)+1,(today-firstday).days+1):
			web_link= part1+str(web_link_date)+part2
			
			sauce= urllib.request.urlopen(web_link).read()
			soup = bs.BeautifulSoup(sauce,'lxml')
			body = soup.body
			date = soup.find("h2", { "class" : "history-date" })
			date_fixed_text = date.text.replace("," , "")
			date_fixed_text = remove_weekdays(date_fixed_text)
		
			print("Getting "+name+" data for : "+date.text)
			print(web_link)
			print(20*'#')
			try:

				table = soup.find("table" , {"id" : "obsTable"})
				index=index+1	
				table_head = table.find("thead")
				rows_to_be_added =[]
					#loops the thead for the header of the table
				for th in table_head:
					th = table_head.find_all('th')
					row = [i.text for i in th]
					## ads a date coloumn and the found cell names from thead 
					## this is done to match the number of coloumn with the data
					##wr.writerow(["Date"]+row)
				total_text =(["Date"]+row)
				
				
				
				dataframe.loc[index,0:len(total_text)] = total_text
				
				cell_data=""
				cell_saved_data =""
				table_body = table.find("tbody")
				cell_data = []
				#tr = table_body.find_all("tr", {"class" : "no-metars"})
				
				
				
				
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
							split_line= str(line).split(',')
						## after finding the cell text for each cell and creating a line date of the measurement is also added to the first row
						##wr.writerow([date_fixed_text]+[line])
						##cell_data.append(line)## for debugging purposes
						index=index+1
						
						total_Text =([date_fixed_text]+split_line)
						
						
						dataframe.loc[index,0:len(total_Text)] = total_Text
					
			except:
				print('NO DATA FOUND')
				total_Text =([date_fixed_text]+["","",""])
				dataframe.loc[index,0:len(total_Text)] = total_Text
				

	else:
		print(name+".csv is up to date")
	return dataframe
	
	

start_date = datetime(2007,1,1)
todays_date=datetime.today()



names,part1s,part2s = get_city_data()
#df=pd.read_excel(open("completed_xls/Bursa.xlsx",'rb'), sheetname="Sheet1")
#dfs=open_csv(names)
holiday_df= open_days()
day_df = holiday_df['Day']
value_df= holiday_df['Value']
dfs = open_csv(names)
list_no =0
for df in dfs:
	
	last_date = dfs[list_no]['Date'].tail(1)
	print(last_date)

	splitted_date_string = str(last_date).split()
	last_index= int(splitted_date_string[0])
	last_date_month =splitted_date_string[1]
	last_date_day =splitted_date_string[2]
	last_date_year =splitted_date_string[3]

	last_date_numeric = time.strptime(last_date_month+last_date_day+last_date_year,'%B%d%Y' )


	last_date_datetime = datetime.fromtimestamp(mktime(last_date_numeric))
	day_to_start = last_date_datetime +timedelta(days=1)
	data_number = len(names)
	print("Last date found in the current database :"+str(last_date_numeric))
	print("UPDATING DATABASE")
	dfs[list_no] = update_excel(names[list_no],part1s[list_no],part2s[list_no],day_to_start,todays_date,start_date,dfs[list_no],last_index)
	
	
	for i in range(len(df.index)):
		date= str(df.loc[i,'Date'])
		
		try:
			#print(type(date_numeric))
			date_numeric = time.strptime(date,'%B %d %Y')
			date_datetime = datetime.fromtimestamp(mktime(date_numeric))
			
			day_difference = (date_datetime - start_date).days
			df.loc[i,"Holiday"] =value_df.loc[day_difference]
			hour = str(df.loc[i,'Time (EET)'])
			hour_numeric= time.strptime(date+" "+hour, '%B %d %Y %H:%M:%S')
			hour_datetime = datetime.fromtimestamp(mktime(hour_numeric))
			
			df.loc[i,'weekDay'] =date_datetime.weekday()
		except:
			pass
	
	
	dfs[list_no].to_excel(names[list_no]+".xlsx")
	print(names[list_no]+".xlsx file saved")
	print(20*"#")
	list_no= list_no+1

print(20*"*")
print(20*"#")
print(20*"*")
print("SUCCESS")
