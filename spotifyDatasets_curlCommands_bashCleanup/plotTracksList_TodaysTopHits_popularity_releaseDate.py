#Name: Elizabeth Brooks
#File: plotTracksList_TodaysTopHits_popularity_releaseDate.py
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
with open("tracksList_TodaysTopHits_popularity.txt","r") as file:
        for line in file:
                popularities.append(int(line))
#Retrieve release dates
release_dates = []
with open("tracksList_TodaysTopHits_releaseDate.txt","r") as file:
        for line in file:
                release_dates.append(line)
#Format dates
release_dates = [pd.to_datetime(d) for d in release_dates]
# plot
plt.scatter(release_dates,popularities)
plt.ylabel('Track Popularity')
plt.xlabel('Release Date')
# Save the figure
plt.savefig('spotify_TodaysTopHIts_popularity_releaseDate_plot.png', bbox_inches='tight')
