import pycom

@pycom.command
def test(msg1, msg2, uppercase=False, lowercase=False):
    if uppercase:
        print(f"msg1: {str.upper(msg1)}")
        print(f"msg2: {str.upper(msg2)}")
    if lowercase:
        print(f"msg1: {str.lower(msg1)}")
        print(f"msg2: {str.lower(msg2)}")
    else:
        print(f"msg1: {msg1}")
        print(f"msg2: {msg2}")

if __name__ == "__main__":
    pycom.start()