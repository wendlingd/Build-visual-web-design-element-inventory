# Build-visual-web-design-inventory
> **Use Python / Selenium to collect screenshots of your site's design elements**

Use this code if you want to get a visual inventory of a large web site that has many different types of designs/presentations - such as if it was merged from many sources, or was built by different designers over time. You can use this result when you are standardizing to a web design system.

The script automatically opens a URL, scrolls to the item you want, writes a screenshot, then goes on to the next URL.

For example, if you want a screenshot of every form on your site, you can use a spidering tool to get the list of URLs where the <form> tag is present, and feed the list to this script, which will automatically generate a folder of the screenshots.


## Example workflow:

1. Run spider to locate tag of interest, for example collect all URLs where the form tag is found.
2. Feed the list of URLs to this py script. Example of script capability-xpath can locate form but use 'not contains' to avoid capturing your site search box, which probably appears on most pages).
3. Import images into a photo management program.
4. Crop images to your target design element.
5. In Apple Photos I use AppleScript to automatically write the file name to the image title - making the URL appear under the image. I used https://discussions.apple.com/docs/DOC-8414.
5. Drag images into categories. In the forms example, we might divide the images this way: sign up for email updates, database search-simple, database search-advanced, customer service request forms, evaluating services or events, license agreements, etc.
6. Output photo montages that you can use to set standards and make your design parallel across the site, and plan the work.


## Traffic, survey reports as the source file

An alternative use could be to extract from your traffic tool, your top 150 pages by traffic, or top-traffic pages from one site area/domain, or all pages viewed last week, or all pages where survey participants were invited to take your survey and agreed (and perhaps who gave you a low satisfaction score), and show the tops of those pages, without looking for one design element. The script indicates what lines to comment out for this use. In this case you will only see what is "above the fold." 


## More info

* Put _design system_ into your favorite search engine or try http://atomicdesign.bradfrost.com/chapter-1/.


## Requirements

* Python
* Selenium webdriver
