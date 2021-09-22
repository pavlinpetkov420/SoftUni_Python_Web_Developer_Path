class Smartphone:

    def __init__(self, memory: int):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        # if self.is_on:
        #     self.is_on = False
        # else:
        #     self.is_on = True
        self.is_on = not self.is_on

    def memory_left(self):
        return self.memory - self.memory_taken

    def install(self, app, app_memory):
        is_memory_enough = self.memory_left() >= app_memory
        if not is_memory_enough:
            return f"Not enough memory to install {app}"
        elif is_memory_enough and not self.is_on:
            return f"Turn on your phone to install {app}"
        self.apps.append(app)
        self.memory_taken += app_memory
        return f"Installing {app}"

    def status(self):
        total_apps = len(self.apps)
        memory_left = self.memory_left()
        return f"Total apps: {total_apps}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
