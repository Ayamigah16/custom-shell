import os
import difflib

# data structure to store command history
command_history = []

# some shell commands
example_commands = ['ls', 'cd', 'mkdir', 'rm', 'touch', 'cat', 'python', 'exit']

def execute_command(command):
    """
    Allows user to execute commands

    Args:
        command (str): command to excute

    Return:
        None
    """
    try:
        output = os.popen(command).read()
    except Exception as e:
        print(f"An error occured: {str(e)}")

def suggestion_comands(partial_command):
    """
    Sugeest commands based on the partial command.

    Args:
        partial_command (str): the partial command entered
    
    Return:
        list: a list of suggested commands
    """
    suggestions = difflib.get_close_matches(partial_command, example_commands)
    return suggestions


def main():
    while True:
        user_input = input("custom-shell: ")
        if user_input.lower() == "exit":
            break

        # commands stack
        command_history.append(user_input)

        # display command history per "history" command
        if user_input.lower() == "history":
            print("Command History: ")
            for idx, cmd in enumerate(command_history, start=1):
                print(f"{idx}, {cmd}")
        
        # execute commands
        else:
            suggestions = suggestion_comands(user_input)
            if suggestions:
                print("Suggestions: ")
                for suggestion in suggestions:
                    print(suggestion)
            else:
                execute_command(user_input)

if __name__ == "__main__":
    main()