class Topic:
    """
    class Topic with 3 attributes upon initialization - id, topic, storage_folder
    2 methods:
        edit - change topic and storage folders
        repr - return string repr in following format: "Topic {self.id}: {topic} in {storage_folder}"
    """

    def __init__(self, id: int, topic: str, storage_folder: str):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"

    def kill(self):
        del self

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder
