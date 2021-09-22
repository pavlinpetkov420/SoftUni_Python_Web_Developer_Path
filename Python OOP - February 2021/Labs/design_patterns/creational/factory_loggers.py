from abc import ABC, abstractmethod
import os

class Logger(ABC):

    @abstractmethod
    def log(self, obj):
        pass


class FileLogger(Logger):

    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, obj):
        with open(self.file_path, 'a') as file:
            file.write(obj)
            file.write('\n')


class StdOutLogger(Logger):

    def log(self, obj):
        print(obj)


class LoggersFatory:

    def __init__(self):
        self.environment = os.environ.get('ENVIRONMENT', 'dev')
        self.logs_file_path = os.environ.get('LOGS_FILE_PATH', None)
        self.__init_logger()

    def get(self) -> Logger:
        return self.logger

    def __init_logger(self):
        if self.environment == 'prod':
            self.logger = FileLogger(self.logs_file_path)
        else:
            self.logger = StdOutLogger()



environment = ''  # prod, dev

loggers_factory = LoggersFatory()
loggers_factory2 = LoggersFatory()

print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())

# writes in a file
logger = loggers_factory.get()
logger.log("it's Allive!!!!")

# prints on stdout
logger = loggers_factory.get()
logger.log('Pickle Rick!')