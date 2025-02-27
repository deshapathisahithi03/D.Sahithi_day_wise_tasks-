class Logger:
    def __init__(self, message):
        self.message = message.lower()  # Normalize the message for consistent checks

    def log(self):
        if "error" in self.message:
            print(f"[ERROR] {self.message}")
        elif "warning" in self.message:
            print(f"[WARNING] {self.message}")
        elif "info" in self.message:
            print(f"[INFO] {self.message}")
        else:
            print(f"[LOG] {self.message}")  # Default case for general logs

# Example usage:
l1 = Logger("Error: System crash detected")
l1.log()

l2 = Logger("Warning: Disk space running low")
l2.log()

l3 = Logger("Info: User login successful")
l3.log()

l4 = Logger("Hello, this is a test log")
l4.log()
