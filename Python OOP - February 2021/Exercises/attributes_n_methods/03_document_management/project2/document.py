from project2.category import Category
from project2.topic import Topic


class Document:

    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        """4 attributes upon initialization:
            id, category_id, topic_id, file_name
        1 class attribute:
            tags - empty list"""
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    def __repr__(self):
        """make a string representation
        :return: "Document {id}: {file_name}; category {category_id},
         topic {topic_id}, tags: {tags joined by comma and space)}" """
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}," \
               f" tags: {', '.join([str(t) for t in self.tags])}"

    def kill(self):
        del self

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        """create new instance with following parameters
        :param id: instance id
        :param category: instance -> we use its id
        :param topic:  instance -> we use its id
        :param file_name: instance file_name
        :return: new instance cls"""
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        """add new tag if it is NOT already in the list
            :param tag_content:  new possible tag
            :return: updated tags list"""
        filtered_tags = []
        if self.tags:
            filtered_tags = [t for t in self.tags if t == tag_content][0]
        if not filtered_tags:
            return self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        """remove tag if it is in the list
            :param tag_content:  tag to remove
            :return: updated tags list"""
        if self.tags:
            filtered_tags = [t for t in self.tags if t == tag_content][0]
            if filtered_tags:
                return self.tags.remove(tag_content)

    def edit(self, file_name: str):
        """change the file name
        :param file_name: str -> new file name
        :return: changed file name"""
        self.__setattr__('file_name', file_name)

