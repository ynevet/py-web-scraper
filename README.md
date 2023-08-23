Follow these steps to get your Python environment set up with all the necessary packages:

1. Install Python3:
    - Visit the official Python website: https://www.python.org/downloads/
    - Download the latest Python3 version.
    - Follow the installation steps and ensure you check the box that says "Add Python to PATH" during installation.
2. Setting up a Project Directory:
    - First, ensure you have Visual Studio Code (VSCode) installed. If not, download it from here: https://code.visualstudio.com/
    - Open a terminal or command prompt.
    - Create a new directory for your project:
   mkdir MyPythonProject

- Navigate into the directory:
  cd MyPythonProject
- Open this directory with VSCode:
  code .

3. Setting up a Python Virtual Environment:
    - Inside VSCode's terminal, create a new virtual environment:
   python3 -m venv venv_name
   Replace `venv_name` with your desired virtual environment name.
    - Activate the virtual environment:
    - Windows:
   .\venv_name\Scripts\Activate

- Mac/Linux:
  source venv_name/bin/activate
- Ensure Python3 is the interpreter for your virtual environment. Within VSCode, you can select the interpreter by pressing `Ctrl+Shift+P`, typing `Python: Select Interpreter`, and then choosing the one within your virtual environment.

4. Installing the Required Packages:
    - With your virtual environment activated, install the required packages using `pip`:
   pip install webdriver-manager beautifulsoup4 pandas html5lib
5. Setting up Chrome WebDriver:
    - Determine your Chrome version by navigating to the three-dot menu in the upper right corner of your Chrome browser, selecting Help, and then About Google Chrome.
    - Visit the ChromeDriver download page: https://sites.google.com/a/chromium.org/chromedriver/downloads and download the matching version.
    - Once downloaded, you have two options:
    a. Copy the `chromedriver` binary into your `MyPythonProject` directory.
    b. Or, add the location of the `chromedriver` binary to your system's PATH variable.
6. Execute your script by running the following command:
   python main.py
7. Check-out your root folder and you'll find new created files as output of your web scraping:
   `products.csv` and `data.parquet` directory which contains a parquet file.
