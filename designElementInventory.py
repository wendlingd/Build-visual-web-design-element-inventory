# =======================================
# Get screenshot for every URL in a file
# =======================================
'''
Required before running: Text file with one URL per line. I use a spider to 
find elements on pages and traffic / site area to guide what subset of site 
URLs to visit.

Source URLs need to start with https or http.
What types of page elements you can target: https://selenium-python.readthedocs.io/locating-elements.html

xpath examples:
    /html/body/footer
    //form[@id='loginForm']
    //form[not(contains(@action, 'actionIdont-want'))] # for example site search box that is on every page
    //form[(contains(@action, 'do-want'))]")
    //button
'''

import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
# from selenium.webdriver.chrome.options import Options

# Set working directory
os.chdir('/Users/DesignSystem/UrlScreenshotGrabber')

# Name of the URL list to process
sourceListFile = "siteFormUrls.txt"

def save_screenshots(sourceList):
    for index, url in enumerate(sourceList):
        options = Options()
        options.add_argument( "--headless" )
        driver = webdriver.Firefox( options=options )
        # driver = webdriver.Chrome('/Users/name/anaconda3/bin/chromedriver')
        driver.get(url)
        element = driver.find_element_by_xpath("//form")
        element.location_once_scrolled_into_view
        fname = url.replace("https://www.mysite.org/", "")
        fname = fname.replace("/", "-")
        fname = fname.replace(".", "-")
        fname = fname.replace("\n", "")
        driver.save_screenshot(fname + "-{}.png".format(index)) # Number protects because multiple elements may appear on one page
        driver.quit()
 
sourceList = open(sourceListFile, "r")
 
save_screenshots(sourceList)
