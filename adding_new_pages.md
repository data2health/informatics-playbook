# Adding new pages

## Creating the html file

All the pages added individually outside of sphinx's automatic page creation are located at *docs/_templates*. First create the html file (eg *new_page.html*).

Then you can either create a page from scratch or follow the **example_template.html** structure located at the root folder. The **example_template.html** template overrides some of the default theme blocks from the forked **basicstrap** theme that are not needed but also extends from *layout.html* which contains essential styles and scripts (it is recommended to extend from *layout.html*).

## Adding the html file to sphinx

After you create your html file you need to configure sphinx to locate and build this file with the rest of the pages.

Locate the **conf.py** file under the *docs* folder. Then find the **html_additional_pages** dictionary and modify it like this

`html_additional_pages = {'index': 'index.html', 'about': 'about.html', 'new_page': 'new_page.html'}`

After these steps if you run **make html** again you should be able to view your *new_page.html* in your browser.
