# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    
    fuel_price_url = "https://gasprices.aaa.com/state-gas-price-averages/"
    states = browser.find_link_by_partial_href("https://gasprices.aaa.com?state=")
    
    
    
    
    # Returning scraped data
    return mars_data