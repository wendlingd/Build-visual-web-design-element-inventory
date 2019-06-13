# =======================================
# Get screenshot for every URL in a file
# =======================================
'''
Last modified: 2019-06-13

This script: Turns text file with one URL per line, into screenshots of the
top of each page. 

----------------
NOTES
----------------
Stuff you need to do / opportunities for script improvement

- URLs need to start with https:// or http://
- Does not capture pages that are behind authentication.
- Script can be run all at once, but check your file names/locations.
- Serving suggestion: Import into Apple Photos and turn slide show 
  into a video, with site rank-page name visible on top of screenshot.
  I used this to move file names into Title in Apple Photos;
  https://discussions.apple.com/docs/DOC-8414. 
  - Alternative to Apple Photos: Perhaps Python and PIL (Python Imaging Library) 
  would be a way to write URLs directly onto the images, but you would
  probably need both background and foreground, so it would appear reliably.
  
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
        element = driver.find_element_by_xpath("//form") # comment this and next out, if you just want top of page
        element.location_once_scrolled_into_view
        fname = url.replace("https://www.mysite.org/", "")
        fname = fname.replace("/", "-")
        fname = fname.replace(".", "-")
        fname = fname.replace("\n", "")
        driver.save_screenshot(fname + "-{}.png".format(index)) # Number protects because multiple elements may appear on one page
        driver.quit()
 
sourceList = open(sourceListFile, "r")
 
save_screenshots(sourceList)
