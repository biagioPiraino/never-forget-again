from datetime import datetime
from Birthday import Birthday

class FileHandler:
    __path_prefix = "./Script/"

    def __init__(self) -> None:
        pass
    
    @classmethod
    def RetrieveAllQuotesFromFile(self) -> list:
        with open(file=f"{self.__path_prefix}quotes", mode="r", encoding="utf-8") as file:
            return file.readlines()

    @classmethod
    def RetrieveCredentialsFromFile(self) -> list:
        with open(file=f"{self.__path_prefix}credentials", mode="r", encoding="utf-8") as file:
            return file.readline().split(",")

    @classmethod
    def RetrieveAllBirthdaysFromFile(self) -> list:
        """
            This method will return a list containing all the
            scheduled Birthdays (class) by reading the info contained in the 
            'birthdays' file. Every birthday object will contain the name of
            the person, the date of his/her birthday and his/her email
        """
        all_birthdays = list()
        
        with open(file=f"{self.__path_prefix}birthdays", mode="r", encoding="utf-8") as file:
            all_lines = file.readlines()

            for line in all_lines:
                split_line  = line.split(',') # CSV format
                split_date  = split_line[1].split('-') # Split the date in DD-MM-YYYY
                
                birthday  = Birthday(
                    name  = split_line[0],
                    date  = datetime(
                        day   = int(split_date[0]), 
                        month = int(split_date[1]), 
                        year  = int(split_date[2])),
                    email = split_line[2])
                
                all_birthdays.append(birthday)
            
        return all_birthdays