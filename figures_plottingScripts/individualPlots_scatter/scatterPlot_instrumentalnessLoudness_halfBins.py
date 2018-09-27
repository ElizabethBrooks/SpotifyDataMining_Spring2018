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
#Scatter plot of danceability vs loudness colored by bin
plt.scatter(X[y==0]['Instrumentalness'], X[y==0]['Loudness'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Instrumentalness'], X[y==1]['Loudness'], label='0 < Popularity < 25', c='red')
plt.scatter(X[y==2]['Instrumentalness'], X[y==2]['Loudness'], label='24 < Popularity < 50', c='red')
plt.scatter(X[y==3]['Instrumentalness'], X[y==3]['Loudness'], label='49 < Popularity < 75', c='blue')
plt.scatter(X[y==4]['Instrumentalness'], X[y==4]['Loudness'], label='74 < Popularity < 100', c='blue')
plt.scatter(X[y==5]['Instrumentalness'], X[y==5]['Loudness'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Instrumentalness')
plt.ylabel('Loudness')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_loudnessInstrumentalness_halfBins.png', bbox_inches='tight')