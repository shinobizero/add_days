# -*- coding: utf-8 -*-

import datetime

def febuaryDays(year):
    if year % 4 == 0:
        days = 29
    else:
        days = 28
    return days

def getTodayDate():
    current_year = int(datetime.datetime.now().strftime("%Y"))
    current_month = int(datetime.datetime.now().strftime("%m"))
    current_day = int(datetime.datetime.now().strftime("%d"))
    return current_year, current_month, current_day

def dateStamp():
    current_year, current_month, current_day = getTodayDate()
    current_date = str(current_day) + "/" + str(current_month) + "/" + str(current_year)
    return current_date

def getDaysMonth(month, year):
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    days_30 = ['April', 'June', 'September', 'November']
    selected_month = months[month-1]    
    days = 0
    if selected_month in days_31:
        days += 31
    elif selected_month in days_30:
        days += 30
    elif selected_month not in days_30 and selected_month not in days_31:
        days += febuaryDays(year)
    return days

def addDays(days_to_add, return_string=True):
    current_year, current_month, current_day = getTodayDate()

    output_day = 0  
    output_month = 0
    output_year = 0
        
    working_with_month = current_month
    working_with_year = current_year
    remaining_days = 0
    
    month_days = getDaysMonth(working_with_month, working_with_year)
    if days_to_add + current_day < month_days:
        output_day += days_to_add + current_day
        output_month += working_with_month
        output_year += working_with_year
    else:
        remaining_days += month_days-current_day
        days_to_add -= remaining_days
        if working_with_month == 12:
           working_with_month -= 12
           working_with_year += 1
        else:
           working_with_month += 1
        while True:
            month_days = getDaysMonth(working_with_month, working_with_year)
            if days_to_add <= month_days:
                output_day += days_to_add
                output_month += working_with_month
                output_year += working_with_year
                break
            elif days_to_add > month_days:
                days_to_add -= month_days
                if working_with_month == 12:
                    working_with_month -= 11
                    working_with_year += 1
                else:
                    working_with_month += 1
    if return_string == True:
        output = str(output_day) + "/" + str(output_month) + "/" + str(output_year)
        return output
    elif return_string == False:
        return output_day, output_month, output_year

days_to_add = int(input("Please enter days to add: "))
output = addDays(days_to_add)
print(str(dateStamp()) + " + " + str(days_to_add) + " days = " + str(output))