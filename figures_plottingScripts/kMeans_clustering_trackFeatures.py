from sklearn.cluster import KMeans
import pandas as pd 
#Retrieve track features and popularities and store in data frame
cols =  ['TrackID', 'Popularity', 'FeatureID', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 
         'Speechiness', 'Acousticness', 'Instrumentalness', 'Livenss', 
         'Valence', 'Tempo', 'TimeSignature', 'Duration', 'Bin']
df_train = pd.read_csv('trackFeatures_totalTrackFeaturesMapped_train.csv', names=cols)
y_train = df_train['Popularity']          # Split off classifications
X_train = df_train.ix[:, 'Danceability':'Duration'] # Split off features
#Initialize kMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(df_train)
#Learn labels
labels = kmeans.predict(x_train)
centroids = kmeans.cluster_centers_
#Plot clusters
fig = plt.figure(figsize=(5, 5))
colors = map(lambda x: colmap[x+1], labels)
plt.scatter(df_train['x'], df_train['y'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colmap[idx+1])
plt.xlim(0, 80)
plt.ylim(0, 80)
#Display plot
plt.show()
