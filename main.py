from tensorflow.python.client import device_lib


def print_hi(name):
    print(device_lib.list_local_devices())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
