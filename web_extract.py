#*******************************************************************************************************
#
#          Web Page Extractor
#
#   results = extr_link("https://sample.com/index.html")
#   results = ["https://sample.com/index.html", "https://sample.com/page1.html", ...]
#
#*******************************************************************************************************


# extraction des formulaires
def extract_forms(url, soup):
    forms = soup.find_all('form')  # Recherche tous les éléments <form> dans le contenu HTML
    extracted_forms = []

    if forms:
        for form in forms:
            form_data = []

            # Extraction des champs et types de données
            fields = form.find_all('input')
            for field in fields:
                field_name = field.name
                data_type = field.get('type')
                field_data = (field_name, data_type)
                form_data.append(field_data)

            form_action = form.get('action')

            extracted_forms.append({'fields': form_data, 'action': form_action})

    return extracted_forms



# def scrap_url(url):
#     try:
#         from .logs import log  # Importing the log function from the logs module
#         log(0, "Scraping url : "+url)
#         import requests
#         rep = requests.get(url)  # Sending a GET request to the specified URL
#         log(0, "Scraping finished")
#         return rep.text  # Returning the response text of the page
#     except:
#         log(1, "Scraping failed")
#         return "Error"


# def extr_link(page):
#     from bs4 import BeautifulSoup  # Importing the BeautifulSoup library for HTML parsing
#     from .logs import log  # Importing the log function from the logs module

#     try:
#         # Extracting links from the page
#         log(0, "Links extract started")
#         soup = BeautifulSoup(page, "html.parser")  # Creating a BeautifulSoup object with the page HTML
#         links = set()  # Creating an empty set to store the unique links

#         # Finding all <a> tags in the page and adding their href attribute to the 'links' set
#         for l in soup.find_all("a"):
#             links.add(l.get("href"))

#         log(0, "Links extract finished")

#         return links  # Returning the set of links

#     except:
#         log(1, "Links extract failed")
#         return ["Error"]  # Returning an error message in case of an exception



# def extr_form(page):
#     import requests
#     from bs4 import BeautifulSoup  # Importing the BeautifulSoup library for HTML parsing
#     from .logs import log  # Importing the log function from the logs module

#     try:
#         # Extracting forms from the page
#         log(0, "Forms extract started")
#         soup = BeautifulSoup(page, "html.parser")  # Creating a BeautifulSoup object with the page HTML
#         forms = []  # Creating an empty list to store the extracted forms

#         # Finding all <form> tags in the page and extracting their attributes (action, method, name)
#         for f in soup.find_all("form"):
#             forms.append({
#                 "action" : f.get("action"),
#                 "method" : f.get("method"),
#                 "name" : f.get("name")
#             })

#         log(0, "Forms extract finished")

#         return forms  # Returning the list of extracted forms

#     except:
#         log(1, "Forms extract failed")
#         return ["Error"]  # Returning an error message in case of an exception
