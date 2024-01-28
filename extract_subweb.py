import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_subpages(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all anchor tags in the HTML
    anchor_tags = soup.find_all('a')
    
    # Extract the href attribute from each anchor tag
    subpages = [urljoin(url, tag.get('href')) for tag in anchor_tags]
    
    return subpages


# add a functoion that gets each subpage and extracts the content in plain text with no markdown or code formatting. limite the number of subpages to 10
# 50

def extract_text(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the paragraphs
    paragraphs = soup.find_all('p')
    
    # Extract the text from the paragraphs
    text = '\n\n'.join([paragraph.text for paragraph in paragraphs])
    
    return text 

# use extract_subpages to get the subpages and extract_text to get the text from each subpage
# Define the URL to be scraped  
url = 'https://en.wikipedia.org/wiki/Apple_Inc.'
subpages = extract_subpages(url)
print(subpages)

# Extract the text from each subpage
max_subpages = 100
subpage_text = [extract_text(subpage) for subpage in subpages[:max_subpages]]

# Print the text extracted from the subpages into a file
with open('subpage_text.txt', 'w') as f:
    f.write('\n\n'.join(subpage_text))



