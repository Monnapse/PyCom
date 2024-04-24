import pycom

@pycom.command
def test(msg1:str, msg2: str="HELLO WORLD", msg3:str = "WHAT", uppercase:bool=False, lowercase:bool=False):
    if uppercase:
        print(f"msg1: {str.upper(str(msg1))}")
        print(f"msg2: {str.upper(str(msg2))}")
        print(f"msg3: {str.upper(str(msg3))}")
    elif lowercase:
        print(f"msg1: {str.lower(str(msg1))}")
        print(f"msg2: {str.lower(str(msg2))}")
        print(f"msg3: {str.lower(str(msg3))}")
    else:
        print(f"msg1: {str(msg1)}")
        print(f"msg2: {str(msg2)}")
        print(f"msg3: {str(msg3)}")

if __name__ == "__main__":
    pycom.start()