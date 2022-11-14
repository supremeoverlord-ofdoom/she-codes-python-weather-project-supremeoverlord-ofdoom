import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"  #this is a constant 

#can leave doc strings in
#add functions for the doc strings descriptions

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    from datetime import datetime
    y = datetime.fromisoformat(iso_string) #converts string into datetime in iso format
    y_year = y.year
    y_weekday = y.strftime("%A")
    y_day = y.strftime("%d")
    y_month = y.strftime("%B")
    formatted_date = f"{y_weekday} {y_day} {y_month} {y_year}"
    return(formatted_date)
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit = float(temp_in_farenheit) #convert to float
    temp_in_celcius = ((temp_in_farenheit -32) * 5/9) #converts fahrenheit to celcius
    temp_in_celcius = float("{:.1f}".format(temp_in_celcius)) #store as 2 decimal places as float
    return temp_in_celcius
    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    for num in weather_data:
        num = float(num)
        total += num
        mean = (total/len(weather_data))
    return mean
    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    import csv
    stored_data_list = []
    rows = []
    with open(csv_file, encoding="utf-8") as csv_file: #encoding turns into binary string so computer can read it
        reader = csv.reader(csv_file)  #reader allows us to loop over lines in csv
        next(reader)
        for line in reader:
            if line != []: #if line not blank
                rows.append([line[0], int(line[1]), int(line[2])])
    return rows
    pass

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    weather_data_num = []
    for num in weather_data:
        weather_data_num.append(float(num))
    # print(weather_data_num)
    min_temp = min(weather_data_num, default=None)
    location = [i for i in range(len(weather_data_num)) if weather_data_num[i]==min_temp]
    if len(location) >1:
        location = location[1]
    elif min_temp == None:
        location = None
    else:
        location = location[0]

    if min_temp == None:
        result = ()  # otherwise it will do weird stuff
    else:
        result = (min_temp, location)
    return result
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    
    weather_data_num = []
    for num in weather_data:
        weather_data_num.append(float(num))
    # print(weather_data_num)
    max_temp = max(weather_data_num, default=None)
    location = [i for i in range(len(weather_data_num)) if weather_data_num[i]==max_temp]
    if len(location) >1:
        location = location[1]
    elif max_temp == None:
        location = None
    else:
        location = location[0]

    if max_temp == None:
        result = ()  # otherwise it will do weird stuff
    else:
        result = (max_temp, location)
    return result
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    num_of_days = len(weather_data)
    weather_data_lows_list = []
    weather_data_highs_list = []

    for item in weather_data:
        weather_data_lows_list.append(item[1])
    for item in weather_data:
        weather_data_highs_list.append(item[2])

    # weather_data_ultimate_list = weather_data_lows_list + weather_data_highs_list
    # print(weather_data_ultimate_list)

    # max_temp_and_location = find_max(weather_data_ultimate_list) #hashing out for now because there is a possible error in assignment
    max_temp_and_location = find_max(weather_data_highs_list)
    max_temp_value = max_temp_and_location[0]
    max_temp_value_celcius = convert_f_to_c(max_temp_value)

    # min_temp_and_location = find_min(weather_data_ultimate_list) #hashing out for now because there is a possible error in assignment
    min_temp_and_location = find_min(weather_data_lows_list)
    min_temp_value = min_temp_and_location[0]
    min_temp_value_celcius = convert_f_to_c(min_temp_value)

    for item in weather_data:
        if min_temp_value == item[1] or min_temp_value == item[2]:
            min_temp_date = item[0]
    min_temp_date_formatted = convert_date(min_temp_date)


    for item in weather_data:
        if max_temp_value == item[1] or max_temp_value == item[2]:
            max_temp_date = item[0]
    max_temp_date_formatted = convert_date(max_temp_date)

    #finding the average highs and lows
    mean_lows = calculate_mean(weather_data_lows_list)
    mean_lows = convert_f_to_c(mean_lows)
    mean_highs = calculate_mean(weather_data_highs_list)
    mean_highs= convert_f_to_c(mean_highs)
    summary = f"{num_of_days} Day Overview\n  The lowest temperature will be {min_temp_value_celcius}°C, and will occur on {min_temp_date_formatted}.\n  The highest temperature will be {max_temp_value_celcius}°C, and will occur on {max_temp_date_formatted}.\n  The average low this week is {mean_lows}°C.\n  The average high this week is {mean_highs}°C.\n"
    return summary
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
