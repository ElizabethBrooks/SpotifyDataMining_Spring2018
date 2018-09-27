import matplotlib as mpl
## agg backend is used to create plot as a .png file
mpl.use('agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
#Retrieve track features and popularities and store in data frame
cols =  ['TrackID', 'Popularity', 'FeatureID', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 
         'Speechiness', 'Acousticness', 'Instrumentalness', 'Livenss', 
         'Valence', 'Tempo', 'TimeSignature', 'Duration', 'Bin']
data = pd.read_csv('trackFeatures_totalTrackFeaturesMapped_shuffled_binned.csv', names=cols)
y = data['Bin']          # Split off classifications
X = data.ix[:, 'Danceability':'Duration'] # Split off features
#Scatter plot of danceability vs energy colored by bin
plt.scatter(X[y==0]['Energy'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Energy'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Energy'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Energy'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Energy'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Energy'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
plt.legend()
plt.xlabel('Energy')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityEnergy_legendIncluded.png', bbox_inches='tight')
