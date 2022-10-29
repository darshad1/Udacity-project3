import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington','all']
    while True:
        city = input('\nEnter the city name for which you want to see the data : Chicago, New York City, Washington \n')     
        city = city.lower()

        if city.lower() in cities:
            break
        else:
            print('\nYou have entered an invalid city name. Please re-enter from the list: Chicago, New York City, Washington \n')
              
    # get user input for month (all, january, february, ... , june)
    
    months = ['january', 'february','march','april','may','june','all']
    while True:
        month = input('\nEnter the month for which you want to see the data : January, February, March, April, May, June or Enter All for entire data \n' )
        month = month.lower()
        
        if month in months:
            break
        else:
            print('\nYou have entered an invalid month. Please re-enter from the list: January, February, March, April, May, June or Enter All for entire data')
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input('\nEnter the day for which you want to see the data : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or Enter All for entire data \n')
        day = day.lower()
        
        if day in days:
            break
        else:
            print('\nYou have entered an invalid day. Please re-enter from the list: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or Enter All for entire data \n')

    print('-'*40)
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
    df= pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day!='all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month is:',months[df['month'].mode()[0]-1],'\n' )

    # display the most common day of week
    print('The most common day of week  is ', df['day_of_week'].mode()[0], '\n')


    # display the most common start hour
    print('The most common day of start hour is ', df['Start Time'].dt.hour.mode()[0], '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common Start station is ', df['Start Station'].mode()[0], '\n')
    
    # display most commonly used end station
    print('The most common End station is ', df['End Station'].mode()[0], '\n')
    
    # display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] +' to '+ df['End Station']
    print('The most common Start to End station combination is ', df['start_end'].mode()[0], '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()/86400
    print('The total travel time ',total_travel_time,' Days')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('The mean travel time ',mean_travel_time, ' Minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics such as different type of users on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('The count of user types is :',user_types)
    except:
        print('\nUser data not available for this month\n')
    
    # Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('The count of gender is :',gender_types)
    except:
        print('\nGender data not available for this month\n')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].max()
        recent_yob = df['Birth Year'].min()
        common_yob = df['Birth Year'].mode()[0]
        print('The earliest year of birth is :', earliest_yob)
        print('The most recent year of birth is :', recent_yob)
        print('The most common year of birth is :', common_yob)
    except:
        print('\nYear of Birth data not available for this month\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df): 
    """Display 5 lines of raw data basis user input"""
    
    # Creating input list for validation
    option = ['yes','no']
    i=0
    t=i+5
    
    while True:
        choice = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n')
        choice = choice.lower()
        if choice.lower() in option:
            if choice !='yes':
                break
            else:
                while i<t:
                    print(df.iloc[i])
                    i=i+1
                t= i+5
        else:          
            print('\nInvalid Input. Please enter yes to see data or enter no to exit\n') 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
