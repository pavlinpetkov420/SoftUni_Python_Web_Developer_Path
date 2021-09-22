from problem_solving_2.document_management.project.category import Category
from problem_solving_2.document_management.project.topic import Topic
from problem_solving_2.document_management.project.document import Document


class Storage:

	def __init__(self):
		self.categories = []
		self.topics = []
		self.documents = []

	def __repr__(self):
		return '\n'.join([repr(doc) for doc in self.documents])

	def get_attribute_instance(self, id, key):
		attribute_mapper = {
			'categories': self.categories,
			'topics': self.topics,
			'documents': self.documents
		}
		work_list = attribute_mapper[key]
		for el in work_list:
			if el.id == id:
				return el

	def add_category(self, category: Category):
		if category not in self.categories:
			self.categories.append(category)

	def add_topic(self, topic: Topic):
		if topic not in self.topics:
			self.topics.append(topic)

	def add_document(self, document: Document):
		if document not in self.documents:
			self.documents.append(document)

	def edit_category(self, category_id: int, new_name: str):
		category = self.get_attribute_instance(category_id, 'categories')
		if category:
			category.name = new_name

	def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
		topic = self.get_attribute_instance(topic_id, 'topics')
		if topic:
			topic.name = new_topic
			topic.storage_folder = new_storage_folder

	def edit_document(self, document_id: int, new_file_name: str):
		document = self.get_attribute_instance(document_id, 'documents')
		if document:
			document.file_name = new_file_name

	def delete_category(self, category_id: int):
		category = self.get_attribute_instance(category_id, 'categories')
		if category:
			self.categories.remove(category)

	def delete_topic(self, topics_id: int):
		topic = self.get_attribute_instance(topics_id, 'topics')
		if topic:
			self.topics.remove(topic)

	def delete_document(self, document_id: int):
		document = self.get_attribute_instance(document_id, 'documents')
		if document:
			self.documents.remove(document)

	def get_document(self, document_id):
		document = self.get_attribute_instance(document_id, 'documents')
		if document:
			return document
