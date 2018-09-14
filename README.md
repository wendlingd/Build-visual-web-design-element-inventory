# Build-visual-web-design-inventory
> **Use Python / Selenium to collect screenshots of your site's design elements**

Use this code if you want to get a visual inventory of a large web site that has many different types of designs/presentations - such as if it was merged from many sources, or was built by different designers over time. You can use this result when creating a web design system.

For example, if you want a screenshot of every form on your site, you can use a spidering tool to get the list of URLs where the <form> tag is present, and feed the list to this script and automatically generate a folder of the screenshots.


## Example workflow:

1. Run spider to locate tag of interest, for example collect every URLs where the form tag is found.
2. Feed the list of URLs to this py script. Example of script capability-xpath can locate form but use 'not contains' to avoid capturing your site search box, which probably appears on most pages).
3. Import images into a photo management program.
4. Crop images to your target design element.
5. In Apple Photos I use AppleScript to automatically right the file name to the title, meaning the URL appears under the image.
5. Drag images into categories. In forms example, might be, forms to sign up for email updates, forms for database searches, forms for customer service requests, forms for evaluating services or events, license agreements, etc.
6. Output photo montages that you can use to set standards and level your design across the site, and plan your work.


## Requirements

* Python
* Selenium webdriver
