import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

print("--- Step 3.1: Loading MNIST Dataset ---")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("--- Step 3.2: Preprocessing Data ---")
# Reshape data to 4D tensors (samples, height, width, channels)
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

# Normalize pixel values from [0, 255] to [0.0, 1.0]
X_train = X_train / 255.0
X_test = X_test / 255.0

# One-hot encode targets
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("--- Step 3.3: Building CNN Architecture ---")
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

print("--- Step 3.4: Compiling Model ---")
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

print("--- Step 3.5: Training Model ---")
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2)

print("--- Step 3.6: Evaluating Model ---")
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTraining Complete! Test Accuracy: {accuracy * 100:.2f}%")

print("--- Step 3.7: Saving Model Weights ---")
model.save("handwritten_model.h5")
print("Model saved successfully as 'handwritten_model.h5'")