import socket
import base64
import pickle
import getpass

# create a socket object
def pickler(data, flag=0):
    if flag == 0:
        return pickle.dumps(data)
    elif flag == 1:
        return pickle.loads(data)

def encoder(data, flag=0):
    if flag == 0:
        # return pickler(base64.encodestring(pickler(data)).strip())
        return pickler(base64.encodebytes(pickler(data)).strip())
    elif flag == 1:
        # return pickler(base64.decodestring(pickler(data, flag=1)), flag=1)
        return pickler(base64.decodebytes(pickler(data, flag=1)), flag=1)


def get_credential():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter password: ")
    token= encoder('{}:{}'.format(username, password))
    return username, token


def authenticator(host='192.168.5.37', port=5555):
    username, token = get_credential()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("connected to {}:{}".format(host, port))
    s.sendall(token)
    data = s.recv(2048)
    data = encoder(data, flag=1)
    if data == "invalid credential":
        print("Invalid credential.. try again")
        s.close()
        return False
    else:
        print("Welcome, {}".format(username))
        print(data)
        return True
        # s.close()

if __name__ == "__main__":
    result = authenticator()
    if not result:
        choice = input("Do you want to try again? (y/n)")
        if choice.lower() == "y":
            result = authenticator()
            if not result:
                print("Better luck next time..")
        else:
            print("bye...")
