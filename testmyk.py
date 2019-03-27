import datetime,random
from datetime import date

class villa(object):
    vilResIdList=[]
    def __init__(self,n,id):
        self.vilResIdList.append(id)
        self.villaName=n
    def setPersonalAssistant(self,pa):
        self.personalAssistant=pa
        print(f"{pa} will be on call from 8.00am to 8.00pm")
    def cleanAndChangeKey(self,d1,d2):
        print(f"The villa will be cleaned and keys will be changed on {d1} and {d2}")
    def printGiftLabel(self,s):
        print(f"Welcome to the Myconos Hidden Cove, {s} party!")
