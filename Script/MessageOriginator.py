import random
from FileHandler import FileHandler

class MessageOriginator:
    __single_line = '\n'
    __double_line = "\n\n" 

    def __init__(self) -> None:
        pass
    
    @classmethod
    def __retrieve_subject(self, recipient_age: int) -> str:
        return f"Subject:They are {recipient_age}!{self.__double_line}"

    @classmethod
    def __retrieve_initial_part(self, recipient_name: str) -> str:
        return f"Hey {recipient_name.capitalize()},{self.__double_line}"

    @classmethod
    def __retrieve_random_quote(self) -> str:
        file_handler = FileHandler()
        all_quotes = file_handler.RetrieveAllQuotesFromFile()
        return f"{random.choice(all_quotes)}{self.__single_line}"

    @classmethod
    def __retrieve_ending(self, sender_name: str) -> str:
        ending_message = "Lots of love,\n"
        return f"{ending_message}{sender_name.capitalize()}"

    @classmethod
    def GenerateMessage(self, sender_name: str, recipient_name: str, recipient_age: int) -> str:
        """
            The email will have three parts: 
                1) an opening greeting message that will contain the recipient's name
                2) a random quote retrieved from a file
                3) an ending greeting message that will contain the sender's name
            The email will have a subject that contains the recipient age
        """
        subject = self.__retrieve_subject(recipient_age=recipient_age)
        initial_part = self.__retrieve_initial_part(recipient_name=recipient_name)
        quote = self.__retrieve_random_quote()
        ending = self.__retrieve_ending(sender_name=sender_name)
        return f"{subject}{initial_part}{quote}{ending}"