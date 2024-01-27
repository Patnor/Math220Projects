

alphabeDict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 
               5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 
               10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 
               15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 
               20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 
               25: 'Z', 26: '.', 27: '?', 28: ' '}

# key to the cipher
key = [
    [1, 9],
    [6, 7]]


def keyInverse2x2(key):
    determinant = (key[0][0] * key[1][1]) - (key[0][1] * key[1][0])

    print('determinant = ' + str(determinant))
    if determinant == 0:
        return False
    else:
        inverse = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
        for i in range(len(inverse)):
            for j in range(len(inverse[0])):
                inverse[i][j] = inverse[i][j] * (1/ determinant)
        return inverse
    

def findKey(value, alphabeDict):
    for key, val in alphabeDict.items():
        if val == value:
            return key


# create the message matrix
# message is a string of characters
# alphabeDict is a dictionary of the alphabet         
def createMessageMatrix(message, alphabeDict):
    numCols = (len(message) + 1) // 2

    #set up the message matrix
    messageMatrix = [[None] * numCols, [None] * numCols]

    # first row of message matrix
    for i in range(0, numCols):
        messageMatrix[0][i] = findKey(message[i], alphabeDict)
    
    # second row of message matrix
    for i in range(0, numCols):
        # check if the message is odd and if so add a space at the end
        if(numCols + i >= len(message)):
            messageMatrix[1][i] = 28
        else:
            messageMatrix[1][i] = findKey(message[numCols + i ], alphabeDict) 

    return messageMatrix

# encrypt the message matrix
# messageMatrix is a 2xN matrix
# key is a 2x2 matrix
# returns a 2xN matrix
def encryptMessage(messageMatrix, key):
    #encrypt the messageMatrix by multiplying by the key
    encryptedMessageMatrix = [[None] * len(messageMatrix[0]), [None] * len(messageMatrix[0])]
    for i in range(0, len(messageMatrix[0])):
        for j in range(0, len(messageMatrix)):
            encryptedMessageMatrix[j][i] = (key[j][0] * messageMatrix[0][i]) + (key[j][1] * messageMatrix[1][i])
        
    return encryptedMessageMatrix

# decrypt the message matrix
# messageMatrix is a 2xN matrix
# keyI is a 2x2 matrix
# returns a 2xN matrix
def decryptMessage(messageMatrix, keyI):
#encrypt the messageMatrix by multiplying by the key
    decryptedMessageMatrix = [[None] * len(messageMatrix[0]), [None] * len(messageMatrix[0])]
    for i in range(0, len(messageMatrix[0])):
        for j in range(0, len(messageMatrix)):
            decryptedMessageMatrix[j][i] = (round(keyI[j][0] * messageMatrix[0][i])) + round((keyI[j][1] * messageMatrix[1][i]))
        
    return decryptedMessageMatrix

# the inverse matrix of the key
keyI = keyInverse2x2(key)
print("The inverse key is ")
print(keyI)

# create the message to encrypt
message = 'HELLO WORLD'
messageMatrix = createMessageMatrix(message, alphabeDict)
print(messageMatrix)

# encrypt the message
encryptedMessageMatrix = encryptMessage(messageMatrix, key)
print("The encryptedMessageMatrix is ")
print(encryptedMessageMatrix)

# decrypt the message
decryptedMessageMatrix = decryptMessage(encryptedMessageMatrix, keyI)
print("The decryptedMessageMatrix is ")
print(decryptedMessageMatrix)