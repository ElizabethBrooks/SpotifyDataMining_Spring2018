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
#plt.legend()
plt.xlabel('Energy')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityEnergy.png', bbox_inches='tight')
#Scatter plot of danceability vs key colored by bin
plt.scatter(X[y==0]['Key'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Key'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Key'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Key'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Key'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Key'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Key')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityKey.png', bbox_inches='tight')
#Scatter plot of danceability vs loudness colored by bin
plt.scatter(X[y==0]['Loudness'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Loudness'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Loudness'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Loudness'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Loudness'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Loudness'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Loudness')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityLoudness.png', bbox_inches='tight')
#Scatter plot of danceability vs mode colored by bin
plt.scatter(X[y==0]['Mode'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Mode'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Mode'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Mode'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Mode'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Mode'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Mode')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityMode.png', bbox_inches='tight')
#Scatter plot of danceability vs speechiness colored by bin
plt.scatter(X[y==0]['Speechiness'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Speechiness'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Speechiness'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Speechiness'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Speechiness'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Speechiness'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Speechiness')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilitySpeechiness.png', bbox_inches='tight')
#Scatter plot of danceability vs acousticness colored by bin
plt.scatter(X[y==0]['Acousticness'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Acousticness'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Acousticness'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Acousticness'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Acousticness'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Acousticness'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Acousticness')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityAcousticness.png', bbox_inches='tight')
#Scatter plot of danceability vs instrumentalness colored by bin
plt.scatter(X[y==0]['Instrumentalness'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Instrumentalness'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Instrumentalness'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Instrumentalness'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Instrumentalness'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Instrumentalness'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Instrumentalness')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityInstrumentalness.png', bbox_inches='tight')
#Scatter plot of danceability vs valence colored by bin
plt.scatter(X[y==0]['Valence'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Valence'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Valence'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Valence'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Valence'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Valence'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Valence')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityValence.png', bbox_inches='tight')
#Scatter plot of danceability vs tempo colored by bin
plt.scatter(X[y==0]['Tempo'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Tempo'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Tempo'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Tempo'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Tempo'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Tempo'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Tempo')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityTempo.png', bbox_inches='tight')
#Scatter plot of danceability vs time signature colored by bin
plt.scatter(X[y==0]['TimeSignature'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['TimeSignature'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['TimeSignature'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['TimeSignature'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['TimeSignature'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['TimeSignature'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('TimeSignature')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityTimeSignature.png', bbox_inches='tight')
#Scatter plot of danceability vs tempo colored by bin
plt.scatter(X[y==0]['Duration'], X[y==0]['Danceability'], label='Popularity = 0', c='red')
plt.scatter(X[y==1]['Duration'], X[y==1]['Danceability'], label='0 < Popularity < 25', c='green')
plt.scatter(X[y==2]['Duration'], X[y==2]['Danceability'], label='24 < Popularity < 50', c='orange')
plt.scatter(X[y==3]['Duration'], X[y==3]['Danceability'], label='49 < Popularity < 75', c='purple')
plt.scatter(X[y==4]['Duration'], X[y==4]['Danceability'], label='74 < Popularity < 100', c='pink')
plt.scatter(X[y==5]['Duration'], X[y==5]['Danceability'], label='Popularity = 100', c='blue')
#Prettify the graph
#plt.legend()
plt.xlabel('Duration')
plt.ylabel('Danceability')
#Show plot
#plt.show()
#Save plot
plt.savefig('scatterPlot_danceabilityDuration.png', bbox_inches='tight')
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
