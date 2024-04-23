import pycom

@pycom.command
def test(msg1: str, msg2, uppercase:bool=False, lowercase:bool=False):
    if uppercase:
        print(f"msg1: {str.upper(str(msg1))}")
        print(f"msg2: {str.upper(str(msg2))}")
    elif lowercase:
        print(f"msg1: {str.lower(str(msg1))}")
        print(f"msg2: {str.lower(str(msg2))}")
    else:
        print(f"msg1: {str(msg1)}")
        print(f"msg2: {str(msg2)}")

if __name__ == "__main__":
    pycom.start()