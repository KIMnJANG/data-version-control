import dvc.api
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, Input, Model

with dvc.api.open(
    "data/dataset.npz", repo="https://github.com/ssuwani/dvc-tutorial", mode="rb"
) as fd:
    dataset = np.load(fd)
    train_x = dataset["train_x"]
    train_y = dataset["train_y"]
    test_x = dataset["test_x"]
    test_y = dataset["test_y"]

inputs = Input(shape=(28, 28))
x = layers.Flatten()(inputs)
x = layers.Dense(128, activation="relu")(x)
outputs = layers.Dense(10, activation="softmax")(x)

model = Model(inputs, outputs)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["acc"])

model.fit(train_x, train_y, epochs=3)

loss, acc = model.evaluate(test_x, test_y)
print(f"model Loss: {loss:.4f} acc: {acc:.4f}")
