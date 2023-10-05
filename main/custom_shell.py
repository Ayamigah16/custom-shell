import os
import difflib

# data structure to store command history
command_history = []

# customization contents --> color
prompt_prefix = "custom-prompt"
prompt_color = "\033[1;32m" #default color: green


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

def customize_prompt():
    """
    Allow the user to customize the prompt format and color.

    Returns:
        None
    """
    global prompt_prefix, prompt_color
    prompt_prefix = input("Enter custom prompt prefix: ")
    prompt_color = input("Enter custom prompt color (e.g., \033[1;32m for green): ")

def display_help():
    """
    Display help and documentation for available commands.

    Returns:
        None
    """
    print("Available Commands:")
    for cmd in example_commands:
        print(cmd)

def main():
    while True:
        user_input = input(f"{prompt_color}{prompt_prefix}> \033[0m")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'customize':
            customize_prompt()
        elif user_input.lower() == 'help':
            display_help()
        elif user_input.lower() == 'history':
            print("Command History:")
            for idx, cmd in enumerate(command_history, start=1):
                print(f"{idx}. {cmd}")

        # commands stack
        command_history.append(user_input)

        # display command history per "history" command
        if user_input.lower() == "history":
            print("Command History: ")
            for idx, cmd in enumerate(command_history, start=1):
                print(f"{idx}, {cmd}")
        
        # execute commands
        else:
            # suggestions = suggestion_comands(user_input)
            # if suggestions:
            #     print("Suggestions: ")
            #     for suggestion in suggestions:
            #         print(suggestion)
            # else:
            execute_command(user_input)

if __name__ == "__main__":
    main()