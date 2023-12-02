# list =[]
# with open("weather_data.csv" ,"r") as weater_file:
#     weaters=weater_file.read()
#     weaters_list=weaters.split()
#     for item in weaters_list:
#         text = item.split(",")
#         obj={'day':text[0],'temp':text[1],'condition':text[2]}
#         list.append(obj)
# print(list)


# import csv
# with open("weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     temperatures=[]
#     for temp in data:
#         if temp[1] !="temp":
#             temperatures.append(int(temp[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# to_dict() : the will turn to objct with all data tabel
data_dict = data.to_dict()
# print(data_dict)

# tolist() : will turn the rowsValues to python list
temp_list = data["temp"].tolist()

# mean() : is a same  avg=round(sum(temp_list)/len(temp_list))
avg = data["temp"].mean()
# print(avg)
# max() : get a grates number of list
max = data["temp"].max()
# print(max)

# get a Data in Colums
# print(data["condition"])
# print(data.day)

# get Data in Row
row = data[data.temp == data.temp.min()]
print(row)

# Create a dataframe from scratch
data_dict = {
    "schuler": ["Nour", "Mohammad", "Ahmed"],
    "note": [1, 3, 6]
}
data_New = pandas.DataFrame(data_dict)
data_New.to_csv("shculer.csv")

# print(type(data))
# print(data["temp"])
