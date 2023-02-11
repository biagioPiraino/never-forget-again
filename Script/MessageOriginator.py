import random

class MessageOriginator:
    __single_line = '\n'
    __double_line = "\n\n" 

    def __init__(self) -> None:
        pass
    
    @classmethod
    def __retrieve_initial_part(self, recipient_name: str) -> str:
        return f"Hey {recipient_name.capitalize()},{self.__double_line}"

    @classmethod
    def __retrieve_random_quote(self) -> str:
        with open(file="quotes", mode="r", encoding="utf-8") as file:
            quotes = file.readlines()
            quote = random.choice(quotes) 
            return f"{quote}{self.__single_line}"

    @classmethod
    def __retrieve_ending(self, sender_name: str) -> str:
        ending_message = "Lots of love,\n"
        return f"{ending_message}{sender_name.capitalize()}"

    @classmethod
    def GenerateMessage(self, sender_name: str, recipient_name: str) -> str:
        """
            The email will have three parts: 
                1) an opening greeting message that will contain the recipient's name
                2) a random quote retrieved from a file
                3) an ending greeting message that will contain the sender's name
        """
        initial_part = self.__retrieve_initial_part(recipient_name=recipient_name)
        quote = self.__retrieve_random_quote()
        ending = self.__retrieve_ending(sender_name=sender_name)
        return f"{initial_part}{quote}{ending}"           