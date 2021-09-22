class EmailValidator:

	def __init__(self, min_lenght: int, mails: list, domains: list):
		self.min_lenght = min_lenght
		self.mails = mails
		self.domains = domains

	def __validate_name(self, name):

		if len(name) < self.min_lenght:
			return False
		return True

	def __validate_mail(self, mail):
		if mail not in self.mails:
			return False
		return True

	def __validate_domain(self, domain):
		if domain not in self.domains:
			return False
		return True

	def validate(self, email):
		name, mail_n_domain = email.split('@')
		mail, domain = mail_n_domain.split('.')
		if self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain):
			return True

		return False



mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))


