import os

command_history = []

def execute_command(command):
    """Allows user to execute commands

    Args:
        command (str): command to excute
    """
    try:
        output = os.popen().read()
    except Exception as e:
        print(f"An error occured: {str(e)}")

def main():
    while True:
        user_input = input("Command: ")
        if user_input.lower() == "exit":
            break

        command_history.append(user_input)

        if user_input.lower() == "history":
            print("Command History: ")
            for idx, cmd in enumerate(command_history, start=1):
                print(f"{idx}, {cmd}")
        else:
            execute_command(user_input)


if __name__ == "__main__":
    main()