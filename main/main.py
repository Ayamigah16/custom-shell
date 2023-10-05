import os

while True:
    user_input = input("Command: ")
    if user_input.lower() == "exit":
        break

    try:
        os.system(user_input)
    except Exception as e:
        print(f"An error occured: {str(e)}")
