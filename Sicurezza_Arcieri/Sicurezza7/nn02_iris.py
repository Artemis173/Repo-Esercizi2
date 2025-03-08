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

def ConvertiY(y):
    ly = []
    for vy in y:
        if vy == 0:
            ly.append([1,0,0])
        elif vy == 1:
            ly.append([0,1,0])
        else:
            ly.append([0,0,1])
    return np.array(ly)

y = ConvertiY

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu, input_shape=(4,)))
model.add(tf.keras.layers.Dense(32, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(1, activation=tf.keras.activations.softmax))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.3), loss=tf.keras.losses.MeanSquaredError(), metrics=[tf.keras.metrics.Accuracy()])
model.fit(X, y, epochs=100)

predictions = model.predict(X)
print(predictions)

for vx, vy in zip(predictions, y):
    print(vx, vy)
