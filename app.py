{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import pandas as pd\n",
    "\n",
    "import scrape_mars_data as smd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'c:/windows/system32': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mission_to_mars_app\"\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "# Or set inline\n",
    "#mongo = PyMongo(app, uri=\"mongodb://localhost:27017/mission_to_mars_app\")\n",
    "featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    listings = mongo.db.listings.find_one()\n",
    "    return render_template(\"index.html\", listings=listings)\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scraper():\n",
    "    listings = mongo.db.listings\n",
    "    listings_data = smd.scrape()\n",
    "    listings.update({}, listings_data, upsert=True)\n",
    "    return redirect(\"/\", code=302)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
