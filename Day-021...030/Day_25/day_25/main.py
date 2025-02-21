# import csv
# with open("./weather_data.csv") as data:
#     data_list = csv.reader(data)
#     temperature = []
#     for d in data_list:
#         if d[1] != "temp":
#             day_temp = int(d[1])
#             temperature.append(day_temp)
#     print(temperature)

import pandas
from numpy.ma.extras import average

# data = pandas.read_csv("weather_data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)

# monday = data[data.day == "Monday"]
# temp_f = (monday.temp[0] * 1.8) + 32
# print(temp_f)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_colors = []
colors = []
a_num =[]
# checking every color in the csv data
for color in data["Primary Fur Color"].to_list():
    # adding the colors that appeared in the list
    if isinstance(color, str) and color not in primary_colors:
        primary_colors.append(color)
    # adding all colors
    colors.append(color)
# checking the number of times each color appeared
for c in primary_colors:
    color_count = colors.count(c)
    a_num.append(color_count)
print(primary_colors)
print(a_num)

color_dict = {"Primary Fur": primary_colors, "Count": a_num}
new_data = pandas.DataFrame(color_dict)
new_data.to_csv("colors.csv")
print(color_dict)
print(new_data)


