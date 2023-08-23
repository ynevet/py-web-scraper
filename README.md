### Pre-requirments:

1. Install Python3:
    - Visit the official Python website: https://www.python.org/downloads/
    - Download the latest Python3 version.
    - Follow the installation steps and ensure you check the box that says "Add Python to PATH" during installation.

### Download & Install
1. Clone the repo: `git clone https://github.com/ynevet/py-web-scraper`

2. CD into `py-web-scraper` directory 

3. Setting up a Python Virtual Environment:
   Execute `python3 -m venv .venv`
 - Activate the virtual environment:
 - Windows: .\venv_name\Scripts\Activate

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
