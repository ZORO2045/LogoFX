try:
    from art import *
    from art import FONT_NAMES as all_fonts
    from colorama import init, Fore, Style
except ImportError as e:
    print(f"Error: {type(e).__name__} - {str(e)}")
    print("Please ensure that the necessary modules are installed.")
    exit(1)

init(autoreset=True)

class ALEX:
    def __init__(self):
        self.display_banner()
        self.name = input(Fore.YELLOW + "[ - ] Enter Your Name : ")
        self.file_name = input(Fore.YELLOW + "[ - ] Enter the output file name (e.g., Logo.txt): ")
        print(Fore.CYAN + "_" * 65)
        self.generate_logos(self.name, self.file_name)
        print(Fore.CYAN + "_" * 65)

    def display_banner(self):
        banner_text = text2art("LogoFX", font='block')
        print(Fore.GREEN + banner_text)
        print(Fore.MAGENTA + "Developed by: ፚ Ꭷ Ꮢ Ꭷ ❥")
        print(Fore.CYAN + "_" * 65)

    def generate_logos(self, text, file_name):
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for font in all_fonts:
                    logo = text2art(text, font=font)
                    file.write(f"Font: {font}\n")
                    file.write(f"{logo}\n\n")
                    print(Fore.BLUE + f"Font: {font}")
                    print(Fore.GREEN + logo)
                    print(Fore.CYAN + "_" * 65)
            print(Fore.GREEN + f"\nLogos have been successfully saved to {file_name}.\n")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {type(e).__name__} - {str(e)}")
    
if __name__ == "__main__":
    while True:
        end = ALEX()
        another = input(Fore.YELLOW + "Would you like to create another logo? (y/n): ").strip().lower()
        if another != 'y':
            print(Fore.MAGENTA + "Goodbye!")
            break
