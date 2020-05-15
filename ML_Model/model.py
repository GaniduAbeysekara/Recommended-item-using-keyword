# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import pickle
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

product_descriptions = pd.read_csv('dataset/product_descriptions_original.csv')

# Removing duplicate entries :
product_descriptions.drop_duplicates(inplace=True)

# Missing values
product_descriptions = product_descriptions.dropna()

df_produits = product_descriptions.head(500)

# Converting the text in product description into numerical data for analysis
vectorizer = TfidfVectorizer(stop_words='english')
X1 = vectorizer.fit_transform(df_produits["product_description"])

# Save vectorizer.vocabulary_
pickle.dump(vectorizer.vocabulary_, open("models/train_vocabulary.h5", "wb"))

# Fitting K-Means to the dataset

X = X1

kmeans = KMeans(n_clusters=10, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)
plt.plot(y_kmeans, ".")
plt.show()


# # Optimal clusters is

true_k = 10

model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X1)

pickle.dump(model, open("models/train_model.h5", "wb"))
