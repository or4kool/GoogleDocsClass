class Document:
	def __init__(self, title, content):
		self.title=title
		self.content=content

	def rename_doc(self, title):
		self.title=title
		return self.title

	def add_content(self):
		self.0content = open(self.title,"w")
		# self.content.append(content)

	def read_content(self):
		# self.content=content
		# for content in self.content:
		self.existing_doc= open(self.title,"r")
		print(self.existing_doc)

	def share_doc(self, email_address):
		pass

	def save_file(self, file_name):
		pass



		#import smtplib

		#host =
		#port =
		#username =
		#password =


Zazipitch = Document("Zazimed", "market research validation")
print(Zazipitch.title)

print(Zazipitch.rename_doc("Zazi-meder"))

Zazipitch.add_content()

Zazipitch.read_content()







