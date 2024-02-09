import logging
import requests
from Utilities import Configuration

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set the logging level for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Define a log message format
console_handler.setFormatter(formatter)  # Set the formatter for the handler

# Get the root logger and add the StreamHandler to it
root_logger = logging.getLogger('')
root_logger.addHandler(console_handler)

def check_website(uri):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    try:
        response = requests.get(uri, headers=headers)
        if response.status_code == 200:
            print("Page loaded successfully")
            logging.info("Page loaded successfully")
        elif response.status_code == 404:
            print("Page not found")
            logging.info("Page not found")
    except Exception as e:
        error_message = str(e)
        if "HTTPSConnectionPool" in error_message:
            print("Ensure your URL and Internet connection")
            logging.info("Ensure your URL and Internet connection")
        else:
            print(f"An error occurred: {error_message}")
            logging.info(error_message)

# if __name__ == "__main__":
#     uri = "https://www.makemytrip.com/"
#     check_website(uri)

