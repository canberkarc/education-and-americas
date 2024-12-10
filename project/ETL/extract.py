from helium import *
from time import sleep
import logging
import os
import traceback
from retry import retry
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

logging.basicConfig(filename='./log.txt',
	filemode='a',
	format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
	datefmt='%d %m %Y %H:%M:%S',
	level=logging.INFO)

def get_downloads_path():
    # Different paths based on the operating system
    if os.name == 'nt':  # Windows
        path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif os.name == 'posix':  # Unix-like systems (Linux, macOS)
        path = os.path.join(os.path.expanduser('~'), 'Downloads')
    else:
        return None  # Unsupported operating system

    # Normalize the path and replace backslashes with forward slashes
    normalized_path = os.path.normpath(path)
    return normalized_path.replace('\\', '/')

directory = get_downloads_path()

def start_custom_firefox():
    firefox_bin = "/snap/firefox/current/usr/lib/firefox/firefox"
    firefoxdriver_bin = "/snap/firefox/current/usr/lib/firefox/geckodriver"
    
    options = Options()
    options.add_argument('--headless')
    options.binary_location = firefox_bin

    service = webdriver.firefox.service.Service(executable_path=firefoxdriver_bin)

    driver = webdriver.Firefox(service=service, options=options)
    helium.set_driver(driver)

def get_last_downloaded_file(directory):
    
    try:
        logging.info("Getting the most recently downloaded file...")

        # List all files in the directory
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        # If there are no files in the directory, return None
        if not files:
            return None
        
        # Find the most recently modified file
        latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
        
        logging.info(f"The most recently modified file is: {latest_file}")

        # Return the full path of the most recently modified file
        full_path = os.path.join(directory, latest_file)
        normalized_path = os.path.normpath(full_path)

        logging.info(f"The full path of the most recently modified file is: {normalized_path}")
        return normalized_path.replace('\\', '/')
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=10, logger=logging)
# Extract GDP data
def extractGdpData():

    try:
        # Extract GDP data
        logging.info("Starting Firefox...")
        start_custom_firefox()
        driver = helium.get_driver()

        sleep(1)
        logging.info("Downloading GDP data...")
        driver.get("https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?view=chart")
        sleep(3)

        driver.execute_script("window.scrollBy(0, 500);")
        sleep(1)

        click('EXCEL')
        sleep(15)

        lastDownloadedFile = get_last_downloaded_file(directory)

        # If the file is not downloaded, try again
        logging.info("GDP data is downloaded...")
        driver.quit()

        return lastDownloadedFile
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=10, logger=logging)
# Extact illiteracy rate data
def extractIlliteracyRateData():
    
        try:
            # Extract illiteracy rate data
            logging.info("Starting Firefox...")
            start_custom_firefox()
            driver = helium.get_driver()
    
            logging.info("Opening illiteracy rate data website...")
            url = "https://statistics.cepal.org/portal/databank/index.html?lang=en&indicator_id=53&area_id=408&members=43053%2C146%2C327%2C2172%2C29170%2C29171%2C29172%2C29173%2C29174%2C29175%2C29176%2C29177%2C29178%2C29179%2C29180%2C29181%2C29182%2C29183%2C29184%2C29185%2C29186%2C29187%2C29188%2C29189%2C29190%2C29191%2C29192"
            driver.get(url)
            sleep(5)
    
            driver.execute_script("window.scrollBy(0, 500);")
    
            click('Select all')
            sleep(2)
            
            driver.execute_script("window.scrollBy(0, 500);")
            sleep(1)
            click('.XLSX')
            sleep(15)

            lastDownloadedFile = get_last_downloaded_file(directory)
    
            # If the file is not downloaded, try again
            logging.info("Illiteracy rate data is downloaded...")
            driver.quit()
             
            return lastDownloadedFile
        
        except Exception as e:
            logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=10, logger=logging)
