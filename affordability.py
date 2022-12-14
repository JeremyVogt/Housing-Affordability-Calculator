# -*- coding: utf-8 -*-
"""
COMP 4710 Project - Fall 2014

@author: Jeremy Vogt
@studentid: 6852536
"""

import csv

def load_data(fname):
    datafile = open(fname, 'r')
    reader = csv.reader(datafile, delimiter=',', quotechar='"')
    data = []
    header = True
    for row in reader:
        if header:
            header = False
            continue
        row_dict = {}
        if (row[6] == 'Total number of private households by tenure'):
            cur_households = row[8]
            continue
        elif (row[6] == '  Owner'):
            cur_own = row[8]
            continue
        elif (row[6] == '  Renter'):
            cur_rent = row[8]
            continue
        elif (row[6] == '    Spending 30% to less than 100% of household total income on shelter costs'):
            cur_over_thirty = row[8]
            continue
        elif (row[6] == '  Average monthly shelter costs for owned dwellings ($)'):
            cur_avg_own = row[8]
            continue
        elif (row[6] == '  Average value of dwellings ($)'):
            cur_avg_value = row[8]
            continue
        elif (row[6] == '  Average monthly shelter costs for rented dwellings ($)'):
            cur_avg_rent = row[8]
            continue
        elif (row[6] == '  Average after-tax household income ($)'):
            cur_avg_income = row[8]
            # The following always goes with the last elif statement.
            row_dict["id"] = row[0]
            row_dict["province"] = row[1]
            row_dict["name"] = row[2]
            row_dict["households"] = int(cur_households)
            row_dict["own"] = int(cur_own)
            row_dict["rent"] = int(cur_rent)
            row_dict["over_thirty"] = int(cur_over_thirty)
            row_dict["avg_own"] = int(cur_avg_own) * 12
            row_dict["avg_value"] = int(cur_avg_value)
            row_dict["avg_rent"] = int(cur_avg_rent) * 12
            row_dict["avg_income"] = int(cur_avg_income)
        else:
            continue # Discard all other rows.
        data.append(row_dict)
    datafile.close()
    return data
    
def get_percentage(results, numerator, denominator, ascending):
    sorted_list = []
    for place in results:
        placename = place["name"] + ", " + place["province"]
        percentage = (float(place[numerator])) / (float(place[denominator])) * 100
        data_point = tuple([placename, percentage])
        sorted_list.append(data_point)
    sorted_list.sort(key=lambda tup: tup[1])  # sorts in place
    if (ascending == False):
        sorted_list.reverse()
    for data_point in sorted_list:
        print(data_point[0] + " - %.1f%%" % data_point[1])
        
def get_absolute(results, desired_variable, ascending):
    sorted_list = []
    for place in results:
        placename = place["name"] + ", " + place["province"]
        assoc_num = place[desired_variable]
        data_point = tuple([placename, assoc_num])
        sorted_list.append(data_point)
    sorted_list.sort(key=lambda tup: tup[1])  # sorts in place
    if (ascending == False):
        sorted_list.reverse()
    for data_point in sorted_list:
        print(data_point[0] + " - %d" % data_point[1])
        
def get_difference(results, minuend, subtrahend, ascending):
    sorted_list = []
    for place in results:
        placename = place["name"] + ", " + place["province"]
        difference = place[minuend] - place[subtrahend]
        data_point = tuple([placename, difference])
        sorted_list.append(data_point)
    sorted_list.sort(key=lambda tup: tup[1])  # sorts in place
    if (ascending == False):
        sorted_list.reverse()
    for data_point in sorted_list:
        print(data_point[0] + " - %d" % data_point[1])
        
def header(to_be_printed):
    print("\n" + to_be_printed)
    print("=" * len(to_be_printed))
    
def main():
    results = load_data("metros.csv")
    header("Percentage of households in owned dwellings:")
    get_percentage(results, "own", "households", False)
    header("Percentage of households in rented dwellings:")
    get_percentage(results, "rent", "households", False)
    header("Average annual shelter costs for owner-occupied dwellings:")
    get_absolute(results, "avg_own", False)
    header("Average annual shelter costs for rented dwellings:")
    get_absolute(results, "avg_rent", False)
    header("Average annual after-tax income per household:")
    get_absolute(results, "avg_income", False)
    header("Average percentage of income spent on shelter costs for homeowners:")
    get_percentage(results, "avg_own", "avg_income", False)
    header("Average percentage of income spent on shelter costs for renters:")
    get_percentage(results, "avg_rent", "avg_income", False)
    header("Percentage of households spending over 30% of income on shelter costs:")
    get_percentage(results, "over_thirty", "households", False)
    header("Average income left over after shelter costs for homeowners:")
    get_difference(results, "avg_income", "avg_own", False)
    header("Average income left over after shelter costs for renters:")
    get_difference(results, "avg_income", "avg_rent", False)
    header("Average value of dwellings:")
    get_absolute(results, "avg_value", False)
    header("Average value of dwellings relative to average income:")
    get_percentage(results, "avg_value", "avg_income", False)
    print("\nDone. *whew*")
    
main()