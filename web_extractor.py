import requests
import html2text

def extract_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        text_content = html2text.html2text(html_content)
        return text_content
    else:
        return None

def save_content_to_file(content, filepath):
    with open(filepath, 'w') as file:
        file.write(content)

def extract_subpages_content(url, max_pages=50):
    subpages_content = []
    subpages = [url]
    count = 0

    while subpages and count < max_pages:
        subpage_url = subpages.pop(0)
        content = extract_website_content(subpage_url)
        if content:
            subpages_content.append(content)
            count += 1
            if count == max_pages:
                break
            subpages.extend(get_subpages(subpage_url, content))  # Pass the html_content argument
    return subpages_content

def get_subpages(url, html_content):  # Add the html_content parameter
    response = requests.get(url)
    if response.status_code == 200:
        subpages = extract_subpage_urls(html_content)
        return subpages
    else:
        return []

def extract_subpage_urls(html_content):  # Add the html_content parameter
    # Implement your logic to extract subpage URLs from the HTML content
    # and return a list of URLs
    pass

# Example usage
website_url = "https://www.canada.ca/en.html"

def get_subpages(url, html_content):  # Add the html_content parameter
    response = requests.get(url)
    if response.status_code == 200:
        subpages = extract_subpage_urls(html_content)
        return subpages
    else:
        return []

def extract_subpage_urls(html_content):  # Add the html_content parameter
    # Implement your logic to extract subpage URLs from the HTML content
    # and return a list of URLs
    pass

# Example usage
website_url = "https://www.canada.ca/en.html"
subpages_content = extract_subpages_content(website_url, max_pages=50)
for i, content in enumerate(subpages_content):
    filepath = f"/Users/hamedketabdar/newstart_learning/website_content_{i}.txt"
    save_content_to_file(content, filepath)
    print(f"Website content {i} saved to file.")

