class Logger:

    def __init__(self):
        self.messages_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message not in self.messages_dict:
            self.messages_dict[message] = timestamp
            return True
        
        if timestamp - self.messages_dict[message] >= 10:
            self.messages_dict[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)