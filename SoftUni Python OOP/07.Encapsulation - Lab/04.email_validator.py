class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains

    def validate(self, email: str):
        name, info = email.split('@')
        mail, domain = info.split('.')

        if self.__is_name_valid(name) and self.__is_domain_valid(domain) and self.__is_mail_valid(mail):
            return True
        return False

# https://github.com/ZahariBakov/SoftUni-Python/blob/main/Python%20OOP/Encapsulation%20-%20Lab/03_profile.py

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))