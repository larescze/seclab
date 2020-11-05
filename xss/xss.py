import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def get_forms(url):
    """
    Function requests all HTML forms from website
    :param url: Requested url of website
    :return: Returns all forms from the HTML content
    """
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    Function extracts all attributes of HTML form
    :param form: HTML form
    :return: All attributes and values of HTML form
    """
    forms_details = []
    for form in forms:
        details = {}
        # get the form action attribute
        action = form.attrs.get("action")
        # get the form method attribute
        method = form.attrs.get("method", "get")
        # get all the input attributes and values
        inputs = []
        for input_tag in form.find_all(["input", "button"]):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})
        # add all attributes and values to array
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        # add all as the form array
        forms_details.append(details)
    return forms_details

if __name__ == "__main__":
    url = "http://apache1.willilazarov.cz/"
    forms = get_forms(url)
    print(get_form_details(forms))