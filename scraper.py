import argparse
import requests
from bs4 import BeautifulSoup

def has_swagger_ui(subdomain):
    try:
        response = requests.get(f"http://{subdomain}")
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find(string="swagger ui") is not None
    except:
        return False

# Parse the file name from the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of the file containing the list of subdomains")
args = parser.parse_args()

# Read the list of subdomains from the file
with open(args.filename, "r") as f:
    subdomains = [line.strip() for line in f]

# Iterate through the list of subdomains and check for the presence of "swagger ui"
results = []
for subdomain in subdomains:
    has_ui = has_swagger_ui(subdomain)
    results.append((subdomain, has_ui))

# Print the results
for subdomain, has_ui in results:
    print(f"{subdomain}: {has_ui}")
