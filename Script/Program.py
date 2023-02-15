from BirthdayRetriever import BirthdayRetriever
from Birthday import Birthday
from MessageOriginator import MessageOriginator
from MailServer import MailServer

class Program: 
    def __init__(self) -> None:
        pass

    @classmethod
    def ProcessBirthdays(self) -> None:
        """
            The process can be broken down in the following logical steps:
                1) Retrieve the birhtdays to process
                2) For every birthday we generate a random message...
                3) ...and than send an email to them.
        """
        sender_name = "sender" # Specify your name
        birthday_retriever = BirthdayRetriever()
        birthday_to_process: list(Birthday) = birthday_retriever.RetrieveTodayBirthdays()

        for birthday in birthday_to_process:
            msg_originator = MessageOriginator()
            msg = msg_originator.GenerateMessage(sender_name=sender_name, recipient_name=birthday.name, dob=birthday.date)
            mail_server = MailServer()
            mail_server.SendEmail(message=msg, recipient=birthday.email)