import os
import difflib

class CommandPrompt:
    """
    A simple object-oriented command prompt with customization and suggestion features.

    Attributes:
        command_history (list): A list to store the command history.
        prompt_prefix (str): The prefix for the command prompt.
        prompt_color (str): The color for the command prompt.
        example_commands (list): A list of example commands for suggestion.
    """

    def __init__(self):
        """
        Initialize the CommandPrompt instance.
        """
        self.command_history = []
        self.prompt_prefix = "CustomPrompt"
        self.prompt_color = "\033[1;32m"  # Default color: green
        self.example_commands = ['ls', 'cd', 'mkdir', 'rm', 'touch', 'cat', 'python', 'exit']

    def execute_command(self, command):
        """
        Execute the given command using os.popen and print the output.
        
        Args:
            command (str): The command to execute.

        Returns:
            None
        """
        try:
            output = os.popen(command).read()
            print(output)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def suggest_commands(self, partial_command):
        """
        Suggest commands or options based on the partial command.

        Args:
            partial_command (str): The partial command entered by the user.

        Returns:
            list: A list of suggested commands or options.
        """
        suggestions = difflib.get_close_matches(partial_command, self.example_commands)
        return suggestions

    def customize_prompt(self):
        """
        Allow the user to customize the prompt format and color.

        Returns:
            None
        """
        self.prompt_prefix = input("Enter custom prompt prefix: ")
        self.prompt_color = input("Enter custom prompt color (e.g., \033[1;32m for green): ")

    def display_help(self):
        """
        Display help and documentation for available commands.

        Returns:
            None
        """
        print("Available Commands:")
        for cmd in self.example_commands:
            print(cmd)

    def run(self):
        """
        Run the command prompt, taking user input and executing commands.

        Returns:
            None
        """
        while True:
            user_input = input(f"{self.prompt_color}{self.prompt_prefix}> \033[0m")
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'customize':
                self.customize_prompt()
            elif user_input.lower() == 'help':
                self.display_help()
            elif user_input.lower() == 'history':
                print("Command History:")
                for idx, cmd in enumerate(self.command_history, start=1):
                    print(f"{idx}. {cmd}")
            else:
                self.command_history.append(user_input)
                suggestions = self.suggest_commands(user_input)
                if suggestions:
                    print("Suggestions:")
                    for suggestion in suggestions:
                        print(suggestion)
                else:
                    self.execute_command(user_input)

if __name__ == "__main__":
    command_prompt = CommandPrompt()
    command_prompt.run()
