class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True


with HelloContextManager() as hello:
    print(hello)