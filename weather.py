import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"  # this is a constant

# can leave doc strings in
# add functions for the doc strings descriptions


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
    from datetime import datetime  # import datetime library
    # converts string into datetime in iso format
    y = datetime.fromisoformat(iso_string)
    y_year = y.year
    y_weekday = y.strftime("%A")
    y_day = y.strftime("%d")
    y_month = y.strftime("%B")
    formatted_date = f"{y_weekday} {y_day} {y_month} {y_year}"
    return (formatted_date)
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_farenheit = float(temp_in_farenheit)  # convert to float
    # converts fahrenheit to celcius
    temp_in_celcius = ((temp_in_farenheit - 32) * 5/9)
    # store as 2 decimal places as float
    temp_in_celcius = float("{:.1f}".format(temp_in_celcius))
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
        num = float(num)  # convert num to float
        total += num  # sum the numbers in the weather_data list
        mean = (total/len(weather_data))  # calculate mean
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
    # encoding turns into binary string so computer can read it
    with open(csv_file, encoding="utf-8") as csv_file:
        # reader allows us to loop over lines in csv
        reader = csv.reader(csv_file)
        next(reader)  # skips the first line in header (we don't want the headers)
        for line in reader:
            if line != []:  # if line not blank
                # append the fist item in the line, and the second and third items as integars
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
    # part 1: for each num in list of numbers, converting to float and appending them to a new list
    weather_data_num = []
    for num in weather_data:
        weather_data_num.append(float(num))
    # if there is no data then default if None so doesn't break if there is no data
    min_temp = min(weather_data_num, default=None)

    # part 2: finding location on list and if there is a repeat, finding both locations
    # **stuck here** This worked but I'm still not sure how are why
    location = [i for i in range(
        len(weather_data_num)) if weather_data_num[i] == min_temp]
    if len(location) > 1:  # if there is more than one location
        # we want the second location (this is for if there is a repeat value in the num list)
        location = location[1]
    elif min_temp == None:  # putting in a failsafe if there is no data coming in
        location = None
    else:
        # if there is no repeats and there is data in the num list then we want the first (only) location
        location = location[0]

    # part 3: putting together the result
    if min_temp == None:  # putting in a failsafe if there is no data coming in
        result = ()  # otherwise it will do weird stuff
    else:
        # setting the format of the result unless there is no data
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
    # part 1: for each num in list of numbers, converting to float and appending them to a new list
    weather_data_num = []
    for num in weather_data:
        weather_data_num.append(float(num))

    # part 2: finding location on list and if there is a repeat, finding both locations
    max_temp = max(weather_data_num, default=None)
    location = [i for i in range(
        len(weather_data_num)) if weather_data_num[i] == max_temp]
    if len(location) > 1:
        location = location[1]
    elif max_temp == None:
        location = None
    else:
        location = location[0]

    # part 3: putting together the result
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
    # part 1: making a list of the minimums and a list of the maximums

    num_of_days = len(weather_data)
    weather_data_lows_list = []
    weather_data_highs_list = []

    for item in weather_data:
        weather_data_lows_list.append(item[1])
    for item in weather_data:
        weather_data_highs_list.append(item[2])

    # redacted part: original approach to join both lists to find overall min and max but there is a mistake in the data
    # weather_data_ultimate_list = weather_data_lows_list + weather_data_highs_list
    # max_temp_and_location = find_max(weather_data_ultimate_list) #hashing out for now because there is a possible error in assignment
    # min_temp_and_location = find_min(weather_data_ultimate_list) #hashing out for now because there is a possible error in assignment

    # part 2: finding the min out of lists of mins and max out of list of max
    max_temp_and_location = find_max(weather_data_highs_list)
    max_temp_value = max_temp_and_location[0]
    max_temp_value_celcius = convert_f_to_c(max_temp_value)

    min_temp_and_location = find_min(weather_data_lows_list)
    min_temp_value = min_temp_and_location[0]
    min_temp_value_celcius = convert_f_to_c(min_temp_value)

    # part 3: finding the corresponding date in weather_data for the overall min and overall max
    for item in weather_data:
        if min_temp_value == item[1] or min_temp_value == item[2]:
            min_temp_date = item[0]
    # convert date from iso to text summary using previous function
    min_temp_date_formatted = convert_date(min_temp_date)

    for item in weather_data:
        if max_temp_value == item[1] or max_temp_value == item[2]:
            max_temp_date = item[0]
    # convert date from iso to text summary using previous function
    max_temp_date_formatted = convert_date(max_temp_date)

    # part 4: finding the mean of the mins list and max lists
    mean_lows = calculate_mean(weather_data_lows_list)
    # convert to celcius (converts float from fahrenheit to celcius)
    mean_lows = convert_f_to_c(mean_lows)
    mean_highs = calculate_mean(weather_data_highs_list)
    # convert to celcius (converts float from fahrenheit to celcius)
    mean_highs = convert_f_to_c(mean_highs)

    # Part 5: stringing all the calculated values together with an f string and n\ breaks
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
    # part 1: making a list with the sublists formatted to the right things
    formatted_list = []
    summary_string = f""
    for item in weather_data:
        formatted_list.append(
            [convert_date(item[0]), convert_f_to_c(item[1]), convert_f_to_c(item[2])])

    # part 2 for each of the items in the formatted list, add a string to the mega summary_string
    for item in formatted_list:
        summary_string += f"---- {item[0]} ----\n  Minimum Temperature: {item[1]}°C\n  Maximum Temperature: {item[2]}°C\n\n"
    return summary_string
    pass
