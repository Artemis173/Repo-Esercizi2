import tensorflow as tf
#tf.config.set_visible_devices([], 'GPU')

import numpy as np

# python3 -m venv .cyber
# . .cyber/bin/activate

# deactivate

"""
conoscete lo XOR?
0 XOR 0 => 0
1 XOR 1 => 0
0 XOR 1 => 1
1 XOR 0 => 1
Cercheremo di addestrare una rete neurale per 
apprendere come funziona lo XOR
"""
# Dati booleani per l'operatore XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0],    [1],    [1],    [0]])  # Risultati dell'operatore XOR
#y = np.array([[0],    [0],    [0],    [1]])  # Risultati dell'operatore AND
#y = np.array([[0],    [1],    [1],    [1]])  # Risultati dell'operatore OR

# 0\
#   > 0 
# 0/
# Creare il modello di rete neurale
# Un modello sequenziale è una pila di livelli
model = tf.keras.models.Sequential()

# Aggiungere i livelli alla rete neurale
# Un livello denso è un livello completamente connesso con una funzione di attivazione relu
# il primo livello è 2x16
model.add(tf.keras.layers.Dense(2, activation=tf.keras.activations.relu, input_shape=(2,)))

# #un esempio di relu
# def MyRelu(x):
#     if x <= 0:
#         return 0
#     else:
#         return x


# Entro con un vettore lungo 2
# Esco con un vettore lungo 1
# Internamente ho una matrice 2*16 e in uscita ho una matrice 16*1

# Un altro livello denso (16x1) con una funzione di attivazione sigmoide
model.add(tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid))

# Compilare il modello specificando l'ottimizzatore, la funzione di perdita e la metrica da usare
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.3), loss=tf.keras.losses.MeanSquaredError(), metrics=[tf.keras.metrics.Accuracy()])

# Adattare il modello ai dati di input e output per 100 epoche
model.fit(X, y, epochs=10)

# Prevedere i valori di output per i dati di input
predictions = model.predict(X)
print(predictions)
