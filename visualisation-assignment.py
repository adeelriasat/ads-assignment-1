# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 00:30:15 2023

@author: Muhammad Adeel Riasat
"""
import matplotlib.pyplot as plt
import pandas as pd
import sys


def GetDataFromPath(filePath, sRows=0):
    """
    this method takes the csv file url and return as
    a pandas dataframe
    it takes two parameters 
    filePath = csv path
    sRows = no of rows to skip from start
    default is 0
    """
    data = pd.read_csv(filePath, skiprows=sRows)
    return data


def GetCryptoPrices(cryptoDataFrame):
    """
    in case of multiple dataframes it can be used
    this method takes pandas dataframe as parameter
    and return opening, closing, high and low price of crypto
    """
    opening_price = cryptoDataFrame['open']
    high_price = cryptoDataFrame['high']
    closing_price = cryptoDataFrame['close']
    low_price = cryptoDataFrame['low']
    return opening_price, high_price, closing_price, low_price


def PlotBarGraph(x, y, legend="", title="", xlabel="", ylabel=""):
    """
    this method takes plot bar graph for given data
    it takes graph data in params and plot the bar graph
    if the three params legend, xlabel and ylabel not given default will be empty
    x and y are required
    """
    # set the fig size and resolution
    plt.figure(figsize=(20, 6), dpi=1080)
    # plot the line graph with lengends, date along x-axis and pricws along y-axis
    plt.bar(x, y, label=legend)
    plt.legend()

    # set x-axis and y-axis labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)

    # show graph title with size of title
    plt.title(title, size=18)
    plt.show()


def PlotPieGraph(x, y, title=""):
    """
    this method takes plot bar graph for given data
    it takes graph data in params and plot the bar graph
    if the three params legend, xlabel and ylabel not given default will be empty
    x and y are required
    """
    # set the fig size and resolution
    plt.figure(figsize=(20, 20), dpi=200)
    # plot the pie graph with lengends
    plt.pie(y, labels=x)
    plt.legend(loc='upper left')
    plt.show()


# first graph line
# get crypto data for CEX Exchange and store in Dataframe
# skip first 1 rows as those contain data references and information
# cryptoData = GetDataFromPath('https://www.cryptodatadownload.com/cdd/CEX_AAVEUSD_d.csv', 1)
cryptoData = GetDataFromPath('../Data/CEX_AAVEUSD_d.csv', 1)

# get first few records for better visualisation
# if you want to see all date comment this line
cryptoData = cryptoData.iloc[1:50]

# convert the column to pandas datetime format
cryptoData['date'] = pd.to_datetime(cryptoData['date'], format='%Y/%m/%d')

# I will get only date portion for better visualisation on x-axis
cryptoData['date_only'] = cryptoData['date'].dt.date

# get opening, closing, low and high price from function
opening_price, high_price, low_price, closing_price = GetCryptoPrices(
    cryptoData)

# set the fig size and resolution
plt.figure(figsize=(20, 6), dpi=1080)

# plot the line graph with lengends, date along x-axis and pricws along y-axis
plt.plot(cryptoData['date_only'], opening_price, label='Opening Price')
plt.plot(cryptoData['date_only'], high_price, label='High Price')
plt.plot(cryptoData['date_only'], low_price, label='Low Price')
plt.plot(cryptoData['date_only'], closing_price, label='Closing Price')

# set x-axis and y-axis labels
plt.ylabel('AAVE/USD')
plt.xlabel('Date')

# show graph title with size of title
plt.title('CEX Exchange Data (CEXIO) on Daily Basis', size=18)
plt.legend()
# rotate the x-axis to 45 degree for better visualisation
plt.xticks(rotation=45)
plt.show()

# second graph bar

# get student records of enrollment for year 2014/15 and skip description rows 14
std_records_2014 = GetDataFromPath('../Data/table 11-(2014-15).csv', 14)
std_records_2021 = GetDataFromPath('../Data/table 11-(2021-22).csv', 14)

# slice data for better visualisation and avoiding memory error bcz data is big
std_records_2014 = std_records_2014.iloc[0:200]
std_records_2021 = std_records_2021.iloc[0:500]

# plot the graph by method for student enrolled by region for year 2014-15
PlotBarGraph(std_records_2014['Region of HE provider'], "Student Enrollment Record 2014-15", std_records_2014['Number'],
             'Number of Students Enrolled By Region in Academic Year 2014-15', 'Region', 'Number of Students')

# plot the graph by method for student enrolled by Mode of study for year 2021-22
PlotBarGraph(std_records_2021['Mode of study'], "Student Enrollment Record 2021-22", std_records_2021['Number'],
             'Number of Students Enrolled By Study Mode in Academic Year 2021-22', 'Study Mode', 'Number of Students')

# third graph pie

# cellular subscription data according to region for years
cellular_subs_data = GetDataFromPath(
    '../Data/API_IT.CEL.SETS.P2_DS2_en_csv_v2_4903391.csv', 4)

# get first 10 countries data
cellular_subs_data = cellular_subs_data.iloc[0:10]

# plot the pie graph for first 10 countries for year 2010
PlotPieGraph(cellular_subs_data['Country Name'], cellular_subs_data['2010'],
             "Mobile Cellular Subscriptions By Region (per 100 people) - 2010")


# plot the pie graph for first 10 countries for year 2020
PlotPieGraph(cellular_subs_data['Country Name'], cellular_subs_data['2020'],
             "Mobile Cellular Subscriptions By Region (per 100 people) - 2020")
