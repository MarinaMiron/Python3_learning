# with open("Day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("Day25/weather_data.csv")
# #print(type(data))
# #print(data["temp"])

# data_dict = data.to_dict()
# #print(data_dict)

# temp_list = data["temp"].to_list()
#print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

#print(data["temp"].mean())

# print(data["temp"].max())

#Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
#print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp*1.8)+32)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Day25/new_data.csv")

import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
counts = data["Primary Fur Color"].value_counts()

df = pandas.DataFrame(counts) 
df.to_csv("Day25/squirrel_data.csv")