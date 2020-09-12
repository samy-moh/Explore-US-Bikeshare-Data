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
    print("Hello! My name is Samy and I'm here to help you explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter which city you want to analyze (chicago/new york city/washington): ").lower()

    while city not in ["chicago","new york city","washington"] :
        city = input("Invalid city please re-enter city as (chicago/new york city/washington) : ").lower()

    # get user input for month (all, january, february, ... , june)
        
    month = input("good, which month you want to analyze , You can choose from (january to june, or you can type (all) for all monthes) :" ).lower()

    while month not in ["january","february","march","april","may","june","all"]:
        month = input("Invalid month ,(please type in full month name or type all ) : ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('good, what day you want to analyze or just type(all) for all week : ').lower()

    while day not in ["saturday","sunday","monday","tuesday","wednesday","thursday","friday","all"]:
        day = input("Invalid day ,(please type in full day name or type all ) : ").lower()



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
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name.str.lower()
    

    if month != "all":
        all_monthes = ["january","february","march","april","may","june"]
        month = all_monthes.index(month) + 1

        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day"] == day]

    df = df.dropna(axis=0)



    return df



def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months_names = ["January","February","March","April","May","June"]

    month_index = months_names[(df["month"].mode()[0]) - 1]
   
    # display the most common month
    if month == "all":
        print("Here's the most common month : " + str(month_index))


    # display the most common day of week
    if day == "all":
        print("Here's the most common day : " + str(df["day"].mode()[0]))

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour

    print("Here's the most common start hour : " + str(df["hour"].mode()[0]))
    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Here's the most commonly start station : " + str(df["Start Station"].mode()[0]))


    # display most commonly used end station
    print("Here's the most commonly end station : " + str(df["End Station"].mode()[0]))


    # display most frequent combination of start station and end station trip
    most_trip = df["Start Station"] + " To " + df["End Station"]
    print("Here's the most commonly combination of start station and end station trip : " + str(most_trip.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print("The total travel time is : "+ str(df["Trip Duration"].sum() / 60 / 60) + " Hours")


    # display mean travel time
    print("The average travel time is : " + str(df["Trip Duration"].mean() / 60) + " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_type = df["User Type"].value_counts()
    print("Here's the count of user typs : \n" + counts_type.to_string())

    print("-"*10)


    # Display counts of gender

    if city != "washington":
        counts_gender = df["Gender"].value_counts()
        print("Here's the count of user gender : \n" + counts_gender.to_string())
        print("-"*10)


    # Display earliest, most recent, and most common year of birth

        print("The earlist birth year is : " + str(int(df["Birth Year"].min())))
        print("-"*10)

        print("The most recent birth year is : " + str(int(df["Birth Year"].max())))
        print("-"*10)

        print("Finally , The most common birth year is : " + str(int(df["Birth Year"].mode()[0])))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):

    user_request = input("Do you want to see some raw data? (yes or no) ").lower()

    start_raw = 0
    end_raw = 5

    if user_request == "yes":
        while True:
            
            print(df.iloc[start_raw:end_raw])

            start_raw += 5
            end_raw += 5

            user_request = input("show more data(yes or no) ??")

            if user_request == "no":
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
