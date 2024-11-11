import tensorflow as tf
import ssl

# required to prevent dataset download SSL error
ssl._create_default_https_context = ssl._create_unverified_context

# Sample code below is from:
# https://developer.apple.com/metal/tensorflow-plugin/
# (adapted to use the MobileNetV2 model)

cifar = tf.keras.datasets.cifar100
(x_train, y_train), (x_test, y_test) = cifar.load_data()

model = tf.keras.applications.MobileNetV2(
    input_shape=(32, 32, 3),
    alpha=1.0,
    include_top=True,
    weights=None,
    input_tensor=None,
    pooling=None,
    classes=100,
    classifier_activation="softmax",
    name=None,
)


loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64)