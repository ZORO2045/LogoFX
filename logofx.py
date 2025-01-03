import os
import sys
from art import text2art, FONT_NAMES
from colorama import init, Fore, Style
from typing import List
import re

# Initialize colorama
init(autoreset=True)


def remove_ansi_codes(text: str) -> str:
    """Removes ANSI escape codes from text."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


class LogoGenerator:
    """
    A class to generate text logos using various fonts and save them to a file.
    """
    def __init__(self):
        self.print_banner()
        self.name = self._get_user_input(Fore.YELLOW + "[ - ] Enter Your Name: ")
        self.file_name = self._get_valid_filename(Fore.YELLOW + "[ - ] Enter the output file name (e.g., logo.txt): ")
        print(Fore.CYAN + "_" * 75)
        self.generate_logos()
        print(Fore.CYAN + "_" * 75)

    def print_banner(self) -> None:
        """Displays the application banner with 'LogoFX' using the 'tarty1' font."""
        banner_text = text2art("LogoFX", font='tarty1')
        print(Fore.GREEN + banner_text)
        print(Fore.MAGENTA + "Developed by: ፚ Ꭷ Ꮢ Ꭷ ❥")
        print(Fore.CYAN + "_" * 75)

    def _get_user_input(self, prompt: str) -> str:
        """Gets user input and strips leading/trailing spaces."""
        while True:
          try:
            user_input = input(prompt).strip()
            if user_input:
              return user_input
            else:
              print(Fore.RED + "Input cannot be empty. Please try again.")
          except (KeyboardInterrupt):
            print("\n" + Fore.RED + "Operation cancelled by user.")
            sys.exit(0)

    def _get_valid_filename(self, prompt: str) -> str:
        """Gets a valid filename from the user."""
        while True:
          try:
              filename = self._get_user_input(prompt)
              if not filename:
                print(Fore.RED + "File name cannot be empty. Please try again.")
                continue
              
              if not filename.lower().endswith(('.txt', '.log')):
                filename += '.txt' 

              if os.path.exists(filename):
                  overwrite = self._get_user_input(Fore.YELLOW + f"File '{filename}' already exists. Overwrite? (y/n): ").lower()
                  if overwrite != 'y':
                    continue

              return filename
          except (KeyboardInterrupt):
            print("\n" + Fore.RED + "Operation cancelled by user.")
            sys.exit(0)

    def generate_logos(self) -> None:
        """Generates logos for all available fonts and saves them to a file."""
        plain_file_name = self.file_name.replace(".txt", "_plain.txt") if ".txt" in self.file_name else self.file_name + "_plain.txt"
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file, open(plain_file_name, 'w', encoding='utf-8') as plain_file:
                for font in FONT_NAMES:
                    try:
                        logo = text2art(self.name, font=font)
                        file.write(f"Font: {font}\n")
                        file.write(f"{logo}\n\n")
                        print(Fore.BLUE + f"Font: {font}")
                        print(Fore.GREEN + logo)
                        print(Fore.CYAN + "_" * 75)
                        
                        plain_logo = remove_ansi_codes(logo)
                        plain_file.write(f"Font: {font}\n")
                        plain_file.write(f"{plain_logo}\n\n")
                    except Exception as e:
                        print(Fore.RED + f"Error processing font '{font}': {type(e).__name__} - {str(e)}")
            print(Fore.GREEN + f"\nLogos have been successfully saved to '{self.file_name}' and '{plain_file_name}'.\n")
        except Exception as e:
            print(Fore.RED + f"An error occurred while writing to file: {type(e).__name__} - {str(e)}")

def main():
    """Main execution function."""
    while True:
      try:
          LogoGenerator()
          another = input(Fore.YELLOW + "Would you like to create another logo? (y/n): ").strip().lower()
          if another != 'y':
            print(Fore.MAGENTA + "Goodbye!")
            break
      except (KeyboardInterrupt):
        print("\n" + Fore.RED + "Operation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"Unexpected error occurred: {type(e).__name__} - {str(e)}")
        sys.exit(1)
