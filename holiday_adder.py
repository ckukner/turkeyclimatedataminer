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
	
	
def open_csv(city_name):
	dfs=[]
	print()
	
	for i in range (0, len(city_name)): #####len(city_name)
		print("Fetchin data from: "+city_name[i]+".xlsx")
		df=pd.read_excel(open(city_name[i]+".xlsx",'rb'), sheetname="Sheet1")
		
		print('  SUCCESS')
		dfs.append(df)
		
		
	return dfs	
	
def	add_week_day():
	return 1	
def open_days():
	df=pd.read_excel(open("holidays.xlsx", 'rb'), sheetname="holidays")
	
	return df
	
	
def string_to_datetime(timestampX):
	datetimeX=datetime.fromtimestamp(mktime(timestampX))
	return datetimeX
	
def find_index():
	
	
	
	return True
	
	
	
	
	

names,part1s,part2s = get_city_data()	
dfs = open_csv(names)

holiday_df= open_days()

day_df = holiday_df['Day']
value_df= holiday_df['Value']


day_one = datetime(2007,1,1)
counter=0

for df in dfs:
	for i in range(len(df.index)):
		date= str(df.loc[i,'Date'])
		try:
			date_numeric = time.strptime(date,'%B %d %Y')
			#print(type(date_numeric))
			
			date_datetime = datetime.fromtimestamp(mktime(date_numeric))
			day_difference = (date_datetime - day_one).days
			df.loc[i,"Holiday"] =value_df.loc[day_difference]
			
			
			df.loc[i,'weekDay'] =date_datetime.weekday()
		except:
			##print("error")
			pass
			
	df.to_excel(names[counter]+".xlsx")
	counter=counter+1
	

	
	

	
	
	
	
	
	
	
	
	
	
	
