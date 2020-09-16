# Build-visual-web-design-inventory
> **Use Python / Selenium to collect screenshots of your site's design elements**

Use this code if you want to get a visual inventory of a large web site that has many different types of designs/presentations - such as if it was merged from many sources, or was built by different designers over time. You can use this result when you are standardizing to a web design system.

The script automatically opens a URL, scrolls to the item you want, writes a screenshot, then goes on to the next URL.

For example, if you want a screenshot of every form on your site, you can use grep or a spidering tool to get the list of URLs where the form tag is present, and feed the list to this script, which will automatically generate screenshots of the item.


## Example workflow:

1. Run spider to locate tag of interest, for example collect all URLs where the form tag is found. Some spiders can be set to capture things you want, but not what you don't want. Example: If you want all forms EXCEPT site search, perhaps an xpath statement can avoid capturing your site search box.
2. If useful, sort the list of URLs, such as to list the highest-traffic pages first.
3. Feed the list of URLs to this py script.
4. Import the resulting images into a photo management program.
5. Crop images to your target design element.
6. In Apple Photos I use AppleScript to automatically write the file name to the image title - making the URL appear under the image. I used https://discussions.apple.com/docs/DOC-8414.
7. Drag images into categories. In the forms example, we might divide the images this way: sign up for email updates; database search-simple; database search-advanced; customer service request forms; evaluating services or events; license agreements; etc.
8. Output photo montages that you can use to set standards and make your design parallel across the site, and plan the work.


## Traffic, survey reports as the source file

An alternative use could be to extract from your traffic tool, your top 150 pages by traffic, or top-traffic pages from one site area/domain, or all pages viewed last week, or all pages where survey participants were invited to take your survey and agreed (and perhaps who gave you a low satisfaction score), and show the tops of those pages, without looking for one design element. The script indicates what lines to comment out for this use. In this case, you will see what is "above the fold." 


## More info

* Put _design system_ into your favorite search engine or try http://atomicdesign.bradfrost.com/chapter-1/.


## Requirements

* Python
* Selenium webdriver


## Anaconda users / Mac

My experience with a new webdriver install for Anaconda - Mac took a lot longer than I wanted it to. The correct instructions were spread out in multiple places, so here's a boost if your configuration is Mac - Catalina or higher - Anaconda. I decided to use the Firefox geckodriver here, but I also use Chromedriver successfully.

1. See https://anaconda.org/conda-forge/selenium, conda install -c conda-forge selenium
2. Get driver. Start at https://selenium-python.readthedocs.io/installation.html. Go to the page where it's available, and download.
3. Uncompress driver in Downloads
4. Terminal: cp /Downloads/filename /destination ('which conda' command in Terminal will provide)
5. Terminal: sudo nano /etc/paths - and add the path to destination (found above); save and close
6. Terminal: echo $PATH - to make sure the new entry appears
7. Exit Terminal, try running the script.
