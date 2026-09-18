class data:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def display(self,data):
        print(f"The username is {self.username}")

obj=data("Penguin", "Penguin123")
obj.display("Penguin")
