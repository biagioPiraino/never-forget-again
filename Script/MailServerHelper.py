from FileHandler import FileHandler

class MailServerHelper:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def __define_provider(self, email: str) -> str:
        special_character = '@'
        ending_character = '.'
        if (special_character in email):
            return email.partition(special_character)[2].partition(ending_character)[0]
        
        return None

    @classmethod
    def DefineSMTPConnectionString(self, provider: str) -> str:
        if (provider == "gmail" or provider == "Gmail"):
            return "smtp.gmail.com"
        
        return None

    @classmethod
    def RetrieveCredentials(self) -> dict:
        """
            Credentials will be stored in a dictionary.
            The dictionary will contain three keys: "mail", "password", "provider"
        """
        file_handler = FileHandler()
        file_credentials = file_handler.RetrieveCredentialsFromFile()

        credentials = {
            "mail": file_credentials[0],
            "password": file_credentials[1],
            "provider": self.__define_provider(file_credentials[0]) 
        }

        return credentials