import re


class EmailValidator:
    
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    @staticmethod
    def split_email(email):
        pattern = r"(?P<username>[A-Za-z0-9]+)@(?P<mail>[a-z]+)\.(?P<domain>[a-z]+)"
        match = re.findall(pattern, email)
        for res in match:
            return res

    def __validate_name(self, name):
        name_length = len(name)
        return name_length >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        username, mail, domain = self.split_email(email)
        if self.__validate_name(username):
            if self.__validate_mail(mail):
                if self.__validate_domain(domain):
                    return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
