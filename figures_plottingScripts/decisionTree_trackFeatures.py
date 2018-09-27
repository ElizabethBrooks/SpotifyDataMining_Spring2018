from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd 
#Retrieve track features and popularities and store in data frame
cols =  ['TrackID', 'Popularity', 'FeatureID', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 
         'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 
         'Valence', 'Tempo', 'TimeSignature', 'Duration', 'Bin']
df_train = pd.read_csv('trackFeatures_totalTrackFeaturesMapped_train.csv', names=cols)
y_train = df_train['Popularity']          # Split off classifications
X_train = df_train.ix[:, 'Danceability':'Duration'] # Split off features
####
# Building Decision Tree - CART Algorithm (gini criteria)
dt_train_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
# Train
dt_train_gini.fit(X_train, y_train)
#Export for visualization
with open("dt_train_gini_popularity.txt", "w") as f:
    f = tree.export_graphviz(dt_train_gini, out_file=f)
