import time
import pandas as pd
import numpy as np

# Initializing lists
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_LIST = ['all','january', 'february', 'march', 'april', 'may', 'june', '']
DAYS_LIST = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', '']
ANSWERS_LIST = ["yes", "no"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\n' + '-'*40+ '\n')
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nWould you like to see the data for Chicago, New York or Washington ?: ").lower()

    while city not in CITY_DATA.keys():
        print("\nPlease, choose one of these options: Chicago, New York or Washington.")
        city = input("\nWould you like to see the data for Chicago, New York or Washington ?: ").lower()



    print('\n' + '-'*40+ '\n')
    # get user input for month (all, january, february, ... , june)
    month = input("\nWhich month? January, February, March, April, May, June or you can enter \"All\" or leave it blank to get data for all months: ").lower()
    
    while month not in MONTHS_LIST:
        print("\nPlease, choose one of these options: January, February, March, April, May, June or you can enter \"All\" or leave it blank to get data for all months.")
        month = input("\nWhich month? January, February, March, April, May, June or you can enter \"All\" or leave it blank to get data for all months: ").lower()



    print('\n' + '-'*40+ '\n')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or you can enter \"All\" or leave it blank to get data for all days: ").lower()
    
    while day not in DAYS_LIST:
        print("\nPlease, choose one of these options: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or you can enter \"All\" or leave it blank to get data for all days.")
        day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or you can enter \"All\" or leave it blank to get data for all days: ").lower()



    print('\n' + '-'*40+ '\n')
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    # Loading data for city
    df = pd.read_csv(CITY_DATA[city])
    print('Processing Data...\n\n' + '-'*40)

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Getting month of each date
    df['month'] = df['Start Time'].dt.month

    # Getting Day name of each date
    df['day'] = df['Start Time'].dt.day_name()

    # Filtring Data By Month
    if month != "all" and month !="":
        # Getting month position in the year
        month = MONTHS_LIST.index(month)

        # Create a new DataFrame with only the specified month
        df = df[df['month'] == month]


    # Filtring Data By Day Name
    if day != "all" and day !="":

        # Create a new DataFrame with only the specified day
        df = df[df['day'] == day.title()]
    

    # Return a DataFrame with the specified filters
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # Get the most common month
    most_common_month = df['month'].mode()[0]

    # Display the most common month
    print("\nThe most popular month is: {}.".format(most_common_month))

    # Get the most common day of week
    most_common_day = df['day'].mode()[0]

    # Display the most common day of week
    print("\nThe most popular day is: {}.".format(most_common_day))
    
    # Getting Day name of each start date
    df['day'] = df['Start Time'].dt.day_name()

    # Creating Year column from Start Time column
    df['hour'] = df['Start Time'].dt.hour

    # Get the most common start hour
    most_common_hour = df['hour'].mode()[0]

    # Display the most common start hour
    print("\nThe most popular hour is: {}.".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # get most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]

    # display most commonly used start station
    print("\nThe most used START station is: {}.".format(most_used_start_station))

    # get most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]

    # display most commonly used end station
    print("\nThe most used END station is: {}.".format(most_used_end_station))

    # Creating a new column that combines the start and end station
    df['Trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')

    # Get most frequent combination of start station and end station trip
    most_freq_combination = df['Trip'].mode()[0]

    # Display most frequent combination of start station and end station trip
    print("\nThe most frequent combination of start station and end station trip is: {}.".format(most_freq_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def limiting_floats(float_var):
    """
    Limiting floats to two decimal points

    Arg:
        (float) float_var - the float variable that will be limited to 2 decimal places.

    return:
        (str) string of the float_var float with 2 decimal places.
    """

    return "{:.2f}".format(float_var)


def print_duration(calculation_type, time_list):
    """
    Adaptting time printing according to the minutes (more or less then one hour)

    Args:
        (str) calculation_type - name of the calculation type (total or mean)
        (list) time_list - list of hours, minutes and seconds values
    """

    if time_list[0] == 0 and time_list[1] < 60:
        print("\nThe %s travel duration is: %s minutes and %s seconds." % (calculation_type, limiting_floats(time_list[1]), limiting_floats(time_list[2])))
    else:
        print("\nThe %s travel duration is: %s hours, %s minutes and %s seconds."% (calculation_type, limiting_floats(time_list[0]), limiting_floats(time_list[1]), limiting_floats(time_list[2])))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...')
    start_time = time.time()

    # Get total travel time in minutes and seconds
    total_time_min, total_time_sec = divmod(df['Trip Duration'].sum(), 60)

    # Get total travel time in hours
    total_time_hr, total_time_min = divmod(total_time_min, 60)

    # Display total travel time
    print_duration("total", [total_time_hr, total_time_min, total_time_sec])

    # Get mean travel time in minutes and seconds
    mean_time_min, mean_time_sec = divmod(df['Trip Duration'].mean(), 60)

    # Get total travel time in hours
    mean_time_hr, mean_time_min = divmod(mean_time_min, 60)

    # Display mean travel time
    print_duration("mean", [mean_time_hr, mean_time_min, mean_time_sec])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Replace the blank values of User Type by "Not Specified"
    df['User Type'] = df['User Type'].fillna("Not Specified")

    # Get counts of user types
    users_types = df['User Type'].value_counts()

    # Display counts of user types
    for key in users_types.keys():
        if key != "Not Specified":
            # Display counts of specified accounts types
            print("\nThe %s type has: %s users." % (key, users_types.get(key)))
        else: 
            # Display counts of unspecified accounts types
            print("\nThere are %s users without a specifies user type." % (users_types.get(key)))
    
    # Trying to execute the code of Gender column
    try:
        # Replace the blank values of gender by "Not Specified"
        df['Gender'] = df['Gender'].fillna("Not Specified")

        # Get counts of gender
        gender = df['Gender'].value_counts()

        # Display counts of each gender
        print("\nThere are %s female users and %s male users." % (gender.get('Female'), gender.get('Male')))
        
        if len(gender) != 2:
            print("\nThere are %s users that has not specified their gender." % (gender.get('Not Specified')))
    except:
        # Handling the error when the gender column doesn't exist
        print("\nSorry, it seems that the user's gender has not been entered for this city.")
    
    # Trying to execute the code of Birth Year column
    try:
        # Get earliest year of birth
        earliest_year = int(df['Birth Year'].min())

        # Display earliest year of birth
        print("\nThe earliest year of birth is: {}.".format(earliest_year))
        
        # Get most recent year of birth
        recent_year = int(df['Birth Year'].max())

        # Display most recent year of birth
        print("\nThe most recent year of birth is: {}.".format(recent_year))

        # Get most common year of birth
        most_common_year = int(df['Birth Year'].mode()[0])

        # Display most common year of birth
        print("\nThe most common year of birth is: {}.".format(most_common_year))
    except:
        # Handling the error when the Birth Year column doesn't exist
        print("\nSorry, it seems that the user's birth year has not been entered for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data_input():
    """
    Asking user if he wants to see the next five rows

    retrun:
        (str) view_response - the user answer if he wants to see more data or not
    """

    print('-'*40)
    # Getting user answer
    view_response = input("\nWould you like to view the next five rows of the used data?: Enter yes or no: ")

    # Handling user answers if it's not as expected
    while view_response not in ANSWERS_LIST:

        # Guiding the user to the expected answers
        print("\nPlease, choose one of these options: Yes or No.")

        # Getting user answer
        view_response = input("\nWould you like to view the next five rows of the used data?: ").lower()

    return view_response


def diplay_data(df):
    """
    Displaying the used data if the user wants that

    arg:
        (Pandas DataFrame) df - dataframe choosed by user (using the filters)

    """
    # Initializing rows counter
    count = 0

    # Asking user if he want to see the first five rows
    view_response = input("\nDo you want to see the first five rows of the used data? Enter yes or no: ")

    # Handling user answers if it's not as expected
    while view_response not in ANSWERS_LIST:

        # Guiding the user to the expected answers
        print("\nPlease, choose one of these options: Yes or No.")

        # Getting user response
        view_response = input("\nWould you like to see the first five rows of the used data?: ").lower()

    if view_response == "yes":
        # Display the first five rows of the used data
        print(df.head())

        # Asking user if he wants to see more data
        view_response = view_data_input()

        while view_response == "yes":

            # Adjusting the rows counter to point to the next five rows
            count += 5

            # Trying to display the next five rows and if that's impossible it means that the user has reached the limits
            try: 
                # Display the next five rows of the used data
                print(df[count:count+5])

                # Asking user if he wants to see more data
                view_response = view_data_input()
            except:
                # Telling the users that they have reached the limits of viewable data
                print("\nSorry, there is no more raw data to display.")
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        diplay_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