# Extract years of education data
def extractYearsOfEducationData():

    try:
        logging.info("Starting Firefox...")
        start_custom_firefox()
        driver = helium.get_driver()

        logging.info("Opening years of education data website...")
        url = 'https://statistics.cepal.org/portal/databank/index.html?lang=en&indicator_id=1781&area_id=408&members=43053%2C146%2C327%2C1431%2C1432%2C1433%2C1434%2C29170%2C29171%2C29172%2C29173%2C29174%2C29175%2C29176%2C29177%2C29178%2C29179%2C29180%2C29181%2C29182%2C29183%2C29184%2C29185%2C29186%2C29187%2C29188%2C29189%2C29190%2C29191%2C29192'
        driver.get(url)
        sleep(5)

        driver.execute_script("window.scrollBy(0, 500);")

        click('Select all')
        sleep(2)

        # Eliminate other options to get the data for 13 years and over
        click('0 to 5 years')
        click('6 to 9 years')
        click('10 to 12 years')
        sleep(1)

        driver.execute_script("window.scrollBy(0, 500);")
        sleep(1)

        click('.XLSX')
        sleep(15)

        lastDownloadedFile = get_last_downloaded_file(directory)

        # If the file is not downloaded, try again
        logging.info("Years of education data is downloaded...")
        driver.quit()
        
        return lastDownloadedFile
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=10, logger=logging)
def extractEconomicActivityParticipationData():
    
    try:
        logging.info("Starting Firefox...")
        start_custom_firefox()
        driver = helium.get_driver()

        logging.info("Opening economic activity participation data website...")
        url = 'https://statistics.cepal.org/portal/databank/index.html?lang=en&indicator_id=1788&area_id=408&members=43053%2C146%2C327%2C1431%2C1432%2C1433%2C1434%2C29170%2C29171%2C29172%2C29173%2C29174%2C29175%2C29176%2C29177%2C29178%2C29179%2C29180%2C29181%2C29182%2C29183%2C29184%2C29185%2C29186%2C29187%2C29188%2C29189%2C29190%2C29191%2C29192'
        driver.get(url)
        sleep(5)

        driver.execute_script("window.scrollBy(0, 500);")
        sleep(1)

        click('Select all')
        sleep(2)

        # Eliminate other options to get the data for 13 years and over
        click('0 to 5 years')
        click('6 to 9 years')
        click('10 to 12 years')
        sleep(1)

        driver.execute_script("window.scrollBy(0, 500);")
        sleep(1)

        click('.XLSX')
        sleep(15)

        lastDownloadedFile = get_last_downloaded_file(directory)

        # If the file is not downloaded, try again
        logging.info("Economic activity participation data is downloaded...")
        driver.quit()
        
        return lastDownloadedFile
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

@retry(tries=3, delay=10, logger=logging)
# Extract public expenditure data
def extractPublicExpenditureData():
    try:
        logging.info("Starting Firefox...")
        start_custom_firefox()
        driver = helium.get_driver()

        logging.info("Opening public expenditure data website...")
        url = 'https://statistics.cepal.org/portal/databank/index.html?lang=en&indicator_id=460&area_id=408&members=216%2C1409%2C1411%2C29138%2C29139%2C29140%2C29141%2C29142%2C29143%2C29144%2C29145%2C29146%2C29147%2C29150%2C29151%2C29152%2C29153%2C29154%2C29155%2C29156%2C29157%2C29158%2C29159%2C29160%2C29161%2C29162%2C29163%2C29164%2C29165%2C29166%2C29167%2C29168%2C29169%2C29170%2C29171%2C29172%2C29173%2C29174%2C29175%2C29176%2C29177%2C29178%2C29179%2C29180%2C29181%2C29182%2C29183%2C29184%2C29185%2C29186%2C29187%2C29188%2C29189%2C29190%2C29191%2C29192%2C29193'
        driver.get(url)
        sleep(5)

        driver.execute_script("window.scrollBy(0, 500);")
        sleep(1)

        click('Select all')
        sleep(2)

        click('Percentage of Gross Domestic Product (GDP)')
        sleep(1)

        driver.execute_script("window.scrollBy(0, 500);")
        sleep(1)

        click('.XLSX')
        sleep(15)

        lastDownloadedFile = get_last_downloaded_file(directory)

        # If the file is not downloaded, try again
        logging.info("Public expenditure data is downloaded...")
        driver.quit()
        
        return lastDownloadedFile
    
    except Exception as e:
        logging.error(traceback.format_exc())  # Log the traceback

