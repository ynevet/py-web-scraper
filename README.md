# Py Web Scraper

Welcome to the Py Web Scraper repository! This project is a robust web scraping tool developed in Python. The purpose of this README is to guide you through the prerequisites for this project and provide instructions on how to clone and run it.

## Prerequisites

Before cloning and running this project, ensure you have the following installed:

1. **Python:** The project is written in Python. Ensure you have Python 3.x installed. You can download it [here](https://www.python.org/downloads/).

2. **pip:** This is the package installer for Python. If you installed Python from python.org, you likely already have pip. Otherwise, you can get instructions [here](https://pip.pypa.io/en/stable/installation/).

3. **Virtual Environment (Optional):** It's a good practice to run Python projects within a virtual environment to manage dependencies. You can read more about it [here](https://docs.python.org/3/tutorial/venv.html).

4. **ChromeDriver:**
   - This project uses ChromeDriver to interact with the Chrome web browser. Ensure the version of ChromeDriver aligns with your installed version of the Chrome browser.
   - You can download ChromeDriver [here](https://sites.google.com/a/chromium.org/chromedriver/). After downloading, place the `chromedriver` executable in the root folder of this project.
   - Alternatively, you can add the path of the `chromedriver` binary to your system's PATH environment variable.

## Cloning and Setting Up

Follow these steps to get the project up and running:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ynevet/py-web-scraper.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd py-web-scraper
   ```

3. **Set Up a Virtual Environment (Optional):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After setting up, you can run the main script:

```bash
python main.py
```

Upon successful execution of the script, you should expect two generated files:

- A `CSV` file.
- A `parquet` file.

Both files will contain the scraped data.

## Contributions and Issues

Feel free to fork this repository and submit pull requests. If you encounter any issues or have suggestions, please open an issue in the repository..
