from project2.topic import Topic
from project2.category import Category
from project2.document import Document


class Storage:

    def __init__(self):
        """
        no parameters upon initialization
        3 class attributes:
            categories, topics, documents -> empty lists
        """
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        """
        :return: string repr of each document on a new line
        """
        result = ""
        for d in self.documents:
            result += f"{repr(d)}\n"
        return result

    def __del__(self):
        return

    def get_category_instance(self, c_id):
        """
        get instance of class category by id
        :param c_id:
        :return: instance name
        """
        return [_ for _ in self.categories if _.last_id == c_id][0]

    def get_topic_instance(self, t_id):
        """
        get instance of class topic by id
        :param t_id:
        :return: instance name
        """
        return [_ for _ in self.topics if _.last_id == t_id][0]

    def get_document_instance(self, d_id):
        """
        get instance of class Document by id
        :param d_id:
        :return: instance name
        """
        return [_ for _ in self.documents if _.last_id == d_id][0]

    def is_existing(self, instance):
        """
        check is this instance in the list
        :param instance: instance of class
        :return: bool
        """
        if isinstance(instance, Category):
            if instance in self.categories:
                return True
            return False
        elif isinstance(instance, Topic):
            if instance in self.topics:
                return True
            return False
        elif isinstance(instance, Document):
            if instance in self.documents:
                return True
            return False

    def add_category(self, category: Category):
        """if current instance doesn't exist in the list append it
        :param category: instance of Category
        :return: updated list"""
        if not self.is_existing(category):
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        """if current instance doesn't exist in the list append it
        :param topic: instance of Topics
        :return: updated list"""
        if not self.is_existing(topic):
            self.topics.append(topic)

    def add_document(self, document: Document):
        """if current instance doesn't exist in the list append it
        :param document: instance of Documents
        :return: updated list"""
        if not self.is_existing(document):
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        """by id find a category instance and change its name
        :param category_id: int
        :param new_name: str
        :return: updated attribute"""
        cat_instance = self.get_category_instance(category_id)
        if cat_instance:
            cat_instance.__setattr__('name', new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        """find the topic instance by id, change the topic_name and the storage folder
        :param topic_id: int
        :param new_topic: str
        :param new_storage_folder: str
        :return: update id and storage folder"""
        topic_instance = self.get_topic_instance(topic_id)
        if topic_instance:
            topic_instance.__setattr__('topic', new_topic)
            topic_instance.__setattr__('storage_folder', new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        """find document instance by id -> change file name with new
        :param document_id: int
        :param new_file_name: str
        :return: update instance file name"""
        document_instance = self.get_document_instance(document_id)
        if document_instance:
            document_instance.edit(new_file_name)

    def delete_category(self, category_id):
        """Find the instance by id and delete it
        :param category_id:
        :return: delete instance"""
        category = self.get_category_instance(category_id)
        if category:
            category.kill()
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        """
        find instance in class Topic and delete it
        :param topic_id:
        :return:
        """
        topic = self.get_topic_instance(topic_id)
        if topic:
            topic.kill()
            self.topics.remove(topic)

    def delete_document(self, document_id):
        """find instance of class Documents and delete it
        :param document_id:
        :return:"""
        document_instance = self.get_document_instance(document_id)
        if document_instance:
            document_instance.kill()
            self.documents.remove(document_instance)

    def get_document(self, document_id):
        """find document instance by id and return it as a result
        :param document_id:
        :return: document repr"""
        document = self.get_document_instance(document_id)
        if document:
            return repr(document)


# c = Category(1, "C")
# t = Topic(1, "T", "C:\\user")
# d = Document(1, 1, 1, "D")
# s = Storage()
#
# s.add_document(d)
# s.edit_document(1, "new")
# print(s.documents[0].file_name)



