from lib import *

# Algoritmos 
test_md4 = MD4()
test_md5 = MD5()
test_sha1 = SHA1() 
test_sha256 = SHA256()

# Menú principal en TKinter 
message: str = ""
key: str = ""

def getInput() -> None:
  global message
  message = input(str("TEXTO: "))

def getKey() -> None:
  global key
  key = input(str("KEY: "))

def readDataFromFile() -> None:
  global message
  with open('input.txt', 'r') as f:
    message = f.read()

def writeDataToFile(message: str) -> None:
  with open('output.txt', 'w') as f:
    f.write(message)

mainScreen()
state: bool = True
while state is True: 
  option: int = input("Ingrese el número de la opción que desea: ")
  state = False if option == "6" else True 
  match option:
    case '1': 
      getInput()
      print(test_md4.hash_digest(getBytes(message)))
      
    case '2':
      getInput()
      print(test_md5.hash_digest(getBytes(message)))

    case '3':
      getInput()
      print(test_sha1.hash_digest(getBytes(message)))
    
    case '4':
      getInput()
      print(test_sha256.hash_digest(getBytes(message)))

    case '5':
      getInput()
      getKey()
      print(hmac(getBytes(key), getBytes(message), hashlib.sha256).hex())
