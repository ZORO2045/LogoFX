# LogoFX - Text Logo Generator 🚀

![LogoFX](banner.png)

[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=flat-square&logo=python)](https://www.python.org/)

## Description 📝

LogoFX is a Python script that generates text logos using a variety of fonts and saves them to a file. It leverages the `art` library to create visually appealing text art and `colorama` to add color to the output. This script is designed to be simple and user-friendly, allowing you to create logos quickly for various purposes.

## Features ✨

-   **Multiple Fonts 🔤:** Generates logos using all available fonts in the `art` library.
-   **Colored Output 🎨:** Uses `colorama` to add colors to the text output in the console.
-   **Plain Text Output 📄:** Generates a plain text version of the logos without ANSI escape codes for use in environments that don't support colored output.
-   **User-Friendly Input 🙋‍♂️:** Prompts the user for a name and output filename.
-   **Error Handling ✅:** Includes robust error handling to ensure smooth execution.
-   **Interactive 🔄:** Allows for the creation of multiple logos in a single session.
-   **Custom Banner 🖼️:** Displays a custom banner using the `tarty1` font.

## Installation ⚙️

1.  Make sure you have Python installed on your system (Python 3.6+ is recommended).

2.  Clone the repository:

    ```bash
    git clone https://github.com/ZORO2045/LogoFX.git
    ```

3.  Navigate to the project directory:

    ```bash
    cd LogoFX
    ```

4.  Install the required Python packages:

    ```bash
    pip install art colorama
    ```

## Usage 💻

1.  Run the script:

    ```bash
    python logofx.py
    ```

2.  Follow the prompts:

    -   Enter your name when prompted.
    -   Enter the desired output file name (e.g., `logo.txt`). The script will generate two files: one with colors and another with plain text (`_plain.txt`).

3.  The script will display each generated logo in the console and save it to the specified file.

4.  You can create multiple logos in one session by answering 'y' when asked if you want to create another logo.

## Example Output 💡

Here's a sample output of the colored logo:

```bash
Font: font1
[34m  __    __  ______  _    _  _____ [0m
[32m |  \  /  ||  ____|| |  | ||  ___| [0m
[32m |   \/   || |____ | |  | || |__ [0m
[32m | |\  /| ||  ____|| |  | ||  __| [0m
[32m | | \/ | || |     | |__| || |___ [0m
[32m |_|    |_||_|      \____/ ||_____| [0m

Font: font2
[34m  ________  __   __  _______   ____ [0m
[32m /        ||  \ |  ||       | /    \[0m
[32m|  ______ ||   \|  ||  _____||  __  \[0m
[32m| |_____  ||  |\   || |_____ | |  |  |[0m
[32m|  _______||  | \  ||  ____ ||  --  /[0m
[32m \________||__|  \__||_______|\____/[0m
```
## Example Output 💡

Here's a sample output from the plain text file:

```text
Font: font1
  __    __  ______  _    _  _____
 |  \  /  ||  ____|| |  | ||  ___|
 |   \/   || |____ | |  | || |__
 | |\  /| ||  ____|| |  | ||  __|
 | | \/ | || |     | |__| || |___
 |_|    |_||_|      \____/ ||_____|

Font: font2
  ________  __   __  _______   ____
 /        ||  \ |  ||       | /    \
|  ______ ||   \|  ||  _____||  __  \
| |_____  ||  |\   || |_____ | |  |  |
|  _______||  | \  ||  ____ ||  --  /
 \________||__|  \__||_______|\____/
```
## Created By ✍️

This project was created by: [ፚ Ꭷ Ꮢ Ꭷ ❥](https://t.me/ZORO2045).
