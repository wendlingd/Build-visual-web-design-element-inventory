# =======================================
# Get screenshot for every URL in a file
# =======================================
'''
Last modified: 2019-11-23

This script: Turns text file with one URL per line, into screenshots of the top of each page. 

Stuff you need to do / opportunities for script improvement

- I sort my list of URLs by highest traffic first; position is passed through to the png name.
- URLs need to start with https:// or http://.
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

xpath examples (commented out in the demo code):
    /html/body/footer
    //form[@id='loginForm']
    //form[not(contains(@action, 'actionIdont-want'))] # for example site search box that is on every page
    //form[(contains(@action, 'do-want'))]")
    //button

Getting going with Selenium for Python:
    - https://selenium-python.readthedocs.io
    - https://github.com/mozilla/geckodriver (multiple drivers to choose from)
    - https://selenium.dev/selenium/docs/api/py/
    - User group, https://groups.google.com/forum/#!forum/selenium-users
'''

import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options # Other drivers such as chromedriver are available
# driver = webdriver.Firefox(executable_path = '/anaconda3/bin/geckodriver')

# Update to match your system
os.chdir('/Users/name/DesignSystem')
dataRaw = 'data/raw/' # source data
reports = 'reports/Top150/' # where to put the results

sourceListFile = dataRaw + "Top150.txt"

def save_screenshots(sourceList):
    for index, url in enumerate(sourceList):
        options = Options()
        driver = webdriver.Firefox( options=options )
        options.headless = True # some versions, options.add_argument( "--headless" )
        driver.get(url)
        # element = driver.find_element_by_xpath("//form") # comment this and next out, if you just want top of page
        # element.location_once_scrolled_into_view
        fname = url.replace("https://", "")
        fname = fname.replace("/", "-")
        fname = fname.replace(".", "-")
        fname = fname.replace("\n", "")
        index = index + 1 # most people aren't used to base zero
        i = "{:03}".format(index) # Put order into filename to match back to list or sort in photo m'ment app; assumes 999 or less
        driver.save_screenshot(reports + i + '-' + fname + '.png') # Number protects because multiple elements may appear on one page
        driver.quit()
 
sourceList = open(sourceListFile, "r")
 
save_screenshots(sourceList)
