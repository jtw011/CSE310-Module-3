import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the athlete events csv file
data = pd.read_csv('athlete_events.csv')

# Merge two data frames using pandas.merge() 
regions = pd.read_csv('datasets_31029_40943_noc_regions.csv')
merged = pd.merge(data, regions, on='NOC', how='left')

# Display the first five rows of each data set
def display_data_info():
    print(data.head())
    print(data.describe())
    print(data.info())

# New data frame that includes only the gold medalists
def display_gold_medals():
    goldMedals = merged[(merged.Medal == 'Gold')]

    #Graph of the number of gold medals by age
    plt.figure(figsize=(20,10))
    plt.title('Distubution of Gold Medals')
    sns.countplot(goldMedals['Age'])
    plt.show()
    
#Displays athletes who are gold medalists and older than 50
def display_gold_over_50():
    goldMedals = merged[(merged.Medal =='Gold')]
    masterDisciplines = goldMedals['Sport'][goldMedals['Age'] > 50]

    plt.figure(figsize=(20,10))
    plt.tight_layout()
    sns.countplot(masterDisciplines)
    plt.title('Gold Medals for Athletes Over 50')
    plt.show()

#Displays all women athletes who have played in the summer
#Shows the increase in women athletes after a period of time
def display_women_in_olympics():
    womenInOlympics = merged[(merged.Sex == 'F') & (merged.Season == 'Summer')]
    print(womenInOlympics.head(10))

# Graph
    sns.set(style="darkgrid")
    plt.figure(figsize=(20,10))
    sns.countplot(x='Year', data=womenInOlympics)
    plt.title('Women medals per edition of the Games')
    plt.show()

#prints the top 5 countries and show them in the graph with catplot
def display_top_countries():
    goldMedals = merged[merged.Medal == 'Gold']
    totalGoldMedals = goldMedals.region.value_counts().reset_index(name='Medal')
    totalGoldMedals.columns = ['Country', 'Medal']  # Use 'columns', not 'column'

    # Get the top 5 countries
    topGoldMedals = totalGoldMedals.head(5)
    #Graph 
    g = sns.catplot(x="Country", y="Medal", data=topGoldMedals, height=6, kind="bar", palette="muted")
    g.despine(left=True)
    g.set_xlabels("Top 5 Countries")
    g.set_ylabels("Number of Medals")
    plt.title('Medals per Country')
    plt.show()

# This is where the magic happens!
def main():
    while True:
        # print menu options and greeting
        print("Welcome to the olympic data program!")
        print("\nMenu:")
        print("1. Display Data Info")
        print("2. Display Gold Medalists")
        print("3. Display Gold Medalists Over 50")
        print("4. Display Women Athletes in Summer Olympics")
        print("5. Display Top Countries by Gold Medals")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
    # logic for the menu
        if choice == '1':
            display_data_info()
        elif choice == '2':
            display_gold_medals()
        elif choice == '3':
            display_gold_over_50()
        elif choice == '4':
            display_women_in_olympics()
        elif choice == '5':
            display_top_countries()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__== "__main__":
    main()