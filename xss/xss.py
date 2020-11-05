import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def get_forms(url):
    """
    :param url: Requested url of website
    :return: Returns all forms from the HTML content
    """
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

if __name__ == "__main__":
    url = "http://apache2.willilazarov.cz/"
    forms = get_forms(url)
    print(forms)