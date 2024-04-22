import pycom

@pycom.command
def test(msg1, msg2):
    print(f"msg1: {msg1}")
    print(f"msg2: {msg2}")

if __name__ == "__main__":
    pycom.start()