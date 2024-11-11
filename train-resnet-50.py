import tensorflow as tf
import ssl

# check that tensorflow has a GPU available
gpu_devices = tf.config.experimental.list_physical_devices('GPU')
if len(gpu_devices) > 0:
    print('GPUs:')
    for device in gpu_devices:
        print(tf.config.experimental.get_device_details(device))
else:
    print('No GPUs available')

# required to prevent dataset download SSL error
ssl._create_default_https_context = ssl._create_unverified_context

# Sample code below is from:
# https://developer.apple.com/metal/tensorflow-plugin/

cifar = tf.keras.datasets.cifar100
(x_train, y_train), (x_test, y_test) = cifar.load_data()
model = tf.keras.applications.ResNet50(
    include_top=True,
    weights=None,
    input_shape=(32, 32, 3),
    classes=100,)

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])
model.fit(x_train, y_train, epochs=5, batch_size=64)