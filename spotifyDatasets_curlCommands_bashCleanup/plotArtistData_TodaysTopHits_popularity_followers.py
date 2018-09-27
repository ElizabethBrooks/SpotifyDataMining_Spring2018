#Name: Elizabeth Brooks
#File: plotArtistData_TodaysTopHits_popularity_followers.py
#Modified: 2 March 2018
#Imports
import pandas as pd
import matplotlib as mpl
## agg backend is used to create plot as a .png file
mpl.use('agg')
import matplotlib.pyplot as plt
#Initialize variables
#Retrieve popularity
popularities = []
with open("artistData_TodaysTopHits_popularity.txt","r") as file:
        for line in file:
                popularities.append(int(line))
#Retrieve release dates
followers = []
with open("artistData_TodaysTopHits_followers.txt","r") as file:
        for line in file:
                followers.append(int(line))
# plot
plt.scatter(followers,popularities)
plt.ylabel('Artist Popularity')
plt.xlabel('Number of Followers')
# Save the figure
plt.savefig('spotify_TodaysTopHIts_popularity_followers_plot.png', bbox_inches='tight')
