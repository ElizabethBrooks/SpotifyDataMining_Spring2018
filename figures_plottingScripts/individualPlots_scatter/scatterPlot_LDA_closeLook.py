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
####
#Normalize data
X_norm = (X - X.min())/(X.max() - X.min())
####
#Linear discriminant analysis
lda = LDA(n_components=2) #2-dimensional LDA
lda_transformed = pd.DataFrame(lda.fit_transform(X_norm, y))
# Plot all three series
plt.scatter(lda_transformed[y==1][0], lda_transformed[y==1][1], label='0 < Popularity < 25', c='green')
plt.scatter(lda_transformed[y==2][0], lda_transformed[y==2][1], label='24 < Popularity < 50', c='orange')
# Display legend and show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_LDA_bins1and2.png', bbox_inches='tight')
#Linear discriminant analysis
lda = LDA(n_components=2) #2-dimensional LDA
lda_transformed = pd.DataFrame(lda.fit_transform(X_norm, y))
# Plot all three series
plt.scatter(lda_transformed[y==0][0], lda_transformed[y==0][1], label='Popularity = 0', c='red')
plt.scatter(lda_transformed[y==3][0], lda_transformed[y==3][1], label='49 < Popularity < 75', c='purple')
plt.scatter(lda_transformed[y==4][0], lda_transformed[y==4][1], label='74 < Popularity < 100', c='pink')
plt.scatter(lda_transformed[y==5][0], lda_transformed[y==5][1], label='Popularity = 100', c='blue')
# Display legend and show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_LDA_remainingBins.png', bbox_inches='tight')
