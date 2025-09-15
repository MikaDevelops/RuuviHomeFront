import hashlib
from datetime import datetime
import random

class AccessController:
    def __init__(self, passing_word):
        self.passing_word = passing_word
        self.givenToken = None

    def pwOk(self):
        with open("start.txt") as startFile:
            fileContent = startFile.read()
            passingWordByte = self.passing_word.encode()
            hashHex = hashlib.sha256(passingWordByte).hexdigest()
            if fileContent == hashHex:
                return True
            else:
                return False
            
    def checkMainUserPassword(self, password):
        with open("accesslist.txt") as accList: 
            accContent = accList.read() 
            passwordByte = password.encode()
            pwHex = hashlib.sha256(passwordByte).hexdigest()
            if accContent == pwHex:
                return True
            else:
                return False 
            
    def giveNewToken(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        chosenLetters = random.choices(letters, k=4)
        textPart = "".join(chosenLetters)
        dateTimeNum = str(int(datetime.timestamp(datetime.now())))
        token = textPart + dateTimeNum
        validUntil = int(datetime.timestamp(datetime.now())) + 3600
        self.givenToken = {
            "token": token,
            "validUntil": validUntil
        }
        return token
    
    def renewToken(self, token):
        if self.checkToken(token):
            newToken = self.giveNewToken()
            return newToken
        else:
            return False
        
    def checkToken(self, token):
        if self.givenToken == None:
            return False
        timeNow = int(datetime.timestamp(datetime.now()))
        if timeNow > self.givenToken['validUntil']:
            return False
        if token == self.givenToken['token']:
            return True
        else:
            return False
    # load secret to memory
    # create new secret
    # check given secret