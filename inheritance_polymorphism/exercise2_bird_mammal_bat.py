class Bird:
    def fly(self):
        """Method for flying behavior."""
        print("Flying...")

class Mammal:
    def run(self):
        """Method for running behavior."""
        print("Running...")

class Bat(Bird, Mammal):
    def fly(self):
        """Override fly method for Bat."""
        print("Bat is flying.")

    def run(self):
        """Override run method for Bat."""
        print("Bat is running.")

# Test the Bat class
if __name__ == "__main__":
    bat = Bat()
    bat.fly()
    bat.run()
