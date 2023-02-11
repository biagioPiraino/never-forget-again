from datetime import datetime
from FileHandler import FileHandler

class BirthdayRetriever:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def RetrieveTodayBirthdays(self) -> list:
        # Retrieve all the birthdays from the file
        file_handler = FileHandler()
        scheduled_birthdays = file_handler.RetrieveAllBirthdays()

        today = datetime.today()
        todays_birthdays = list()

        # Filter to get today's birthdays
        for birthday in scheduled_birthdays:
            if (birthday.date.day   == today.day and
                birthday.date.month == today.month):
                todays_birthdays.append(birthday)
        
        return todays_birthdays