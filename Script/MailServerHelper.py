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
    def RetrieveCredentials(self) -> dict:
        """
            Credentials will be stored in a dictionary.
            The dictionary will contain three keys: "mail", "password", "provider"
        """
        credentials = {
            "mail": "",
            "password": "",
            "provider": "" 
        }

        # Credentials will be retrieved from a raw text file
        with open(file="credentials", mode="r", encoding="utf-8") as file:
            split_line = file.readline().split(",")
            credentials["mail"] = split_line[0]
            credentials["password"] = split_line[1]
            credentials["provider"] = self.__define_provider(split_line[0])
        
        return credentials