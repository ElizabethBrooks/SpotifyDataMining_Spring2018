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
#Scatter plot of danceability vs tempo colored by bin
plt.scatter(X[y==0]['Tempo'], X[y==0]['Loudness'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Tempo'], X[y==1]['Loudness'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Tempo'], X[y==2]['Loudness'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Tempo'], X[y==3]['Loudness'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Tempo'], X[y==4]['Loudness'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Tempo'], X[y==5]['Loudness'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Tempo')
plt.ylabel('Loudness')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_loudnessTempo.png', bbox_inches='tight')
