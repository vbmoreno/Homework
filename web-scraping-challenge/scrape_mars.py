{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter, BeautifulSoup, and Pandas\n",
    "import pandas as pd\n",
    "import time\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [],
   "source": [
    "#double check if chrome driver is in local drive and matches\n",
    "!which chromedriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [
    {
     "ename": "UnboundLocalError",
     "evalue": "local variable 'e' referenced before assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mUnboundLocalError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-225-cb5842163c5c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# call on chromedriver, still have problem because of chromedriver allthough I already installed and brower because splinter isn't working properly\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mexecutable_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m'executable_path'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m'/usr/local/bin/chromedriver'\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mbrowser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBrowser\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'chrome'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mexecutable_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.6/site-packages/splinter/browser.py\u001b[0m in \u001b[0;36mBrowser\u001b[0;34m(driver_name, retry_count, *args, **kwargs)\u001b[0m\n\u001b[1;32m     88\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mDriverNotFoundError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"No driver for %s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mdriver_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     89\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 90\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mget_driver\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.6/site-packages/splinter/browser.py\u001b[0m in \u001b[0;36mget_driver\u001b[0;34m(driver, retry_count, *args, **kwargs)\u001b[0m\n\u001b[1;32m     66\u001b[0m             \u001b[0;32mpass\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     67\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 68\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     69\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     70\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mUnboundLocalError\u001b[0m: local variable 'e' referenced before assignment"
     ]
    }
   ],
   "source": [
    "# call on chromedriver, still have problem because of chromedriver allthough I already installed and brower because splinter isn't working properly\n",
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Here I get to open up the page\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = bs(html,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_title = soup.find(\"div\",class_=\"content_title\").text\n",
    "\n",
    "print(f\"news_title = {news_title}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "body = soup.find_all('div', class_=\"rollover_description\")\n",
    "print(body)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Let's Start Scrapinghttps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url = \"https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA08813_hires.jpg\"\n",
    "browser.visit(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mars weather's latest tweet from the website\n",
    "mars_weather = \"https://twitter.com/MarsWxReport/status/1291899735419346944\"\n",
    "browser.visit(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "### MARS FACTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars facts from space-facts website\n",
    "mars_facts = \"https://space-facts.com/mars/\"\n",
    "table = pd.read_html(url_facts)\n",
    "table[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_facts_df = table[0]\n",
    "mars_facts_df.columns = [\"Facts\", \"Value\"]\n",
    "mars_facts_df.set_index([\"Facts\"])\n",
    "mars_facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_facts_df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "###Mars Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars facts from USGS Astrogeology website\n",
    "mars_hemisphere = \"https://space-facts.com/mars/\"\n",
    "browser.visit(mars_hemisphere)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'title': 'Cerebrus Hemisphere Enhanced', 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg': '...'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg': '...'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg': '...'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg': '...'}]\n"
     ]
    }
   ],
   "source": [
    "# Hemisphere image urls\n",
    "hemisphere_image_urls = [\n",
    "{\"title\": \"Cerebrus Hemisphere Enhanced\", \"https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg\":\"...\"},\n",
    "{\"title\": \"Schiaparelli Hemisphere Enhanced\", \"https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg\":\"...\"},\n",
    "{\"title\": \"Syrtis Major Hemisphere Enhanced\", \"https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg\":\"...\"},\n",
    "{\"title\": \"Valles Marineris Hemisphere Enhanced\", \"https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg\":\"...\"},\n",
    " ]\n",
    "print(hemisphere_image_urls)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
