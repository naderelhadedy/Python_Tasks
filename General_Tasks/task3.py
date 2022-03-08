# content of file

#received_report = """ Hello from USA! FYI, today Tuesday 06-04-2021, we have deposited 200 USD at 18:20 PM 
#into your account and waiting your response """

# file handling
received_report = open(r"D:\AI_PRO\Content\2- Intro to python\task3.txt", "r")
received_report = received_report.read()


target_countries = ["USA", "UAE", "CA"]
country_currency = {
    "USA":"USD",
    "UAE":"AED",
    "CA":"CAD"
}

# values according to EGP
currency_value_to_head = {
    "USD":15.71,
    "AED":4.28,
    "CAD":12.5
}

# values according to EGP
time_amount_to_head = {
    "USA":6,
    "UAE":-2,
    "CA":6
}

week_days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

# unwanted things
punctuations = '''!()-[]{};:'",<>.'\'/?@#$%^&*_~'''

# handling the input
def get_report_data(received_report):

    report_data = received_report.split()

    counter = 0
    while counter < len(report_data):

        for symbol in punctuations:
            report_data[counter] = report_data[counter].replace(symbol, '')

        counter += 1
    return report_data

# extract country, currency, amount
def get_country_amount(report_data):

    target_country = ""
    for the_input in report_data:
        
        if the_input.isalpha() and the_input.upper() in target_countries:
            target_country = the_input.upper()

    target_currency = country_currency[target_country]
    converted_value = currency_value_to_head[target_currency]
    currency_index = report_data.index(target_currency)

    if report_data[currency_index-1].isnumeric():
        target_amount = report_data[currency_index-1]

    elif report_data[currency_index+1].isnumeric():
        target_amount = report_data[currency_index+1]

    else:
        target_amount = None

    
    return target_country, converted_value, int(target_amount)



import re
# extract date and time
def get_date_time(received_report):

    report_date = re.findall(r'\d{2}-\d{2}-\d{4}', received_report)
    report_time = re.findall(r'\d{2}:\d{2}\s\wM', received_report)

    return report_date[0], report_time[0]

# extract the day
def get_day(resulted_report, week_days):

    target_day = ""
    for word in resulted_report:
        if word.lower() in week_days:
            target_day = word.lower()

    return target_day

# convert data according to egypt
def convert_day_date_time(target_country, target_day, report_date, report_time):
    
    time_amount = time_amount_to_head[target_country]
    converted_time = str(time_amount + int(report_time[0:2])) + report_time[2:]
    converted_date = report_date
    converted_day = target_day

    if int(converted_time[0:2]) >= 24:
        converted_time = str(int(converted_time[0:2])-24) + converted_time[2:-2] + "AM"
        converted_date = str(int(report_date[0:2])+1) + report_date[2:]
        target_index_day = week_days.index(target_day) + 1

        if target_index_day > (len(week_days)-1):
            target_index_day = 0
        converted_day = week_days[target_index_day]

    return converted_day, converted_date, converted_time

# print final report
def print_report():

    print(f"Branch: {target_country}\nDay: {converted_day[0].upper() + converted_day[1:]}\n\
Date: {converted_date}\nTime: {converted_time}\nAmount: {converted_value*target_amount} EGP")


# handling outputs

resulted_report = get_report_data(received_report)

target_country, converted_value, target_amount = get_country_amount(resulted_report)

report_date, report_time = get_date_time(received_report)

target_day = get_day(resulted_report, week_days)

converted_day, converted_date, converted_time = convert_day_date_time(target_country, target_day, report_date, report_time)

# print final report
print_report()