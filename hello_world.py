def hello_world():
    print("Hello World")

def greet(message, name="insert name here"):
    print(message, " ", name)
#Comment this code out and see what happens!
if __name__ == "__main__":
    hello_world()
    name = "Derp"
    message = "Good morning"
    greet(message, name)
    #greet(name=name, message=message)
    #greet(message="message")
