#pip install scikit-learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
iris = load_iris()

data, labels = iris.data, iris.target

res = train_test_split(data, labels, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=42)
train_data, test_data, train_labels, test_labels = res

print()

x = np.array([[0, 0], [0, 1], [1, 1]])
y = np.array([[0],  [1],  [1],   [0]])
print()

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, activation=tf.keras.activations.relu, input_shape=(2,)))
model.add(tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.3), loss=tf.keras.losses.MeanSquaredError(), metrics=[tf.keras.metrics.Accuracy()])
model.fit(x, y, epochs=100)

predictions = model.predict(X)
print(predictions)
