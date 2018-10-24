def hello_world():
    print("Hello World")

def greet(message, name="insert name here"): #default value is "insert name here"
    print(message, " ", name)
#Comment this code out and see what happens!

if __name__ == "__main__":	#if not running this file directly, then this portion of code does not appear 
    hello_world()
    name = "Derp"
    message = "Good morning"
    greet(message, name)
    #greet(name=name, message=message)
    greet(message="message") #overwrite the message in line 11

