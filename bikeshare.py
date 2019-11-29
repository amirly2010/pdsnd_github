#  2- Improve Documentation (third time)....
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    city = input('\n Please, select which city would you like(Chicago, New york , Washington)?\n').lower()
    while True:
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            city = input('Sorry,this is invalid inputs; (Please, Enter the correct city):\n').lower()
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nPlease, select which month would you prefer? \n"
                      "(january, february, march, april, may, june, or all )\n").lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            month = input('Sorry,this is invalid inputs; (Please, Enter the correct month):\n').lower()
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nPlease, select which day would you prefer? \n"
                    "(monday, tuesday, wednesday, thursday, friday, saturday , sunday or all)\n").lower()
        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            day = input('Sorry,this is invalid inputs; (Please, Enter the correct day):\n').lower()
            break
    print('Your selections are:\n', 'city is:', city, '&', 'month is:', month, '&', 'day is :', day)
    print('-' * 40)
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
    # TO loads data and convert column (Start time) in to datetime
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO extract month and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # To filter by month
  
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

        # TO filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n...Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # To display the most common month
    com_month = df['month'].mode()[0]
    print('The Common (Month):', com_month)

    # To display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print('The Common (day):', com_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    print('The Common (Hour):', com_hour)

    print("\nThis took %s (seconds)." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n...Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO  display most  used start station
    st_station = df['Start Station'].value_counts().idxmax()
    print('The Most  used start station:\n', st_station)

    # TO  display most  used end station

    en_station = df['End Station'].value_counts().idxmax()
    print('\nThe most  used end station:\n', en_station)

    # TO  display most frequent combination of start station and end station trip

    comb_station = df['Start Station'] + df['End Station']
    freq_comb = comb_station.value_counts().idxmax()
    print('\nThe most  used combination of start station and end station trip:\n', freq_comb)

    print("\nThis took %s (seconds)." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n...Calculating Trip Duration...\n')
    start_time = time.time()

    # TO display total travel time
    aggregate_time = sum(df['Trip Duration'])
    m, s = divmod(aggregate_time, 60)
    h, m = divmod(m, 60)
    d = aggregate_time // (24 * 3600)
    print('The total travel time (total days)', d, '(days)')
    print('In details.....\n{} (hours) & {} (minutes) & {} (seconds)'.format(h, m, s))

    #  TO display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is:', mean_time / 60, " (minutes)")
    print("\nThis took %s (seconds)." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n...Calculating User Stats...')
    start_time = time.time()
    # TO Display counts of user types
    print('\n...Display counts of user types...')
    user_types = df['User Type'].value_counts()
    print('User Types are:\n', user_types)

    #  TO Display counts of gender
    if 'Gender' in df.columns:
        print('\n...Display counts of gender...')
        gender = df['Gender'].value_counts()
        print('The count of (male/ female) users are\n', gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\n...Display earliest, most recent, and most common year of birth...\n')
        ear_birth = df['Birth Year'].min()
        rec_birth = df['Birth Year'].max()
        com_birth = df['Birth Year'].mode()
        print('The earliest birth year is:\n', int(ear_birth))
        print('The recent birth year is:\n', int(rec_birth))
        print('The common birth year is:\n', int(com_birth))
    print("\nThis took %s (seconds)." % (time.time() - start_time))
    print('-' * 40)
    
    
def display_raw(df):
    raw_data1 = input('Do you want to see raw data? Please, Enter: (yes / no).\n').lower()
    num_1 = 0
    num_2 = 5
    while True:
        if raw_data1 != 'no':
            num_raw1 = df.iloc[num_1: num_2]
            print(num_raw1)
            raw_data1 = input('\nDo you want to see more raw data? Please, Enter: (yes / no).\n').lower()
            num_1 += 5
            num_2 += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
