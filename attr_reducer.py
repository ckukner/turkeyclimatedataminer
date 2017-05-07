import pandas as pd
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
		try:
			print("Fetchin data from: "+city_name[i]+".xlsx")
			df=pd.read_excel(open(city_name[i]+".xlsx",'rb'), sheetname="Sheet1")
		
			print('  SUCCESS')
			dfs.append(df)
		except:
			pass
		
		
	return dfs
	
names,part1s,part2s = get_city_data()
dfs = open_csv(names)
list_no =0

for df in dfs:
	new_df=pd.DataFrame()
	new_df['Date'] =df['Date']
	new_df['Time'] = df['Time (EET)']
	new_df['Temp.'] = df['Temp.']
	new_df['Holiday'] = df['Holiday']
	new_df['weekDay'] = df['weekDay']
	
	new_df=new_df[new_df.Date != 'Date']
	
	# for i in range(len(new_df.index)):
		# if new_df.loc[i,'Date'] == 'Date':
			# new_df.drop(i)
	
	
	new_df.to_excel("reduced/"+names[list_no]+"reduced.xlsx")	
	
	print(names[list_no]+"_reduced.xlsx file saved")
	list_no= list_no+1
	print(20*"#")
		
		
		
		
		
print(15*"#*")	
print("ALL DONE")
print(15*"#*")	