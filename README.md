# casadocs
Common Astronomy Software Applications Documentation


## Updating
The generated documentation is held in either Jupyter notebook .ipynb format 
or RestructuredText .rst format.  Jupyter notebook pages have a link at the 
to "Open in Colab" for editing.  RestructuredText files can be edited in the
Github browser window.


## Generating from Scratch

1. Scrape the latest Plone CASAdocs (creates html folder):
   ```
   $: scrapy crawl sitemap
   $: scrapy crawl full
   ```

2. Generate content pages (creates markdown folder)
   ```
   $: python scripts/convert_html.py
   ``` 

3. Generate task definitions (creates tasks folder)
   ```
   $: python scripts/xml_downloader.py
   $: python scripts/task_parser.py
   ```

4. Generate notebook files (creates docs/notebooks folder)
   ```
   $: python scripts/build_notebooks.py
   ```

5. Locally build pages to verify
   ```
   $: cd docs
   $: rm -fr _api/api
   $: rm -fr build
   $: sphinx-build -b html . ./build
   ```

