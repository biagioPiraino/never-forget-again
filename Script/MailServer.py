import smtplib as smt
from MailServerHelper import MailServerHelper

class MailServer():
    def __init__(self) -> None:
        pass

    @classmethod
    def SendEmail(self, message: str, recipient: str) -> None:
        try:
            with self.__connect() as connection:
                connection.sendmail(
                    from_addr=connection.user, to_addrs=recipient, msg=message)
        except (smt.SMTPHeloError, smt.SMTPAuthenticationError,
                smt.SMTPConnectError, smt.SMTPException) as error:
            print(error)

    @classmethod
    def __connect(self) -> smt.SMTP:
        # Retrieve sender credentials
        helper = MailServerHelper()
        sender_credentials = helper.RetrieveCredentials()
        # Connect the user to the mail server
        smtp_connection_string = helper.DefineSMTPConnectionString(provider=sender_credentials["provider"])
        smtp_connection = smt.SMTP(smtp_connection_string)
        # Start encryption in-flight (TLS)
        smtp_connection.starttls()
        # Login user
        smtp_connection.login(user=sender_credentials["mail"], password=sender_credentials["password"])
        # Return the connection
        return smtp_connection